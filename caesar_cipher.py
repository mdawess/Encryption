"""Run the Caesar cipher to encrypt or decrypt a message using the English
alphabet."""

ENCRYPT = 'e'
DECRYPT = 'd'


def encrypt_letter(letter: str) -> str:
    """Return letter encrypted by shifting 3 places to the right.

    Precondition: len(letter) == 1 and letter.isupper()

    >>> encrypt_letter('V')
    'Y'
    >>> encrypt_letter('Z')
    'C'
    """
    # Translate to a number in the range 0-25.
    # 'A' translates to 0, 'B' to 1, and so on.
    ord_diff = ord(letter) - ord('A')

    # Apply the right shift; we use % to handle wrapping around the end of
    # the alphabet. The result is in the range 0-25.
    new_char_ord = (ord_diff + 3) % 26

    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))


def decrypt_letter(letter: str) -> str:
    """Return letter decrypted by shifting 3 places to the left.

    Precondition: len(letter) == 1 and letter.isupper()

    >>> decrypt_letter('Y')
    'V'
    >>> decrypt_letter('C')
    'Z'
    """
    # Translate to a number.
    ord_diff = ord(letter) - ord('A')

    # Apply the left shift.
    new_char_ord = (ord_diff - 3) % 26

    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))


def create_caesar_cipher(plaintext: str) -> str:
    """Return plaintext encrypted using the Caesar cipher.

    >>> create_caesar_cipher('NEED MORE SLEEP!  ZZZ...')
    'QHHG PRUH VOHHS!  CCC...'
    >>> create_caesar_cipher('I SOLEMNLY SWEAR THAT I AM UP TO NO GOOD.')
    'L VROHPQOB VZHDU WKDW L DP XS WR QR JRRG.'
    """
    ciphertext = ''

    for letter in plaintext:
        if letter.isupper():
            ciphertext = ciphertext + encrypt_letter(letter)
        else:
            ciphertext = ciphertext + letter

    return ciphertext


def decode_caesar_cipher(ciphertext: str) -> str:
    """Return ciphertext decrypted using the Caesar cipher.

    >>> decode_caesar_cipher('QHHG PRUH VOHHS!  CCC...')
    'NEED MORE SLEEP!  ZZZ...'
    """
    plaintext = ''

    for letter in ciphertext:
        if letter.isupper():
            plaintext = plaintext + decrypt_letter(letter)
        else:
            plaintext = plaintext + letter

    return plaintext


def main() -> None:
    """Perform the Caesar cipher encryption or decryption of the text entered
    by the program user.
    """

    text = input('Enter the text to encrypt or decrypt in uppercase letters: ')
    mode = input('Do you want to encrypt ({0}) or decrypt ({1})? '
                 .format(ENCRYPT, DECRYPT))

    if mode == ENCRYPT:
        print(create_caesar_cipher(text))
    elif mode == DECRYPT:
        print(decode_caesar_cipher(text))
    else:
        print('Invalid mode.')


if __name__ == '__main__':
    # These next two lines automatically run the docstring examples!
    # To run the program by calling function main instead, comment
    # these two lines and then uncomment the one below.
    import doctest
    doctest.testmod()

    # main()
