def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # shifts = []
    if (keyword != "a") | (keyword != "A"):
        for i in range(len(plaintext)):
            ch = plaintext[i]
            if keyword[(len(keyword)-((len(keyword) - i) % len(keyword))) % len(keyword)].islower():
                shift = ord(keyword[(len(keyword)-((len(keyword) - i) % len(keyword))) % len(keyword)]) - ord("a")
            else:
                shift = ord(keyword[(len(keyword)-((len(keyword) - i) % len(keyword))) % len(keyword)]) - ord("A")
            # shifts.append(shift)
            if ((ch >= "a") & (ch <= "z")) | ((ch >= "A") & (ch <= "Z")):
                if ((ch.islower()) & (ord(ch) + shift > ord("z"))) | ((ch.isupper()) & (ord(ch) + shift > ord("Z"))):
                    if ch.islower():
                        ciphertext = ciphertext.__add__(chr(ord("a") + ((ord(ch) + shift - 1) - ord("z"))))
                    else:
                        ciphertext = ciphertext.__add__(chr(ord("A") + ((ord(ch) + shift - 1) - ord("Z"))))
                else:
                    ciphertext = ciphertext.__add__(chr(ord(ch) + shift))
            else:
                ciphertext = ciphertext.__add__(ch)
    else:
        ciphertext=plaintext

    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if (keyword != "a") | (keyword != "A"):
        for i in range(len(ciphertext)):
            ch = ciphertext[i]
            if keyword[(len(keyword)-((len(keyword) - i) % len(keyword))) % len(keyword)].islower():
                shift = ord(keyword[(len(keyword)-((len(keyword) - i) % len(keyword))) % len(keyword)]) - ord("a")
            else:
                shift = ord(keyword[(len(keyword)-((len(keyword) - i) % len(keyword))) % len(keyword)]) - ord("A")
            if ((ch >= "a") & (ch <= "z")) | ((ch >= "A") & (ch <= "Z")):
                if ((ch.islower()) & ((ord(ch) - shift) < ord("a"))) | (
                        (ch.isupper()) & ((ord(ch) - shift) < ord("A"))):
                    if ch.islower():
                        plaintext = plaintext.__add__(chr(ord("z") - shift + 1 + (ord(ch) - ord("a"))))
                    else:
                        plaintext = plaintext.__add__(chr(ord("Z") - shift + 1 + (ord(ch) - ord("A"))))
                else:
                    plaintext = plaintext.__add__(chr(ord(ch) - shift))
            else:
                plaintext = plaintext.__add__(ch)
                # PUT YOUR CODE HERE
    else:
        plaintext = ciphertext
    # PUT YOUR CODE HERE
    return plaintext
