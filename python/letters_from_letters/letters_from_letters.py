"""Letters from letters."""
import json

DATA_PATH = 'letter_map.json'
ENCODING = 'utf-8'
MAP = json.load(open(DATA_PATH, encoding=ENCODING))


def letter(char):
    """Derive letter from char."""
    return MAP.get(char)


if __name__ == '__main__':
    import sys
    for char in sys.argv[1:]:
        print(letter(char) or MAP['?'])

    
