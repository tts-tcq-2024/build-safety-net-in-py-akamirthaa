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


def generate_soundex(name):
    if not name:
        return ""

    # Start with the first letter (capitalized).
    soundex = name[0].upper()

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != soundex[:-1]:
            soundex += code
    if '0' in code:
        soundex = soundex.replace('0','')
    if len(soundex) > 4:
        soundex = soundex [:5]

    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex
