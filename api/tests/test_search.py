import search
from mamba import description,context,it
import time

with description('Module: Search') as self:
    with context('search (users): Function utilizes /search/users endpoint'):
        with it('Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = search.search('users','lightn+repos:>5','stars','desc')
            assert type(x[0]) == int
            assert type(x[1]) == list
            assert type(x[2]) == dict
            if x[1]: assert type(x[1][0]) == dict
            print(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')
                
        with it('STRICT Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = search.search('users','light+repos:>5','stars','asc',page=2,strict =True)
            assert type(x[0]) == int
            assert type(x[1]) == list
            assert type(x[2]) == dict
            if x[1]: assert type(x[1][0]) == dict 
            print(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')

    with context('search_lazy (users): Function utilizes /search/users endpoint'):
        with it('<800 total_counts Lazy Search for search_lazy'):
            x = search.search_lazy('users','light+repos:>200','stars','desc')
            results =[]
            for i in x:
                status_code,items,headers = i
                assert type(status_code) == int
                assert type(items) == list
                assert type(headers) == dict
                results.extend(items)
                print(f'\tstatus code = {status_code};\titem list size = {len(items)}; num of headers = {len(headers)}')
            print(f'\tTotal Results Returned = {len(results)}')
        with it('Lazy Form: Lazily Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            x = search.search_lazy('users','light+repos:>5','stars','desc')
            results =[]
            for i in x:
                status_code,items,headers = i
                assert type(status_code) == int
                assert type(items) == list
                assert type(headers) == dict
                results.extend(items)
                print(f'\tstatus code = {status_code};\titem list size = {len(items)}; num of headers = {len(headers)}')
            print(f'\tTotal Results Returned = {len(results)}')
    
    with context('search (repositories): Function utilizes /search/repositories endpoint'):
        with it('Returns tuple(status_code:int,items:list(dict[n]),headers:dict)'):
            time.sleep(60) # Unauthenticated: Max 10 search requests per min
            x = search.search('repositories','stars:>1+forks:>1','stars+forks','desc')
            assert type(x[0]) == int
            assert type(x[1]) == list
            assert type(x[2]) == dict
            if x[1]: assert type(x[1][0]) == dict
            print(f'\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}')

        
