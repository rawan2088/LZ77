from .utils import Token

def find_longest_match(data, pos, search_window, look_ahead):
    best_distance = 0
    best_length = 0

    for start in range (max(0, pos - search_window), pos): #Don't search outside the search window, search until pos -pos is excluded-

        length = 0

        while pos + length < len(data) and length < look_ahead and data[start + length] == data[pos + length]:
            length += 1

        if length >= best_length and length != 0 : #>= to get the closest match, second condition to keep distance = 0 when there is no matching character
            best_length = length
            best_distance = pos - start

    return best_distance, best_length            


def compress(data, search_window, look_ahead) -> list[Token]:
    tags = []
    pos = 0

    while pos < len(data) :
        distance, length = find_longest_match(data, pos, search_window, look_ahead)

        if pos + length < len(data):
            next_char = data[pos+length]
        else:
            next_char = None

        tags.append(Token(distance, length, next_char))
        pos += length + 1

    return tags