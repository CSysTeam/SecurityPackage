import unittest
from HillCipher import HillCipher

class HillCipherTest(unittest.TestCase):
    key = [ 3, 2, 8, 5 ]
    plain = [ 15, 0, 24, 12, 14, 17, 4, 12, 14, 13, 4, 24 ]
    cipher = [ 19, 16, 18, 18, 24, 15, 10, 14, 16, 21, 8, 22 ]

    mainPlain = "paymoremoney"
    mainCipher = "tqssypkoqviw".upper()

    mainPlainError = "lkdi"
    mainCipherError = "SDEK".upper()

    mainPlainError2 = [ 11, 10, 3, 8 ]
    mainCipherError2 = [ 18, 3, 4, 10 ]

    keyError = [ 11, 10, 3, 8 ]

    mainKey = "dcif"


    key3 = [ 17, 17, 5, 21, 18, 21, 2, 2, 19 ]
    cipher3 = [ 11, 13, 18, 7, 3, 11, 4, 22, 12, 19, 17, 22 ]

    keyS3 = "rrfvsvcct"
    cipherS3 = "lnshdlewmtrw".upper()

    mainPlain3 = "fvcfcqtob"
    mainCipher3 = "hgrzeudvq".upper()
    mainKey3 = "bkaaubcpc"

    plain4 = [ 5, 21, 2, 5, 2, 16, 19, 14, 1 ]
    cipher4 = [ 7, 6, 17, 25, 4, 20, 3, 21, 16 ]
    key4 = [ 1, 10, 0, 0, 20, 1, 2, 15, 2 ]

    newPlain = "thegoldisburiedinorono"
    newCipher = "gzscxnvcdjzxeovcrclsrc".upper()
    newKey = "frep"

    #region integer test cases 

    def test_HillCipherTestEnc2(self):
        algorithm = HillCipher()

        cipher2 = algorithm.Encrypt(self.plain, self.key)
        for i in range(len(self.cipher)):
            self.assertEqual(self.cipher[i], cipher2[i])

    def test_HillCipherTestDec2(self):
        algorithm = HillCipher()

        plain2 = algorithm.Decrypt(self.cipher, self.key)
        for i in range(len(self.plain)):
            self.assertEqual(self.plain[i], plain2[i])

    def test_HillCipherTest2By2Analysis2(self):
        algorithm = HillCipher()

        key2 = algorithm.Analyse(self.plain, self.cipher)
        for i in range(len(self.key)):
            self.assertEqual(self.key[i], key2[i])

    def test_HillCipherTestEnc4(self):
        algorithm = HillCipher()

        cipher2 = algorithm.Encrypt(self.plain, self.key3)
        for i in range(len(self.cipher3)):
            self.assertEqual(self.cipher3[i], cipher2[i])

    def test_HillCipherTestDec4(self):
        algorithm = HillCipher()

        plain2 = algorithm.Decrypt(self.cipher3, self.key3)
        for i in range(len(self.plain)):
            self.assertEqual(self.plain[i], plain2[i])

    def test_HillCipherTestEnc6(self):
        algorithm = HillCipher()

        cipher2 = algorithm.Encrypt(self.plain4, self.key4)
        for i in range(len(self.cipher4)):
            self.assertEqual(self.cipher4[i], cipher2[i])

    def test_HillCipherTestDec6(self):
        algorithm = HillCipher()

        plain2 = algorithm.Decrypt(self.cipher4, self.key4)
        for i in range(len(self.plain4)):
            self.assertEqual(self.plain4[i], plain2[i])

    def test_HillCipherTest3By3Analysis2(self):
        algorithm = HillCipher()

        key2 = algorithm.Analyse3By3Key(self.plain4, self.cipher4)
        for i in range(len(self.key4)):
            self.assertEqual(self.key4[i], key2[i])

    #endregion

    #region test cases [Bonus]

    def test_HillCipherTestEnc1(self):
        algorithm = HillCipher()
        cipher = algorithm.Encrypt(self.mainPlain, self.mainKey)
        self.assertEqual(cipher, self.mainCipher)

    def test_HillCipherTestDec1(self):
        algorithm = HillCipher()
        plain = algorithm.Decrypt(self.mainCipher, self.mainKey)
        self.assertEqual(plain, self.mainPlain)

    def test_HillCipherTest2By2Analysis1(self):
        algorithm = HillCipher()
        key = algorithm.Analyse(self.mainPlain, self.mainCipher)
        self.assertEqual(key, self.mainKey)

    def test_HillCipherTestEnc3(self):
        algorithm = HillCipher()
        cipher = algorithm.Encrypt(self.mainPlain, self.keyS3)
        self.assertEqual(cipher, self.cipherS3)

    def test_HillCipherTestDec3(self):
        algorithm = HillCipher()
        plain = algorithm.Decrypt(self.cipherS3, self.keyS3)
        self.assertEqual(plain, self.mainPlain)

    def test_HillCipherTestEnc5(self):
        algorithm = HillCipher()
        cipher = algorithm.Encrypt(self.mainPlain3, self.mainKey3)
        self.assertEqual(cipher, self.mainCipher3)

    def test_HillCipherTestDec5(self):
        algorithm = HillCipher()
        plain = algorithm.Decrypt(self.mainCipher3, self.mainKey3)
        self.assertEqual(plain, self.mainPlain3)

    def test_HillCipherTest3By3Analysis1(self):
        algorithm = HillCipher()
        key = algorithm.Analyse3By3Key(self.mainPlain3, self.mainCipher3)
        self.assertEqual(key, self.mainKey3)

    def test_HillCipherTestNewEnc(self):
        algorithm = HillCipher()
        cipher = algorithm.Encrypt(self.newPlain, self.newKey)
        self.assertEqual(cipher, self.newCipher)

    def test_HillCipherTestNewDec(self):
        algorithm = HillCipher()
        plain = algorithm.Decrypt(self.newCipher, self.newKey)
        self.assertEqual(plain, self.newPlain)

    def test_HillCipherTestNew2By2Analysis(self):
        algorithm = HillCipher()
        key = algorithm.Analyse(self.newPlain, self.newCipher)
        self.assertEqual(key, self.newKey)

    #endregion

    #region error test cases (self.key with no inverse) 

    # [ExpectedException(typeof(InvalidAnlysisException))]
    def test_HillCipherError2(self):
        algorithm = HillCipher()

        key2 = algorithm.Analyse(self.mainPlainError2, self.mainCipherError2)

    # Decrypt with invalid key
    # [ExpectedException(typeof(System.Exception), AllowDerivedTypes = true)]
    def test_HillCipherError3(self):
        algorithm = HillCipher()

        key2 = algorithm.Decrypt(self.plain, self.keyError)

    #endregion

    #region error test cases (self.key with no inverse) [Bonus]

    # [ExpectedException(typeof(InvalidAnlysisException))]
    def test_HillCipherError1(self):
        algorithm = HillCipher()

        key2 = algorithm.Analyse(self.mainPlainError, self.mainCipherError)

    # [ExpectedException(typeof(InvalidAnlysisException), AllowDerivedTypes = true)]
    def test_HillCipherError4(self):
        algorithm = HillCipher()
        key = algorithm.Analyse3By3Key(self.mainPlain, self.cipherS3)
        self.assertEqual(key, self.keyS3)

    #endregion        


if __name__ == '__main__':
    unittest.main()
