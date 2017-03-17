

class RailFence:
    def Analyse(self, plainText: str, cipherText: str) -> int:
        raise NotImplementedError

    def Decrypt(self, cipherText: str, key: int) -> str:
        raise NotImplementedError

    def Encrypt(self, plainText: str, key: int) -> str:
        raise NotImplementedError
