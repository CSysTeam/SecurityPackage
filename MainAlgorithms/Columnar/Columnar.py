

class Columnar:
    def Analyse(self, plainText: str, cipherText: str) -> list:
        raise NotImplementedError

    def Decrypt(self, cipherText: str, key: list) -> str:
        """
            `key` is list of int
        """
        raise NotImplementedError

    def Encrypt(self, plainText: str, key: list) -> str:
        """
            `key` is list of int
        """
        raise NotImplementedError
