import sys, os

from helpers.poem_repository import PoemRepository 

repo = PoemRepository()

poem = repo.retrieve_poem()
print(poem)