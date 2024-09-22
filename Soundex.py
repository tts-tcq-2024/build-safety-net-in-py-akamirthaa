def get_soundex_code(c):
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c.upper(), '0')  # Default to '0' for non-mapped characters


def check_for_empty_str(name):
    return "" if not name else generate_soundex(name)

def generate_soundex(name):

    # Start with the first letter (capitalized).
    soundex = name[0].upper()

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != soundex[:-1]:
            soundex += code

    soundex = soundex[:5]

    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex
