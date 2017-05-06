import math

class RSA:
    def Encrypt(self, p: int, q: int, M: int, e: int) -> int:
        #raise NotImplementedError
        n = p * q
        totient = (p - 1) * (q - 1)
        C = (M ** e) % n
        return int(C)

    def Decrypt(self, p: int, q: int, C: int, e: int) -> int:
        #raise NotImplementedError
        n = p * q
        totient = (p - 1) * (q - 1)
        d = self.reciprocal(int(e), int(totient))
        M = (C**d) % n

        return int(M)

    def reciprocal(self, e, totient):
        maximum_factor = 0

        for iii in range(2, totient):
            result = (e * iii) % totient
            if result == 1 and maximum_factor < iii:
                maximum_factor = iii
        return maximum_factor
