import unittest
from Columnar import Columnar


class ColumnarTest(unittest.TestCase):
    mainPlain1 = "attackpostponeduntiltwoam"
    mainPlain2 = "attackpostponeduntiltwoamxxx"
    mainkey = [ 4, 3, 1, 2, 5, 6, 7 ]

    mainCipher1 = "ttnaaptmtsuoaodwcoiknlpet".upper()
    mainCipher2 = "ttnaaptmtsuoaodwcoixknlxpetx".upper()

    mainPlain3 = "computerscience"
    mainPlain4 = "computersciencex"

    mainCipher3 = "ctipscoeemrnuce".upper()
    mainCipher4 = "cusnpremeieotcc".upper()
    mainCipher5 = "cusnprexmeieotcc".upper()

    mainkey1 = [ 1, 3, 4, 2, 5 ]
    mainkey2 = [ 1, 4, 3, 2 ]

    newPlain = "defendtheeastwallofthecastleee"
    newCipher = "nalceehwttdttfseeleedsoaefeahl"

    newKey = [ 3, 2, 6, 4, 1, 5 ]

    def test_ColumnarTestEnc1(self):
        algorithm = Columnar()
        cipher = algorithm.Encrypt(self.mainPlain1, self.mainkey)
        # Add x's or not
        self.assertTrue(cipher == self.mainCipher1 or cipher == self.mainCipher2)

    def test_ColumnarTestDec1(self):
        algorithm = Columnar()
        plain1 = algorithm.Decrypt(self.mainCipher1, self.mainkey)
        plain2 = algorithm.Decrypt(self.mainCipher2, self.mainkey)

        self.assertTrue(plain1 == self.mainPlain1 or plain2 == self.mainPlain2)

    def test_ColumnarTestAnalysis1(self):
        algorithm = Columnar()
        key1 = algorithm.Analyse(self.mainPlain1, self.mainCipher1)
        key2 = algorithm.Analyse(self.mainPlain2, self.mainCipher2)
        for i in range(len(self.mainkey)):
            self.assertTrue(self.mainkey[i] == key1[i] or self.mainkey[i] == key2[i])

    def test_ColumnarTestEnc2(self):
        algorithm = Columnar()
        cipher = algorithm.Encrypt(self.mainPlain3, self.mainkey1)
        self.assertEqual(cipher, self.mainCipher3)

    def test_ColumnarTestEnc3(self):
        algorithm = Columnar()
        cipher = algorithm.Encrypt(self.mainPlain3, self.mainkey2)

        self.assertTrue(cipher == self.mainCipher4 or cipher == self.mainCipher5)
    def test_ColumnarTestDec2(self):
        algorithm = Columnar()
        plain = algorithm.Decrypt(self.mainCipher3, self.mainkey1)
        self.assertEqual(plain, self.mainPlain3)

    def test_ColumnarTestDec3(self):
        algorithm = Columnar()
        plain1 = algorithm.Decrypt(self.mainCipher4, self.mainkey2)
        plain2 = algorithm.Decrypt(self.mainCipher5, self.mainkey2)
        self.assertTrue(plain1 ==  self.mainPlain3 or plain2 == self.mainPlain4)

    def test_ColumnarTestAnalysis2(self):
        algorithm = Columnar()
        key = algorithm.Analyse(self.mainPlain3, self.mainCipher3)

        for i in range(len(self.mainkey1)):
            self.assertEqual(self.mainkey1[i], key[i])

    def test_ColumnarTestAnalysis3(self):
        algorithm = Columnar()
        key1 = algorithm.Analyse(self.mainPlain3, self.mainCipher4)
        key2 = algorithm.Analyse(self.mainPlain4, self.mainCipher5)

        for i in range(len(self.mainkey2)):
            self.assertTrue(self.mainkey2[i] == key1[i] or self.mainkey2[i] == key2[i])

    def test_ColumnarNewTestEnc(self):
        algorithm = Columnar()
        cipher = algorithm.Encrypt(self.newPlain, self.newKey)
        self.assertEqual(cipher, self.newCipher)

    def test_ColumnarNewTestDec(self):
        algorithm = Columnar()
        plain1 = algorithm.Decrypt(self.newCipher, self.newKey)
        self.assertEqual(plain1, self.newPlain)

    def test_ColumnarNewTestAnalysis(self):
        algorithm = Columnar()
        key1 = algorithm.Analyse(self.newPlain, self.newCipher)
        for i in range(len(self.newKey)):
            self.assertEqual(self.newKey[i], key1[i])


if __name__ == '__main__':
    unittest.main()
