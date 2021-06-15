from typing import List, Tuple

from components.bar import Bar


class BarList:
    def __init__(self, bars: List[Bar], meter: Tuple[int, int] = (4, 4)):
        self.bars = bars
        self.meter = meter
