import helpers.database_helper
import random

class PoemRepository:
    poems = []

    def __init__(self) -> None:
        poems = helpers.database_helper.get_all_poems()

    def shuffle(self):
        shuffeled_array = random.shuffle(self.poems)
        return shuffeled_array

    def retrieve_poem(self):
        shuffeled_arr = self.shuffle()
        selected_poem = random.randint(1,495)
        return shuffeled_arr[selected_poem]