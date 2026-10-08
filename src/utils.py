from dataclasses import dataclass
import math

# this is the closest thing we have to a struct
@dataclass
class Token:
    offset: int
    length: int
    next_char: str


def bits_required(max_value: int) -> int:
    if max_value <= 0:
        return 1

    return math.ceil(math.log2(max_value + 1))


def calculate_sizes(
    text: str,
    tokens: list[Token],
    biggest_offset: int,
    biggest_length: int
) -> tuple[int, int]:

    # Original size
    original_size = len(text) * 8

    # Bits needed for offset and length
    offset_bits = bits_required(biggest_offset)
    length_bits = bits_required(biggest_length)

    # next_char = 8 bits
    token_size = offset_bits + length_bits + 8

    compressed_size = len(tokens) * token_size

    return original_size, compressed_size