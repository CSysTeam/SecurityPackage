import math

class RailFence:
    def Analyse(self, plainText: str, cipherText: str) -> int:
        raise NotImplementedError

    def Decrypt(self, cipherText: str, key: int) -> str:
        #raise NotImplementedError
        plainText = [None] * len(cipherText)
        counter = 0
        step = math.ceil(len(plainText) / key)

        for iii in range(step):
            for jjj in range( iii, len(cipherText), step ):
                plainText[counter] = cipherText[jjj]
                counter += 1

        return ''.join(plainText).lower()

    def Encrypt(self, plainText: str, key: int) -> str:
        #raise NotImplementedError
        cipher = [None] * len(plainText)
        counter = 0
        for iii in range(key):
            for jjj in range(iii, len(plainText), key):
                cipher[counter] = plainText[jjj]
                counter += 1

        return ''.join(cipher).upper()


#if __name__ == "__main__":
    #railfence = RailFence()
    #railfence.Encrypt("WEAREDISCOVEREDFLEEATONCE", 3)
