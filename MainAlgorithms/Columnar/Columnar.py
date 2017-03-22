

class Columnar:
    def Analyse(self, plainText: str, cipherText: str) -> list:
        raise NotImplementedError

    def Decrypt(self, cipherText: str, key: list) -> str:
        """
            `key` is list of int
        """
        #raise NotImplementedError
        plainText = []
        plainText_unorganized = []

        step = int(len(cipherText) / len(key))
        for index in key:
            index -= 1
            plainText_unorganized.append(cipherText[index*step:index*step + step])

        plainText_unorganized = ''.join(plainText_unorganized)

        for iii in range(step):
            for jjj in range(iii, len(plainText_unorganized), step):
                plainText.append(plainText_unorganized[jjj])

        return ''.join(plainText).lower()
        #return plainText.lower()

    def Encrypt(self, plainText: str, key: list) -> str:
        """
            `key` is list of int
        """
        #raise NotImplementedError

        cipher = [None] * len(key)
        cipher_curr_row = 0

        for index in key:
            index = index - 1
            cipher[index] = plainText[cipher_curr_row::len(key)]
            cipher_curr_row += 1

        return ''.join(cipher).upper()


#columnar = Columnar()
#columnar.Decrypt("ctipscoeemrnuce", [ 1, 3, 4, 2, 5 ])
