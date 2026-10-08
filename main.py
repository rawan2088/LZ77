from src.compressor import compress
from src.decompressor import decompress
from src.utils import Token, calculate_sizes



def main():
    while True:
        print(
"""
╔══════════════════════════════╗
║       LZ77 COMPRESSION       ║
╠══════════════════════════════╣
║  1. Compress File            ║
║  2. Decompress File          ║
║  3. Exit                     ║
╚══════════════════════════════╝
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            compress_file()

        elif choice == "2":
            decompress_file()

        elif choice == "3":
            print("Byyyee!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def compress_file():
    input_path = input("Enter input file path: ").strip()
    output_path = input("Enter output file path: ").strip()

    # input_path= 'str.txt'
    # output_path= 'output.txt'

    # Read input
    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()

    search_window = int(input("Enter search window size: ").strip())
    look_ahead = int(input("Enter look ahead window size: ").strip())

    # compressing stage, it should return the tokens. then we would serizlize it to a file here
    tokens = compress(text, search_window, look_ahead) 


    # Write the decompressed text to the output file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write('\n'.join(f"{token.offset} {token.length} {token.next_char}" for token in tokens))

    # The number of tokens used, 
    #todo: we can add the compression size
    print(f"Compressed into {len(tokens)} tokens.")
    
    original, compressed = calculate_sizes(text, tokens)
    print(f"Original size: {original} bits.")
    print(f"Compressed size: {compressed} bits.")
    
    print(f"Compressed successfully")
    


def decompress_file():
    input_path = input("Enter compressed file path: ").strip()
    output_path = input("Enter output file path: ").strip()
    
    # input_path = 'str.txt'
    # output_path = 'output.txt'
    
    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.strip().splitlines()
    tokens = []
    for line in lines:
        offset, length, next_char = line.split(maxsplit=2)

        if next_char == "None":
            next_char = None

        tokens.append(
            Token(
                int(offset),
                int(length),
                next_char
            )
        )
    
    # decompression stage, should return the letters resulted from the decompression
    letters = decompress(tokens)

    # Write the decompressed text to the output file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(letters)
        
    print(f"Decompressed successfully")


if __name__ == "__main__":
    main()
