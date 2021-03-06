from random import randint
from string import printable

#Atom git push test

seed = []


def generate_seed():
    """
    Generate a seed to replace every ASCII character with
    two other ASCII characters, including whitespace, etc.
    """
    global seed
    seed = []

    for char_id in range(0, len(printable)):
        while True:
            char_sequence = [printable[randint(0, len(printable)-1)], printable[randint(0, len(printable)-1)]]
            if char_sequence not in seed:
                break
        seed.append(char_sequence)


def construct_file(in_file):

    """
    Builds the file based off of the encryption key and prints it to the file
    """

    offset_seed = printable[randint(0, len(printable)-1)] # Since the seed is technically an alphabet, the offset changes where the alphabet starts, so to speak. It makes the file harder to decipher.

    generate_seed()

    write_to_file = "#encrypted "
    write_to_file += offset_seed
    write_to_file += "".join(str(two_chars) for char_sequence in seed for two_chars in char_sequence)

    for letter in in_file:
        if printable.index(letter) + printable.index(offset_seed) >= len(printable):
            write_to_file += "".join(seed[printable.index(letter) + printable.index(offset_seed) - len(printable)])
        else:
            write_to_file += "".join(seed[printable.index(letter) + printable.index(offset_seed)])

    return write_to_file
