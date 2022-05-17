def rot13(plaintext: str) -> str:
    """Returns the ciphertext resulting from encrypting `plaintext` using the rot13 algorithm"""

    for letter in str(plaintext):
        if not (letter.isspace() or letter.isalpha()):
            raise TypeError()

    encrypted_text = ""
    for letter in plaintext:
        encrypted_text += rot13_encrypt_letter(letter)
    return encrypted_text


def rot13_encrypt_letter(plain_letter):
    rot_dict = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
                "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"}
    if plain_letter.isspace():
        return " "
    elif plain_letter.isupper():
        return rot_dict[plain_letter.lower()].upper()
    else:
        return rot_dict[plain_letter]
