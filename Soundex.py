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

def check_code_state(code, prev_code):
    return code != "0" and code != prev_code


def process_char(char, soundex, prev_code):
    code = get_soundex_code(char)
    if check_code_state(code, prev_code):
        soundex += code
        prev_code = code
    return soundex, prev_code


def encode_name(name, soundex, prev_code):
    for char in name[1:]:
        soundex, prev_code = process_char(char, soundex, prev_code)
        if len(soundex) == 4:
            break
    # Pad with zeros if necessary
    soundex = soundex.ljust(4, "0")
    return soundex


def generate_soundex(name):
    if not name:
        return ""

    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    return encode_name(name, soundex, prev_code)



