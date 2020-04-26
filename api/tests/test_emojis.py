import emojis,utils
from mamba import description,context,it
import logging
logger = logging.getLogger(__name__)

with description('Module: Emojis') as self:
    with context('emojis: Function utilizes /emojis endpoint'):
        with it('Returns tuple(status_code:int,items:dict,headers:dict)'):
            x = emojis.emojis()
            assert type(x[0]) == int, "First Item in Tuple is of type integer"
            assert type(x[1]) == dict, "Second Item in Tuple is of type Dictionary"
            assert type(x[2]) == dict, "Third Item in Tuple is of type Dictionary"
            if x[1]: 
                if 'octocat' in x[1]: logger.info(f"\tOctocat: {x[1]['octocat']}")
            logger.info(f'\tstatus code = {x[0]};\tnum of emojis = {len(x[1])}; num of headers = {len(x[2])}')