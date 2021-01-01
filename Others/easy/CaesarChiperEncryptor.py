def caesarCipherEncryptor(string, key):

    return ''.join([chr(ord('a') + (ord(elem) - ord('a') + key) % 26) for elem in string])
