class RepeatingkeyVigenere:
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
                if i == len(key):
                    i = 0
                keyStream += key.upper()[i]
                i += 1

        return keyStream

    def get_key(self, keyStream):
        key = ""
        tmp0 = ""
        index = 0
        s = 0
        i = 0
        j = 0
        while i < len(keyStream):
            if keyStream[s] == keyStream[j + 1]:
                if keyStream[s + 1] == keyStream[j + 2]:
                    index = j + 1
                    break
                s += 1
            else:
                s = 0
            j += 1
            i += 1

        print(index)
        x = 0
        while x < index:
            tmp0 += keyStream[x]
            x += 1
        key = tmp0
        return key.lower()

    def Analyse(self, plainText, cipherText):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        keyStream = ""
        tmp = RepeatingkeyVigenere()
        vigenereTableau = tmp.vigenereTableau()
        i = 0
        while i < len(cipherText):
            pIndex = LETTERS.index((plainText.upper()[i]))
            kIndex = vigenereTableau[pIndex].index(cipherText.upper()[i])
            keyStream += LETTERS[kIndex]
            i += 1
        key = tmp.get_key(keyStream)
        return key

    def  Decrypt(self, cipherText: str, key: str) -> str:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        decryptedText = ""
        tmp = RepeatingkeyVigenere()
        keyStream = tmp.get_keyStream(cipherText, key)
        vigenereTableau = tmp.vigenereTableau()
        i = 0
        while i < len(cipherText):
            kIndex = LETTERS.index((keyStream[i]))
            pIndex = vigenereTableau[kIndex].index(cipherText.upper()[i])
            decryptedText += LETTERS[pIndex]
            i += 1
        return decryptedText.lower()

    def  Encrypt(self, plainText: str, key: str) -> str:
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        encryptedText = ""
        tmp = RepeatingkeyVigenere()
        keyStream = tmp.get_keyStream(plainText, key)
        vigenereTableau = tmp.vigenereTableau()
        i = 0
        while i < len(plainText):
            kIndex = LETTERS.index((keyStream[i]))
            pIndex = LETTERS.index(plainText.upper()[i])
            encryptedText += vigenereTableau[kIndex][pIndex]
            i += 1
        return encryptedText
