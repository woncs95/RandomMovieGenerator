from justwatch import JustWatch
import random
from datamodels.movie import Movie
from datamodels.option import Option
from typing import List
import webbrowser


async def calculate_total_page_number(just_watch: JustWatch, option: Option) -> int:
    results = just_watch.search_for_item(providers=option.providers, content_types=option.content_types,
                                         page_size=option.page_size,
                                         release_year_from=option.release_year_from,
                                         page=option.page)
    total_pages = results["total_pages"]
    return total_pages


async def make_movie_lists(page: int, just_watch: JustWatch, movies: List[Movie], option: Option):
    response = just_watch.search_for_item(providers=option.providers, content_types=option.content_types,
                                          page_size=option.page_size,
                                          release_year_from=option.release_year_from,
                                          page=page)
    items_list = response["items"]

    movies.extend([Movie.from_movie_api(el) for el in items_list])


async def show_random_movie(base_url: str, just_watch: JustWatch,  movies: List[Movie], option: Option):
    total_pages = await calculate_total_page_number(just_watch, option)
    # make a list of movie id and title
    for page in range(1, total_pages + 1):
        await make_movie_lists(page, just_watch, movies, option)
    # choose random movie
    random_movie = random.choice(movies)
    movie_path = base_url + random_movie.path
    webbrowser.open(movie_path)
