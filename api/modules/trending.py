import requests
from bs4 import BeautifulSoup
from urllib.parse import splitquery
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
from constants import GITHUB_TRENDING_URL

import logging
logger = logging.getLogger(__name__)

def trending(**kwargs):
    """
    Scrapes trending endpoint on GitHub depending `kwargs` compiles meta data from html 
    `developers:bool`
    
    `since:str`

    `returns tuple(status_code:int,results:list[n],headers:dict)`
    """
    logger.info('Scraper for trending endpoint on GitHub')
    developers = False
    path = f'{GITHUB_TRENDING_URL}'
    freq = ('daily','weekly','monthly')
    if 'developers' in kwargs:
        developers = True
        path = f'{path}/developers'
        logger.debug('Constructing Trending Developer Data')
    else:
        logger.debug('Constructing Trending Repository Data')
    if 'since' in kwargs and kwargs['since'].lower() in freq:
        path = f'{path}?since={kwargs["since"].lower()}'
    
    response = requests.request('GET',path)
    status_code = response.status_code
    headers = dict(response.headers)
    if status_code != 200:
        return status_code,[],headers
    results = __parse_html_response(response.text,developers)
    return status_code,results,headers
    
def __parse_html_response(html,developer_flag):
    logger.debug('Parsing Trending HTML from GitHub')
    html_class = BeautifulSoup(html,"html.parser")
    results = []
    articles = html_class.select('article.Box-row')
    base_url = 'https://github.com'
    
    for article in articles:
        item = {}
        if developer_flag:
            __construct_developer_data(base_url,item,article)
        else:
            __construct_repository_data(base_url,item,article)

        if item:
            results.append(item)
    return results

def __construct_developer_data(base_url,item,html_tag):
    img_tag = html_tag.select_one('div > a > img.rounded-1')
    name = html_tag.select_one('div h1.h3 > a')
    repo_a_tag = html_tag.select_one('article h1.h4 > a')
    repo_description = html_tag.select_one('article div.f6.mt-1')
    repo_details = {}
    if img_tag:
        avatar = img_tag.get('src').strip()
        item['avatar'] = splitquery(avatar)[0]
        if img_tag.parent and img_tag.parent.name == 'a':
            href = img_tag.parent.get('href').strip().split('/')
            if len(href) == 2:
                username = href[-1].strip()
                profile = f'{base_url}/{username}'
                item['username'] = username
                item['profile'] = profile
    if name:
        name = name.text.strip()
        item['name'] = name
    if repo_a_tag:
        href = repo_a_tag.get('href').strip().split('/')
        if len(href) == 3:
            repo_details['name'] = href[-1].strip()
            url = f'{base_url}{"/".join(href)}'
            repo_details['url'] = url
    if repo_description:
        description = repo_description.text.strip()
        repo_details['description'] = description
    if repo_details:
        item['popular_repository'] = repo_details

def __construct_repository_data(base_url,item,html_tag):
    p_tag = html_tag.find('p')
    a_tag = html_tag.select_one('h1>a')
    span_pl_tag = html_tag.select_one('div span[itemprop="programmingLanguage"]')
    span_bg_tag = html_tag.select_one('div span.repo-language-color')
    star_svg = html_tag.select_one('div a svg.octicon.octicon-star')
    fork_svg = html_tag.select_one('div a svg.octicon.octicon-repo-forked')
    freq_star_svg = html_tag.select_one('div span svg.octicon.octicon-star')
    repo_builders = html_tag.select('div>span:contains("Built by")>a')

    if p_tag:
        item['description'] = p_tag.text.strip()
    if span_pl_tag:
        item['programming_language'] = span_pl_tag.text.strip()
        if span_bg_tag:
            item['language_color'] = span_bg_tag.get(
                'style').lower().replace('background-color','').replace(':','').strip().upper()

    if star_svg:
        if star_svg.parent and star_svg.parent.name =='a':
            star_a_tag_text = star_svg.parent.text.strip()
            try:
                item['stars'] = locale.atoi(star_a_tag_text)
            except ValueError:
                pass
    if fork_svg:
        if fork_svg.parent and fork_svg.parent.name =='a':
            fork_a_tag_text = fork_svg.parent.text.strip()
            try:
                item['forks'] = locale.atoi(fork_a_tag_text)
            except ValueError:
                pass
    if freq_star_svg:
        if freq_star_svg.parent and freq_star_svg.parent.name == 'span':
            freq_star_span_text = freq_star_svg.parent.text.strip()
            item['present_freq_stars'] = freq_star_span_text
    if a_tag:
        href = a_tag.get('href').strip().split('/')
        if len(href)>=2:
            repo = href[-1]
            author = href[-2]
            url = f'{base_url}/{author}/{repo}'
            avatar = f'{base_url}/{author}.png'
            item['name'] = repo
            item['author'] = author
            item['url'] = url
            item['avatar'] = avatar
    builders = []
    for builder in repo_builders:
        property_ = {}
        href = builder.get('href').strip().split('/')
        if len(href)==2:
            property_['username'] = href[-1].strip()
            property_['profile'] = f'{base_url}/{href[-1].strip()}'
            img_tag = builder.find('img')
            if img_tag:
                property_['avatar'] = splitquery(img_tag.get('src').strip())[0] #remove eveything after ? inclusively
        if property_:
            builders.append(property_)
    item['built_by'] = builders
        
        
if __name__ == '__main__':
    print(*trending(),sep=f'\n{"-"*50}\n')
    print(*trending(since='monthly'),sep=f'\n{"-"*50}\n')
    print(*trending(developers=True,since='weekly'),sep=f'\n{"-"*50}\n')
    
