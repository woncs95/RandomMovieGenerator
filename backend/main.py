from justwatch import JustWatch
from datamodels.movie import Movie
from datamodels.option import Option
from typing import List
from backend.services.random_movie import show_random_movie
from fastapi import FastAPI


base_url = "https://www.justwatch.com"
# initialize class
just_watch = JustWatch(country='DE')
option = Option()
# initialize list of movie object
movies: List[Movie] = []

# initialize fast api app
app = FastAPI()


@app.get("/")
async def home():
    await show_random_movie(base_url=base_url, just_watch=just_watch, option=option, movies=movies)

