def get_soundex_code(c):
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c.upper(),'0')  # Default to '0' for non-mapped characters

    
# Start with the first letter (capitalized).
def get_first_letter(name):
    soundex = name[0].upper()
    return (soundex)

# Drop all occurrences of a, e, i, o, u, y, h, w
def drop_letters(name):
    list_of_letters_to_drop = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
    for letter_to_drop in name[1:]:
        if letter_to_drop in list_of_letters_to_drop:
            name = name.replace(letter_to_drop,"")
    return name


def initial_soundex(name, soundex):
    for letter in name[1:]:
        code_for_letter = get_soundex_code(letter)
        if code_for_letter != soundex[:-1]:
            soundex += code_for_letter
    return soundex

def four_characters(soundex):
    soundex = soundex[:4]
    return soundex

# Pad with zeros if necessary
def add_zeros(soundex):
    soundex = soundex.ljust(4, '0')
    return soundex

def generate_final_soundex(name):
    if name == "":
        return ""
    if name.isnumeric():
        return ""
    first_letter = get_first_letter(name)
    name_after_dropping_letters = drop_letters(name)
    initial_soundex_code = initial_soundex(name_after_dropping_letters, first_letter)
    four_char_soundex_code = four_characters (initial_soundex_code)
    zero_added_soundex_code = add_zeros(four_char_soundex_code)
    return zero_added_soundex_code
