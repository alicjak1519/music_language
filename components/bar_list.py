from typing import List

from components.bar import Bar


class BarList:
    def __init__(self, bars: List[Bar], metrum):
        self.bars = bars
        self.metrum = metrum
