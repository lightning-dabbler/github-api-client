import search
from mamba import description,context,it

with description('Get Users') as self:
    with context('Function utilizes /search/users endpoint'):
        with it('Returns a tuple: tuple[0]-> status code & tuple[0] -> list of dictionaries of metadata'):
            x = search.get_users('light+repos:>5','stars','asc')
            assert type(x[0]) == int
            assert type(x[1]) == list
            if x[1]: assert type(x[1][0]) == dict

            