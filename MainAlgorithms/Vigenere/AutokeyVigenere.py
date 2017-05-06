
class AutokeyVigenere:
    def vigenereTableau(self):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rows, columns = 26, 26
        vigenereTableau = [[0 for x in range(rows)] for y in range(columns)]


        for i in range(rows):
            x = i
            for j in range(columns):
                if x == 26:
                    x = 0
                vigenereTableau[i][j] = LETTERS[x]
                x = x + 1
        return vigenereTableau

    def get_keyStream(self, text, key):
        keyStream = key.upper()
        i = 0
        if len(text) != len(key):
            while len(keyStream) < len(text):
                keyStream += text.upper()[i]
                i += 1
        return keyStream

    def get_key(self, plainText, keyStream):
        print(keyStream)
        key = ""
        tmp = ""
        i = 0
        while i < len(plainText):
            if keyStream[i] != plainText.upper()[0]:
                tmp += keyStream[i]
            else:
                break
            i += 1
        key = tmp
        return key

    def Analyse(self, plainText, cipherText):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        keyStream = ""
        tmp = AutokeyVigenere()
        vigenereTableau = tmp.vigenereTableau()
        i = 0
        while i < len(cipherText):
            pIndex = LETTERS.index((plainText.upper()[i]))
            kIndex = vigenereTableau[pIndex].index(cipherText.upper()[i])
            keyStream += LETTERS[kIndex]
            i += 1
        key = tmp.get_key(plainText, keyStream.upper())
        return key.lower()

    def Decrypt(self, cipherText: str, key: str) -> str:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        decryptedText = ""
        tmp = AutokeyVigenere()
        '''
        keyStream = tmp.get_keyStream(cipherText, key)
        print(keyStream)
        '''
        keyStream = key.upper()
        vigenereTableau = tmp.vigenereTableau()
        i = 0
        while i < len(cipherText):
            kIndex = LETTERS.index((keyStream[i]))
            pIndex = vigenereTableau[kIndex].index(cipherText.upper()[i])
            decryptedText += LETTERS[pIndex]
            keyStream += decryptedText[i]
            i += 1
        return decryptedText

    def Encrypt(self, plainText: str, key: str) -> str:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        encryptedText = ""
        tmp = AutokeyVigenere()
        keyStream = tmp.get_keyStream(plainText, key)
        vigenereTableau = tmp.vigenereTableau()
        i = 0
        while i < len(plainText):
            kIndex = LETTERS.index((keyStream[i]))
            pIndex = LETTERS.index(plainText.upper()[i])
            encryptedText += vigenereTableau[kIndex][pIndex]
            i += 1
        return encryptedText
