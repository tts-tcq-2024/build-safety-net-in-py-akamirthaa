

def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6',
        "A": "8", "E": "8", "I": "8", "O": "8", "U": "8"
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def check_format(name):
    if not name:
        return ""
    return generate_soundex(name)

def check_code(code,prev_code):
    if code == '8':
        return True,""
    return code !='0' and code != prev_code, code

def generate_soundex(name):
    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    for char in name[1:]:
        code = get_soundex_code(char)
        returned_values = check_code(code,prev_code)
        if returned_values[0]:
            soundex += returned_values[1]
            prev_code = code
    return add_zeros(soundex)
    
def add_zeros(soundex):
    soundex = soundex[:4]
    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')
    return soundex
