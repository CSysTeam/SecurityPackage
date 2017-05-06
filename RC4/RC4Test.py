import unittest
from RC4 import RC4


class RC4Test(unittest.TestCase):

    def RC4TestEnc1(self):
        algorithm =  RC4()
        cipher = algorithm.Encrypt("abcd", "test")
        self.assertEqual(cipher, "ÏíDu")
    

    
    def RC4TestDec1(self):
    
        algorithm =  RC4()
        cipher = algorithm.Decrypt("ÏíDu", "test")
        self.assertEqual(cipher, "abcd")
    

    
    def RC4TestEnc2(self):
    
        algorithm =  RC4()
        cipher = algorithm.Encrypt("0x61626364", "0x74657374")
        self.assertTrue(cipher, "0xcfed4475")
    

    
    def RC4TestDec2(self):
    
        algorithm =  RC4()
        cipher = algorithm.Encrypt("0xcfed4475", "0x74657374")
        self.assertTrue(cipher, "0x61626364")
    

    
    def RC4TestEnc(self):
    
        algorithm =  RC4()
        cipher = algorithm.Encrypt("aaaa", "test")
        self.assertEqual(cipher, "ÏîFp")
    

    
    def RC4TestDec(self):
    
        algorithm =  RC4()
        cipher = algorithm.Decrypt("ÏîFp", "test")
        self.assertEqual(cipher, "aaaa")
    

