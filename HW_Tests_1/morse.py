
"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответствие с таблицей азбуки Морзе.

    >>> encode('SOS')
    '... --- ...'

    >>> encode('HELLO WORLD')
    '.... . .-.. .-.. ---  .-- --- .-. .-.. -..'

    >>> encode('!')
    Traceback (most recent call last):
    ...
    KeyError: '!'

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter.upper()] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский.

    >>> decode('... --- ...')
    'SOS'

    >>> decode('.... . .-.. .-.. ---  .-- --- .-. .-.. -..')
    'HELLO WORLD'

    >>> decode('-- .- .. -....- .--. -.-- - ....'
      + ' --- -. -....- ..--- ----- .---- ----.')
    'MAI-PYTHON-2019'

    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
