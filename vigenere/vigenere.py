import re

def reverse(s):
    "Reverses a string"
    return ''.join([c for c in s[::-1]])

def get_key(cipher, plain):
    key = letter((num(cipher) - num(plain)) % 26)
    return key

def translate(cipher, plain):
    "Discerns the key used to encrypt a given cipher from a known plain text"
    keys = []
    i = 0
    for letter in cipher:
        keys.append(get_key(letter, plain[i]))
        i += 1
    return ''.join(keys)

def decrypt(ciphertext, key):
    "Decrypts a ciphertext using the key"
    plaintext = []
    i = 0
    ignore = re.compile('[-è’( ){}_0-9,.\n\r]')
    for char in ciphertext:
        if ignore.match(char):
            plaintext.append(char)
        else:
            k = key[i]
            i += 1
            i %= len(key)
            c = num(char)
            ki = num(k)
            mi = (c - ki) % 26
            plaintext.append(letter(mi))

    return ''.join(plaintext)


def num(char):
    "Converts an ascii character to a 0 indexed number according to its position in the alphabet"
    return ord(char.lower()) - 97


def letter(key):
    "Converts a 0 indexed number into a letter"
    return chr(key + 97)

    
if __name__ == '__main__':
    import sys
    if sys.argv[1] == '-t':
        cipher = input('Please input the cipher: ')
        known_word = input('Please input the known word: ')
        print(translate(cipher, known_word))
    elif sys.argv[1] == '-d':
        ciphertext = input('Please input the ciphertext: ')
        key = input('Please input the key:')
        print(decrypt(ciphertext, key))
