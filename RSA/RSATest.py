from RSA import RSA
import unittest

class RSATest(unittest.TestCase):
    def test_RSATestEnc1(self):
        algorithm = RSA()
        cipher = algorithm.Encrypt(11, 17, 88, 7)
        self.assertEqual(cipher, 11)

    def test_RSATestDec1(self):
        algorithm = RSA()
        plain = algorithm.Decrypt(11, 17, 11, 7)
        self.assertEqual(plain, 88)

    def test_RSATestEnc2(self):
        algorithm = RSA()
        cipher = algorithm.Encrypt(13, 19, 65, 5)
        self.assertEqual(cipher, 221)

    def test_RSATestDec2(self):
        algorithm = RSA()
        plain = algorithm.Decrypt(13, 19, 221, 5)
        self.assertEqual(plain, 65)

    def test_RSATestEnc3(self):
        algorithm = RSA()
        cipher = algorithm.Encrypt(61, 53, 70, 7)
        self.assertEqual(cipher, 2338)

    def test_RSATestDec3(self):
        algorithm = RSA()
        plain = algorithm.Decrypt(61, 53, 2338, 7)
        self.assertEqual(plain, 70)

    def test_RSATestNewEnc(self):
        algorithm = RSA()
        cipher = algorithm.Encrypt(257, 337, 18537, 17)
        self.assertEqual(cipher, 12448)

    def test_RSATestNewDec4(self):
        algorithm = RSA()
        plain = algorithm.Decrypt(257, 337, 12448, 17)
        self.assertEqual(plain, 18537)

if __name__ == "__main__":
    unittest.main()
