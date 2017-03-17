

class HillCipher:
    def Analyse(self, plainText, cipherText):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        raise NotImplementedError

    def Decrypt(self, cipherText, key):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        raise NotImplementedError

    def Encrypt(self, plainText, key):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        raise NotImplementedError

    def Analyse3By3Key(self, plain3, cipher3):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        raise NotImplementedError

