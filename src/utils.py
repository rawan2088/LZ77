from dataclasses import dataclass

# this is the closest thing we have to a struct
@dataclass
class Token:
    offset: int
    length: int
    next_char: str

windowSize = 20;
lookaheadSize = 15;