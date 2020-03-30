import trending
from mamba import description,context,it

with description('Module: Trending') as self:
    with context('trending: Function utilizes and Scrapes https://github.com'):
        with it('Returns Trending Repositories this Month: tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = trending.trending(since='monthly') # Trending Repos this month
            assert type(x[0]) == int, "First Item in Tuple is of type integer"
            assert type(x[1]) == list ,  "Second Item in Tuple is of type List"
            assert type(x[2]) == dict ,  "Third Item in Tuple is of type Dictionary"
            if x[1]: assert type(x[1][0]) == dict,"Values in Second Item of Tuple are of type Dictionary" 
            print(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')
        
        with it('Returns Trending Developers this Week: tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = trending.trending(developers=True,since='weekly') # Trending Developers this week
            assert type(x[0]) == int, "First Item in Tuple is of type integer"
            assert type(x[1]) == list ,  "Second Item in Tuple is of type List"
            assert type(x[2]) == dict ,  "Third Item in Tuple is of type Dictionary"
            if x[1]: assert type(x[1][0]) == dict,"Values in Second Item of Tuple are of type Dictionary" 
            print(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')
