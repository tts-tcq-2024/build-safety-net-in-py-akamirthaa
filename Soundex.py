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

def check_format(name):
    if name == "":
        return ""
    if name.isnumeric():
        return ""
    return get_first_letter(name)
    
def get_first_letter(name):
    soundex = name[0].upper()
    return drop_letters(name, soundex)

def drop_letters(name, soundex):
    list_of_letters_to_drop = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
    for letter_to_drop in name[1:]:
        if letter_to_drop in list_of_letters_to_drop:
            name = name.replace(letter_to_drop,"")
    return generate_soundex(name, soundex)

def generate_soundex(name, soundex):
    # Start with the first letter (capitalized).
    for letter in name[1:]:
        code_for_letter = get_soundex_code(letter)
        if code_for_letter != soundex[:-1]:
            soundex += code_for_letter
    
    # Pad with zeros if necessary
    return four_characters(soundex)

def four_characters(soundex):
    soundex = soundex[:4]
    return add_zeros(soundex)

def add_zeros(soundex):
    soundex = soundex.ljust(4, '0')
    return soundex

print(check_format("tchebycheff"))
