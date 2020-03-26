import trending
from mamba import description,context,it

with description('Module: Trending') as self:
    with context('trending: Function utilizes and Scrapes https://github.com'):
        with it('Returns Trending Repositories this Month: tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = trending.trending(since='monthly') # Trending Repos this month
            assert type(x[0]) == int
            assert type(x[1]) == list
            assert type(x[2]) == dict
            if x[1]: assert type(x[1][0]) == dict
            print(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')