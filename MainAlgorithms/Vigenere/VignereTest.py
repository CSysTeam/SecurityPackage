import unittest
from RepeatingKeyVigenere import RepeatingkeyVigenere
from AutokeyVigenere import AutokeyVigenere


class VignereTest(unittest.TestCase):
    mainPlain = "wearediscoveredsaveyourself"
    mainCipherRep = "zicvtwqngrzgvtwavzhcqyglmgj".upper()
    mainCipherAuto = "zicvtwqngkzeiigasxstslvvwla".upper()
    mainKey = "deceptive"

    newPlain = "MICHIGANTECHNOLOGICALUNIVERSITY".lower()
    newCipherRep = "TWWNPZOAASWNUHZBNWWGSNBVCSLYPMM".upper()
    newCipherAuto = "TWWNPZOAFMEOVULBZMEHYIYWBMTSTNL".upper()
    newKey = "HOUGHTON".lower()

    def test_RepVignereTestEnc1(self):
        algorithm = RepeatingkeyVigenere()
        cipher = algorithm.Encrypt(self.mainPlain, self.mainKey)
        assertEqual(cipher, self.mainCipherRep)

    def test_RepVignereTestDec1(self):
        algorithm = RepeatingkeyVigenere()
        plain = algorithm.Decrypt(self.mainCipherRep, self.mainKey)
        assertEqual(plain, self.mainPlain)

    def test_RepVignereTestAnalysis1(self):
        algorithm = RepeatingkeyVigenere()
        key = algorithm.Analyse(self.mainPlain, self.mainCipherRep)
        assertEqual(key, self.mainKey)

    def test_AutoVignereTestEnc1(self):
        algorithm = AutokeyVigenere()
        cipher = algorithm.Encrypt(self.mainPlain, self.mainKey)
        assertEqual(cipher, self.mainCipherAuto)

    def test_AutoVignereTestDec1(self):
        algorithm = AutokeyVigenere()
        plain = algorithm.Decrypt(self.mainCipherAuto, self.mainKey)
        assertEqual(plain, self.mainPlain)

    def test_AutoVignereTestAnalysis1(self):
        algorithm = AutokeyVigenere()
        key = algorithm.Analyse(self.mainPlain, self.mainCipherAuto)
        assertEqual(key, self.mainKey)

    def test_RepVignereTestNewEnc(self):
        algorithm = RepeatingkeyVigenere()
        cipher = algorithm.Encrypt(self.newPlain, self.newKey)
        assertEqual(cipher, self.newCipherRep)

    def test_RepVignereTestNewDec(self):
        algorithm = RepeatingkeyVigenere()
        plain = algorithm.Decrypt(self.newCipherRep, self.newKey)
        assertEqual(plain, self.newPlain)

    def test_RepVignereTestNewAnalysis(self):
        algorithm = RepeatingkeyVigenere()
        key = algorithm.Analyse(self.newPlain, self.newCipherRep)
        assertEqual(key, self.newKey)

    def test_AutoVignereTestNewEnc(self):
        algorithm = AutokeyVigenere()
        cipher = algorithm.Encrypt(self.newPlain, self.newKey)
        assertEqual(cipher, self.newCipherAuto)

    def test_AutoVignereTestNewDec(self):
        algorithm = AutokeyVigenere()
        plain = algorithm.Decrypt(self.newCipherAuto, self.newKey)
        assertEqual(plain, self.newPlain)

    def test_AutoVignereTestNewAnalysis(self):
        algorithm = AutokeyVigenere()
        key = algorithm.Analyse(self.newPlain, self.newCipherAuto)
        assertEqual(key, self.newKey)


if __name__ == '__main__':
    unittest.main()
