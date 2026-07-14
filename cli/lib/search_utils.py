import json
import os
from typing import TypedDict


class Movie(TypedDict):
    id: int
    title: str
    description: str


DEFAULT_SEARCH_LIMIT = 5


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORDS_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")


def load_movies() -> list[Movie]:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]

def load_stopwords() -> list[str]:
    stopwords_file = open(STOPWORDS_PATH, "r")
    stopwords_content = stopwords_file.read()
    stopwords_list = stopwords_content.splitlines()
    return stopwords_list
