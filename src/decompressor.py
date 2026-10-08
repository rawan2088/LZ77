from .utils import Token

def decompress(tags):
    output = []

    for token in tags:
        offset, length, next_char = token.offset, token.length, token.next_char

        for _ in range (length):
            output.append(output[-offset]) #look offset characters back

        if next_char is not None: 
            output.append(next_char)
           

    return "".join(output)   