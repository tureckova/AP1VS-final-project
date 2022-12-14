# -*- coding: utf-8 -*-
"""Main module for translator.

VARIABLE KEY

'message' -> 'stores the string to be encoded or decoded'
'preparation_output' -> 'stores the prepared form of the message string'
'check' -> 'stores bool value, True if message is morse code, False otherwise'
'is_input_morse' -> 'stores the value of the check after preparation function'
'encrypt_output' -> 'stores the morse form of the alphanumeric string'
'txt_split' -> 'stores the morse code split up by a space in decrypt function'
'decrypt_output' -> 'stores the alphanumeric form of the morse string'
'ex' -> 'stores the boolean value of the continue or exit loop'

"""

import re  # removes extra spaces
import unicodedata  # removes diacritics
import subprocess  # copy to clipboard

morse_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                  '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                  '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
                  '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                  ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
                  '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-.',
                  ' ': '|', "'": '.----.'}
confirmation_variants = {'YES', 'YE', 'Y', 'JO', 'ANO', 'J', 'JJ', 'ZES', 'Z',
                         'ZE', 'A'}
morse_contrary = dict((v, k) for (k, v) in morse_alphabet.items())
ex = False  # Continue or Exit boolean


def preparation(txt):
    """Prepare the message for encrypting/decrypting.

    Remove spaces at the beginning and at the end of the message. Check if
    the message only has certain characters. If yes then
    check remains True and later is redirected to the encryption method. If not
    then check becomes False and later is redirected to the decryption method.

    If the message is in morse code, check for ['"'] at index [0] and [-1], if
    present, replace with morse code. If there is 2-7 spaces in the message,
    replace them with [' | '].

    If the message is in alphanumeric state, replace multiple spaces into a
    single space, remove diacritics in the message.

    Return prepared message and 'check' boolean, which is later used to
    redirect to encryption or decryption function.

    Parameters
    ----------
    txt : string
        Inserted message

    Returns
    -------
    preparation_output : string
        Returns final form of the message
    check : bool
        True if message is morse code, False otherwise

    Examples
    --------
    >>> preparation('Hello      World')
    ('Hello World', False)
    >>> preparation('...       ---   ...')
    ('... | --- | ...', True)

    """
    preparation_output = txt.strip()
    check = True
    for i in preparation_output:
        if i != '.' and i != '-' and i != ' ' and i != '|' and i != '"':
            check = False
    if check is True:
        if preparation_output[0] == '"' and preparation_output[-1] == '"':
            preparation_output = preparation_output.replace('"', ' .-..-. ')\
                .strip()
        for j in ['       ', '      ', '     ', '    ', '   ', '  ']:
            if j in preparation_output:
                preparation_output = preparation_output.replace(j, ' | ')
    if check is False:
        preparation_output = re.sub(r'\s+', ' ', preparation_output,
                                    flags=re.UNICODE)
        preparation_output = unicodedata.normalize('NFKD', preparation_output)\
            .encode('ASCII', 'ignore').decode('utf-8', 'ignore')
    return preparation_output, check


def encrypt(txt):
    """Encrypts message to morse code.

    Changes characters to capital letters, then finds characters key in the
    dictionary morse_alphabet, stores his value in a string encrypt_output
    and puts a space for another character. At the end it removes the space
    at the beginning and at the end.

    Parameters
    ----------
    txt : string
        Inserted message

    Returns
    -------
    encrypt_output : string
        Returns the encrypted message

    Examples
    --------
    >>> encrypt('SOS')
    '... --- ...'
    >>> encrypt(' Hello ')
    '| .... . .-.. .-.. --- |'
    >>> encrypt('$')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

    """
    encrypt_output = ''
    for letter in txt.upper():
        encrypt_output += morse_alphabet.get(letter) + ' '
    return encrypt_output.strip()


def decrypt(txt):
    """Decrypts message to alphanumeric characters.

    Splits the message, then for every word finds his key in dictionary
    morse_contrary and stores his value to a string decrypt_output. Which is
    than returned.

    Parameters
    ----------
    txt : string
        Inserted message

    Returns
    -------
    decrypt_output : string
        Returns the decrypted message

    Examples
    --------
    >>> decrypt('... --- ...')
    'SOS'
    >>> decrypt('...')
    'S'
    >>> decrypt('...     ---')
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "NoneType") to str

    """
    decrypt_output = ''
    txt_split = txt.split(' ')
    for sign in txt_split:
        decrypt_output += morse_contrary.get(sign)
    return decrypt_output


def copy_to_clipboard(txt):
    """Copy result to clipboard.

    Parameters
    ----------
    txt : string
        Inserted message

    """
    subprocess.run(['clip'], text=True, input=txt)


def continue_or_exit(txt):
    """Decide whether to type another string or exit.

    Parameters
    ----------
    txt : string
        Inserted message

    Returns
    -------
    ex : bool
        Returns bool value for while loop

    Examples
    --------
    >>> continue_or_exit('J')
    <BLANKLINE>
    --------------------------------------------------------------
    False

    """
    print('')
    ex = False
    if txt not in confirmation_variants:
        print('Goodbye...\n')
        ex = True
    else:
        print('--------------------------------------------------------------')
    return ex


def copy_or_not(txt):
    """Decide whether to copy to clipboard.

    Parameters
    ----------
    txt : string
        Inserted message

    """
    if txt in confirmation_variants:
        if not is_input_morse:
            copy_to_clipboard(encrypt(message))
        elif is_input_morse:
            copy_to_clipboard(decrypt(message))


def get_message(txt):
    """Get message and test it.

    If message is empty or any symbols are not in both dictionaries, print
    warning message and input line. repeat until the requirements are met.

    Parameters
    ----------
    txt : string
        Inserted message

    Returns
    -------
    txt : string
        Returns tested message

    Examples
    --------
    >>> get_message('hello')
    'hello'

    """
    while txt == '' or txt == ' ' \
            or [item for item in txt.upper() if item not
                in morse_alphabet and item not in morse_contrary]:
        if txt == '' or txt == ' ':
            print('Nothing was written...')
        elif [item for item in txt.upper() if item not in morse_alphabet
                and item not in morse_contrary]:
            print('Inserted symbols I can\'t recognize...')
        txt = str(input('Type your message: '))
    return txt


if __name__ == '__main__':
    while not ex:
        message = get_message(str(input('Type your message: ')))
        message, is_input_morse = preparation(message)
        if is_input_morse is False:
            print('Encrypted message: ' + str(encrypt(message)) + '\n')
        elif is_input_morse is True:
            print('Decrypted message: ' + str(decrypt(message)) + '\n')

        copy_or_not(input('Do you want to copy the result? Type yes '
                          'to copy: ').upper())

        ex = continue_or_exit(input('Do you want to translate another message?'
                                    ' Type yes if you do: ').upper())
