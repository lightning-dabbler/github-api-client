import logging

import trending
import utils
from mamba import context, description, it

logger = logging.getLogger(__name__)

with description("Module: Trending") as self:
    with context("trending: Function utilizes and Scrapes https://github.com"):
        with it(
            "Returns Trending Repositories this Month: tuple(status_code:int,items:list(dict[n]),headers:dict)"
        ):
            x = trending.trending(since="monthly")  # Trending Repos this month
            assert type(x[0]) == int, "First Item in Tuple is of type integer"
            assert type(x[1]) == list, "Second Item in Tuple is of type List"
            assert type(x[2]) == dict, "Third Item in Tuple is of type Dictionary"

            header_date = x[2]["Date"] == str, "header.Date type String"

            for y in x[1]:
                assert (
                    type(y) == dict
                ), "Values in Second Item of Tuple are of type Dictionary"

                assert type(y["author"]) == str, "author type String"
                assert type(y["avatar"]) == str, "avatar type String"
                built_by = y["built_by"]
                assert type(built_by) == list, "built_by type List"
                if len(built_by) > 0:
                    assert (
                        type(built_by[0]["avatar"]) == str
                    ), "built_by.avatar type String"
                    assert (
                        type(built_by[0]["profile"]) == str
                    ), "built_by.profile type String"
                    assert (
                        type(built_by[0]["username"]) == str
                    ), "built_by.username type String"
                if "description" in y:
                    assert type(y["description"]) == str, "description type String"
                assert type(y["forks"]) == int, "forks type Integer"
                assert type(y["stars"]) == int, "stars type Integer"
                if "language_color" in y:
                    assert type(
                        y["language_color"] == str
                    ), "language_color type String (optional result)"
                assert type(y["name"]) == str, "name type String"
                assert (
                    type(y["present_freq_stars"]) == str
                ), "present_freq_stars type String"
                if "programming_language" in y:
                    assert type(
                        y["programming_language"]
                    ), "programming_language type String (optional result)"
                assert type(y["url"]) == str, "url type String"

            logger.info(
                f"\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}"
            )

        with it(
            "Returns Trending Developers this Week: tuple(status_code:int,items:list(dict[n]),headers:dict)"
        ):
            x = trending.trending(
                developers=True, since="weekly"
            )  # Trending Developers this week
            assert type(x[0]) == int, "First Item in Tuple is of type integer"
            assert type(x[1]) == list, "Second Item in Tuple is of type List"
            assert type(x[2]) == dict, "Third Item in Tuple is of type Dictionary"

            header_date = x[2]["Date"] == str, "header.Date type String"

            for y in x[1]:
                assert (
                    type(y) == dict
                ), "Values in Second Item of Tuple are of type Dictionary"

                assert type(y["avatar"]) == str, "avatar type String"
                assert type(y["name"]) == str, "name type String"
                if "popular_repository" in y:
                    popular_repository = y["popular_repository"]
                    assert (
                        type(popular_repository) == dict
                    ), "popular_repository type Dict"
                    if "description" in popular_repository:
                        assert (
                            type(popular_repository["description"]) == str
                        ), "popular_repository.description type String"
                    assert (
                        type(popular_repository["name"]) == str
                    ), "popular_repository.name type String"
                    assert (
                        type(popular_repository["url"]) == str
                    ), "popular_repository.url type String"
                assert type(y["profile"]) == str, "profile type String"
                assert type(y["username"]) == str, "username type String"

            logger.info(
                f"\tstatus code = {x[0]};\titem list size = {len(x[1])}; num of headers = {len(x[2])}"
            )
