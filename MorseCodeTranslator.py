import unicodedata
import subprocess

morse_alphabet = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 
                  'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', 
                  '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', '.':'.-.-.-', ',':'--..--', '?':'..--..', '!':'-.-.--', 
                  '/':'-..-.', '(':'-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', '"':'.-..-.', '@':'.--.-.',
                  ' ':'|', "'": '.----.',}
continue_variants = {'YES', 'YE', 'Y', 'JO', "ANO", 'J', 'JJ', 'ZES', 'Z', 'ZE'} #prejmenovvat continue

morse_contrary = dict((v, k) for (k, v) in morse_alphabet.items())



def preparation(message):
    if message[0] == '"' and message[-1] == '"':
        message = message.replace('"', ' .-..-. ').strip()
    if '       ' in message:
        message = message.replace('       ', ' | ')
    if '      ' in message:
        message = message.replace('      ', ' | ')
    if '     ' in message:
        message = message.replace('     ', ' | ')
    if '    ' in message:
        message = message.replace('    ', ' | ')
    if '   ' in message:
        message = message.replace('   ', ' | ')
    if '  ' in message:
        message = message.replace('  ', ' | ')
    message = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8', 'ignore')
    return message



def remove_accent(message):
    return unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8', 'ignore')



def encrypt(message):
    encrypt_output = ''

    for letter in message.upper():
        encrypt_output += morse_alphabet.get(letter) + ' '
    return encrypt_output



def decrypt(message):
    decrypt_output = ''

    message_split = message.split(' ')

    for sign in message_split:
        decrypt_output += morse_contrary.get(sign)
    return decrypt_output
    


def addToClipBoard(txt):
    subprocess.run(['clip'], text=True, input=txt.strip())



if __name__ == '__main__':
    while True:
        message = str(input('Type your message: '))
        if message == '':
            print('Nothing was written...')
        else:
            message = preparation(message)

            check = True
            for i in message:
                if i != '.' and i != '-' and i != ' ' and i != '|':
                    check = False

            if check == False:
                print(f'Encrypted message: {encrypt(message)}\n')
                copy_or_not = input('Do you want to copy the result? Type yes if you want: ').upper()
                if copy_or_not in continue_variants:
                    addToClipBoard(encrypt(message))
            elif check == True:
                print(f'Decrypted message: {decrypt(message)}\n')
                copy_or_not = input('Do you want to copy the result? Type yes if you want: ').upper() # want do zmenit
                if copy_or_not in continue_variants:
                    addToClipBoard(decrypt(message))

            continue_or_exit = input('Do you want to translate another string? Type yes if you do: ').upper()
            print('')
            if continue_or_exit not in continue_variants:
                break

#if __name__ == '__main__':
#    while True:
#        message = str(input('Type your message: '))
#        if message == '':
#            print('Nothing was written...')
#            break
#        message = preparation(message)

#        check = True
#        for i in message:
#            if i != '.' and i != '-' and i != ' ' and i != '|':
#                check = False

#        if check == False:
#            print(f'Encrypted message: {encrypt(message)}')
#        elif check == True:
#            print(f'Decrypted message: {decrypt(message)}')

#        continue_variants = {'YES', 'YE', 'Y', 'JO', "ANO", 'J', 'JJ', 'ZES'}
#        continue_or_exit = input('Do you want to translate another string? Type yes if you do: ').upper()
#        if continue_or_exit not in continue_variants:
#            break