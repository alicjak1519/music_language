from typing import List, Tuple

from components.note import Note


class Bar:
    def __init__(self, notes: List[Note], meter: Tuple[int, int] = (4, 4)):
        self.meter = meter
        self.notes = notes
