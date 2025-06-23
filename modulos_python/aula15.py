# json.dumps e json.loads com strigs + typing.TypedDict
# Ao converter de Python para JSON:
# Python ------- JSON
# dict ------- object
# list, tuple ------- array
# str ------- string
# int, float ------- number
# True ------- true
# False ------- false
# None ------- null
import json
from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_move: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None


string_json = """
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel ",
  "original_title": "The King of the Rings: THe Fellowship of thr Ring",
  "is_move": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
"""
filme: Movie = json.loads(string_json)
# pprint(filme, width=40)
# print(filme["title"])
# print(filme["characters"][0])
# print(filme["year"])

json_string = json.dumps(filme, ensure_ascii=False, indent=2)

print(json_string)
