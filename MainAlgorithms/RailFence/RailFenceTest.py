import unittest
from RailFence import RailFence

class RailFenceTest(unittest.TestCase):
    mainPlain1 = "meetmeaftertheparty"
    mainPlain2 = "meetmeafterthepartyxx"

    mainCipher = "mematrhpryetefeteat".upper()

    mainCipher2 = "mtaehayemfrereettpt".upper()
    mainCipher3 = "mtaehayemfrerxeettptx".upper()

    mainKey = 2
    mainKey2 = 3

    newPlain = "nothingisasitseems"
    newCipher = "NTIGSSTEMOHNIAISES"
    newkey = 2


    def test_RailFenceTestEnc1(self):
        algorithm = RailFence()
        cipher = algorithm.Encrypt(self.mainPlain1, self.mainKey)
        self.assertTrue(cipher, self.mainCipher)

    def test_RailFenceTestDec1(self):
        algorithm = RailFence()
        plain = algorithm.Decrypt(self.mainCipher, self.mainKey)
        self.assertTrue(plain, self.mainPlain1)

    def test_RailFenceTestAnalysis1(self):
        algorithm = RailFence()
        key = algorithm.Analyse(self.mainPlain1, self.mainCipher)
        self.assertEqual(self.mainKey, key)

    def test_RailFenceTestEnc2(self):
        algorithm = RailFence()
        cipher = algorithm.Encrypt(self.mainPlain1, self.mainKey2)
        # Add x's or not
        self.assertTrue((cipher == self.mainCipher2) or (cipher == self.mainCipher3))

    def test_RailFenceTestDec2(self):
        algorithm = RailFence()
        plain1 = algorithm.Decrypt(self.mainCipher2, self.mainKey2)
        plain2 = algorithm.Decrypt(self.mainCipher3, self.mainKey2)
        self.assertTrue((plain1 == self.mainPlain1) or (plain2 ==  self.mainPlain2))

    def test_RailFenceTestAnalysis2(self):
        algorithm = RailFence()
        key = algorithm.Analyse(self.mainPlain1, self.mainCipher2)
        key2 = algorithm.Analyse(self.mainPlain1, self.mainCipher3)
        self.assertTrue((self.mainKey2 == key) or (self.mainKey2 == key2))

    def test_RailFenceTestNewEnc(self):
        algorithm = RailFence()
        cipher = algorithm.Encrypt(self.newPlain, self.newkey)
        self.assertTrue(cipher, self.newCipher)

    def test_RailFenceTestNewDec(self):
        algorithm = RailFence()
        plain = algorithm.Decrypt(self.newCipher, self.newkey)
        self.assertTrue(plain, self.newPlain)

    def test_RailFenceTestNewAnalysis(self):
        algorithm = RailFence()
        key = algorithm.Analyse(self.newPlain, self.newCipher)
        self.assertEqual(self.newkey, key)


if __name__ == '__main__':
    unittest.main()
