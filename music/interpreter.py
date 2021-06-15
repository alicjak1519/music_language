from typing import List

from components.bar import Bar


class Interpreter:
    def __init__(self, bars_lists: List[Bar], timbre):
        self.bars_lists = bars_lists

    def play(self):
        print("PLAYYY!")
