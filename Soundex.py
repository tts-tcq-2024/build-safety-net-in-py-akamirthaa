def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters
def generate_soundex(name):
    if not name:
        return ""
    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    for letter in name[1:]:
        code_for_letter = get_soundex_code(letter)
        if code_for_letter != 0 and code_for_letter != soundex[-1]:
            soundex += code_for_letter
    return add_zeros(soundex[:4])
    
def add_zeros(soundex):
    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')
    return soundex
