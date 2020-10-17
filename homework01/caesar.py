import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    remain = ""
    # PUT YOUR CODE HERE
    if (shift != 0):
        for ch in plaintext:
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
        ciphertext = plaintext
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    if (shift != 0):
        for ch in ciphertext:
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
        plaintext=ciphertext
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
