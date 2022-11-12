import helpers.database_helper
import random

class PoemRepository:
    poems = []

    def __init__(self) -> None:
        self.poems = helpers.database_helper.get_all_poems()

    def shuffle(self):
        random.shuffle(self.poems)

    def retrieve_poem(self):
        self.shuffle()
        selected_poem = random.randint(1,495)
        poem = self.poems[selected_poem][0]
        return poem