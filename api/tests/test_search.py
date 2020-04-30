import search,utils
from mamba import description,context,it
import logging
logger = logging.getLogger(__name__)

with description('Module: Search') as self:
    with context('search (users): Function utilizes /search/users endpoint'):
        with it('STRICT Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = search.search('users','light+repos:>5','stars','asc',strict =True)
            assert type(x[0]) == int, "First Item in Tuple is of type integer"
            assert type(x[1]) == list,  "Second Item in Tuple is of type List"
            assert type(x[2]) == dict,  "Third Item in Tuple is of type Dictionary"
            for y in x[1]: 
                assert type(y) == dict, "Values in Second Item of Tuple are of type Dictionary" 
                assert type(y['avatar_url'])==str, "avatar_url type String"
                assert type(y['html_url'])==str, "html_url type String"
                assert type(y['login'])==str, "login type String"

            logger.info(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')

    with context('search_lazy (users): Function utilizes /search/users endpoint'):
        with it('Lazy Form: Lazily Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            generator = search.search_lazy('users','light+repos:>5','stars','desc')
            x1 = next(generator)
            assert type(x1[0]) == int, "First Item in Tuple is of type integer"
            assert type(x1[1]) == list,  "Second Item in Tuple is of type List"
            assert type(x1[2]) == dict,  "Third Item in Tuple is of type Dictionary"
            for y in x1[1]: 
                assert type(y) == dict, "Values in Second Item of Tuple are of type Dictionary" 
                assert type(y['avatar_url'])==str, "avatar_url type String"
                assert type(y['html_url'])==str, "html_url type String"
                assert type(y['login'])==str, "login type String"

            logger.info(f'\tstatus code = {x1[0]};\titem list size = {len(x1[1])}; num of headers = {len(x1[2])}')    
            
            x2 = next(generator)
            assert type(x2[0]) == int, "First Item in Tuple is of type integer"
            assert type(x2[1]) == list,  "Second Item in Tuple is of type List"
            assert type(x2[2]) == dict,  "Third Item in Tuple is of type Dictionary"
            for y in x2[1]: 
                assert type(y) == dict, "Values in Second Item of Tuple are of type Dictionary" 
                assert type(y['avatar_url'])==str, "avatar_url type String"
                assert type(y['html_url'])==str, "html_url type String"
                assert type(y['login'])==str, "login type String"

            logger.info(f'\tstatus code = {x2[0]};\titem list size = {len(x2[1])}; num of headers = {len(x2[2])}')  
    
    with context('search (repositories): Function utilizes /search/repositories endpoint'):
        with it('Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = search.search('repositories','stars:>1+forks:>1','stars+forks','desc',strict =True)
            assert type(x[0]) == int , "First Item in Tuple is of type integer"
            assert type(x[1]) == list ,  "Second Item in Tuple is of type List"
            assert type(x[2]) == dict ,  "Third Item in Tuple is of type Dictionary"
            for y in x[1]: 
                assert type(y) == dict,"Values in Second Item of Tuple are of type Dictionary"
                assert type(y['forks_count']) == int, "forks_count type Integer"
                assert type(y['stargazers_count']) == int, "stargazers_count type Integer"
                assert type(y['watchers_count']) == int, "watchers_count type Integer"
                assert type(y['html_url']) == str, "html_url type String"
                if 'description' in y: assert type(y['description']) in (str,type(None)), "description type String or NoneType"
                if 'language' in y: assert type(y['language']) in (str,type(None)), "language type String or NoneType"
                assert type(y['name']) == str, "name type String"
                owner = y['owner']
                assert type(owner) == dict, "owner type Dictionary"
                assert type(owner['avatar_url']) == str, "owner.avatar_url type String"
                assert type(owner['html_url']) == str, "owner.html_url type String"
                assert type(owner['login']) == str, "owner.login type String"

            logger.info(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')

    with context('search (commits): Function utilizes /search/commits endpoint'):
        with it('Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = search.search('commits','test+repo:vuejs/vue',strict =True)
            assert type(x[0]) == int , "First Item in Tuple is of type integer"
            assert type(x[1]) == list  ,  "Second Item in Tuple is of type List"
            assert type(x[2]) == dict  ,  "Third Item in Tuple is of type Dictionary"
            for y in x[1]: 
                assert type(y) == dict, "Values in Second Item of Tuple are of type Dictionary" 
                commit = y['commit']
                assert type(commit) == dict, "commit type Dictionary"
                assert type(commit['message']) == str, "commit.message type String"
                assert type(commit['author']['date']) == str, "commit.author.date type String"
                assert type(commit['author']['email']) == str, "commit.author.email type String"
                assert type(commit['author']['name']) == str, "commit.author.name type String"
                assert type(y['html_url']) == str, "html_url type String"
                repository = y['repository']
                assert type(repository) == dict, "repository type Dictionary"
                assert type(repository['name']) == str,"repository.name type String"
                assert type(repository['owner']['login']) == str,"repository.owner.login type String"
                assert type(repository['html_url']) == str,"repository.html_url type String"

            logger.info(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')
        
        
