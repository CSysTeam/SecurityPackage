﻿

class Monoalphabetic:
    """ Frequency Information:
        E   12.51%
        T	9.25
        A	8.04
        O	7.60
        I	7.26
        N	7.09
        S	6.54
        R	6.12
        H	5.49
        L	4.14
        D	3.99
        C	3.06
        U	2.71
        M	2.53
        F	2.30
        P	2.00
        G	1.96
        W	1.92
        Y	1.73
        B	1.54
        V	0.99
        K	0.67
        X	0.19
        J	0.16
        Q	0.11
        Z	0.09
    """

    def analyse(self, plainText: str, cipherText: str) -> str:
        raise NotImplementedError

    def decrypt(self, cipherText: str, key: str) -> str:
        raise NotImplementedError

    def encrypt(self, plainText: str, key: str) -> str:
        raise NotImplementedError

    def analyseUsingCharFrequency(self,  cipher: str) -> str:
        raise NotImplementedError
