import unittest
from PlayFair import PlayFair

class PlayFairTest(unittest.TestCase):

    mainPlain1 = "armuhsea"
    mainKey1 = "monoarchy"
    mainCipher1 = "rmcmbpim".upper()

    mainPlain2 = "hidethegold"
    mainKey2 = "helloworld"
    mainCipher2 = "lfgdnwdpwoav".upper()

    mainPlain3 = "comsecmeanscommunicationssecurity"
    mainPlain33 = "comsecmeanscommunjcatjonssecurjty"
    mainKey3 = "galois"
    mainCipher3 = "dlfdsdndihbddtntuebluoimcvbserulyo".upper()
    mainCipher33 = "dlfdsdndjhbddtntuebluojmcvbserulyo".upper()

    newPlain = "iseeyouthere"
    newKey = "RPMLDSAXICHKQUYEWOZGBFTVN".lower()
    newCipher = "CAOSGHZQBQBSOS".upper()

    largePlain = "theplayfaircipherusesafivebyfivetablecontainingakeywordorphrasememorizationofthekeywordandfoursimpleruleswasallthatwasrequiredtocreatethefivebyfivetableandusetheciphexlrckhtbrvmbrkhqcrxlrckhtbavheleeatgteenetnwembpqewovtdfheufiknylinthespacesinthetablewiththelettersofthekeyworddroppinganyduplicatelettersthenfilltheremainingspaceswiththerestofthelettersofthealphabetinorderusuallyiandhzittfcsoncapsegteeniohwqdpueityitintfexceruwsoftfdnpelbeoslldhtyvtorightorinsomeotherpatternsuchasaspiralbeginningintheupperlefthandcornerandendinginthecenterthekeywordtogetherwiththeconventionsforfillinginthefivebyfivetableconstitutethecipherkeyxlrckhtbrvmbrkhqcroencryptamessageonewouldbreakthemessageintodigramsgroupsoxlrckhtbemblyvterssuchthatforexamplexlrckhtbrenzloworlxlrckhtbrbecoqrvmbrkhqcrhelloworlxlrckhtbrvmbrkhqcrndmapthemoutonthekeytablxlrckhtbegkmdederxmbrkhqcrppendanuncommonmonogramtocompletethefinaldigraxlrckhtbbmhzetwolettersofthedigramareconsideredastheoppositecornersofarectangleinthekeytablexlrckhtbrctetedrdlwletavosinholohtferooksnrsofthisrectanglxlrckhtbbmhenopdzytiehslzlwrnlgisuurrulexlrckhtbbglwcdplmbrkhqcrtoeachpairoflettersintheplaintextmslxmbrkhqcrfbothlettersarethesamexlrckhtbrcwltvoqenblyvterislefxlrckhtbrvmbrkhqcrddaxlrckhtbrvmbrkhqcrafterthefirstlettexlrckhtbrdkorvsqxtheqewpphbwndboqnftvzmbrkhqcrxlrckhtbrvmbrkhqcrfthelettersappearonthesamerowofyourtablxlrckhtbbvreplacethemwiththeletterstotheirimmediaterightrespectivelyxlrckhtbbvrappingaroundtotheleftsideoftherowifaletterintheoriginalpairwasontherightsideoftheroxlrckhtbbmsmifthelettersappearonthesamecolumnofyourtablexlrckhtbreatorblgeqenmhtfekeyvtersimmediatelybelowrespectivelyxlrckhtbbvrappingaroundtothetopsideofthecolumnifaletterintheoriginalpairwasonthebottomsideofthecolumnmslxmbrkhqcrfthelettersarenotonthesameroworcolumnxlrckhtbreatorblgeqenmhtfekeyvtersonthesamerowrespectivelybutattheotherpairofcornersoftherectangledefinedbytheoriginalpaixlrckhtbbmhzeorderisimportanxlrckhtbbmfeikewmqblyvteroftheencryptedpairistheonethatliesonthesamerowasthefirstletteroftheplaintextpaixlrckhtbrvmbrkhqcrodecryptxlrckhtbeashiegtubearxmbrkhqcrppositexlrckhtbegtfdnowlxmbrkhqcrulesxlrckhtbagshfzmbrkhqcrstasxlrckhtbrvmbrkhqcrdroppinganyextraxlrckhtbrvmbrkhqcrxlrckhtbrvmbrkhqcrxlrckhtbeamhanbokoyuemezsndbittfdhgtanhswsohbahcmkitbslbshsmxlrckhtbbv"
    largeCipher = "NKROMPUIWGDEFWKBFPOBWSGKZDCXGKZDMORNRESTMOHQHQMDTKWCPEEAFRFBSWDTDTPEKYOMKWTSKLKBTKWCPEGDMBKPPFWHLATRFPTRWOSWPMMLGSQOSWDRLYFCRBZEEDDOZKNKRKGYRCUIGYKZSDTRSMRVOBNKREFWKBUNDEFINEDUNDEFINEDUNDEFINEDAKBTRDOMKZKBTKZQSDTRSTCOPZMRGKBPLKFQXQFQLKBWAWDBOHQNKKZSDTRCQNKNKRTKZZKBPPKNKKTCZOPDBBDPAWFMHSMVCPRQFDWZKTRNZZKBPNKBTGKNUMLKBDRVDHQHQHAASERWOKQKNKBDRONPKNKRTKZZKBPPKNKDOURGSCRQKTSDBRDXPVPNUQUGWMBKXKQLKBWSTDWAWDKZKBTKWISMCRPCKQZKQHQLKBZERFPOWPKLKBMORNRKEPNMRKNZXZECFHIZECFXBATKENKRDASNZZKBLPXBISWSWWFDPNRDKHQQHMHHQNKRZSUORFURKNKSMBEPETBDPMBBTCGMHHQNKREBTZKELKBTKWCPEEMAKKZKBCPKQKNKBEWMXBTQKSTPHPEGKNUQFMHHQNKRKGYRCUIGYKZSDTREWXBQKLZZKNKREFWKBEFCZUNDEFINEDUNDEFINEDEKQBCUOLDVBOWSKDSTCOPZMRCDDOTZKBTDBSWSKDHQZECGFDDVAHEPPRWPUNDEFINEDTRNZXZKBPPXBINKOMKPDRVSLATRUNDEFINEDRTXTPOPFUUNDEFINEDCREWTDUNDEFINEDKBNUTPOPFUUNDEFINEDUNDEFINEDMBVDOLKBTAZLSTNKKTCZMORNUNDEFINEDKGTBRBRBUNDEFINEDSUORMBSMXLEWNVTAQNSTAKDPNLWEATRUKZKZKBGKMSMRKHDPUNDEFINEDNKXKZOPTRNZZKBPPKNKRBKHDPVDDREWXBGCRDRBSWNKKESUAPWHZKEWBLRDWPGPDREQSMFMCKQLKBTKZQSDTRUNDEFINEDEZKZKBDRMPQKZDAPWHQKSTPKNKREPETBXBPPKNKHWDREQSMFMUNDEFINEDNKBTSARUZQKBKPNUTPCQMHKPXPFFPTRUNDEFINEDHQPEBRUNDEFINEDZEDOBIASFCPKTRNZZKBPHQNKROMPHQZKZNNANUNDEFINEDHREZFNKZZKBPPDKZKBWSTDUNDEFINEDEPQMZWTBTRNZXZKCFPNRKUNDEFINEDUNDEFINEDBVGDUNDEFINEDUNDEFINEDPGZKELKBGKBPLMKZZKUNDEFINEDBTEDUWNZNKBTCOASFCSMBESTQKLXUNDEFINEDUNDEFINEDUNDEFINEDKLKBTRNZZKBPSAORPDSTNKBODVRDPOPKZWPFMORNUNDEFINEDXDRRUWDKZKBQAKQKNKBTRNZZKBPZENKCKCFNVTDCGOMRDKHKNDRWAREQKZDQUUNDEFINEDXDPSUWFMHPDPZMBZENKRTRKNOGCKEKLKBEPCQGPTRNZZKCFQLKBPEKHHQPMASFCOSWPQLKBCFHINOGCKEKLKBEPUNDEFINEDNANKGNKRTKZZKBPSAORPDSTNKBODVREPTVLTSIUPZELSDTRUNDEFINEDROMPERNKDTCQNKNKRTKZXZKBPGQTDCGOMRTXCRTPODRWAREQKZDQUUNDEFINEDXDPSUWFMHPDPZMBZENKKZPAWHBRPKNKREPTVLQHGPTRNZZKCFQLKBPEKHHQPMASFCOSWPQLKBESNZZENAGCKEKLKBEWUPNQNANUNDEFINEDKLKBTRNZZKBPPDBTEZSTNKBODVRDPOPEEWUPNQUNDEFINEDROMPERNKDTCQNKNKRTKZXZKBPSTNKBODVRDPODRWAREQKZDQURXMONZNKKENKRDASFCPKEWBLRDWPKLKBDREQSMFMRBRKHQRBCXNKKECFHKMSURWGUNDEFINEDNKXKEDBRDHWGQAPELSMUNDEFINEDNKRKFCONTRNZXZKEPKLKBBTEDUWZKRAWGCFONKBSTKZGSLMKCWPQLKBWSTDEPOSONKBGKBPLMKZZKEPKLKBRUWGQLBZLOWGUNDEFINEDUNDEFINEDAERECUOLUNDEFINEDOBNKCKMXRDOBUNDEFINEDSUAPWHZKUNDEFINEDKLKBMPONUNDEFINEDPUBOUNDEFINEDMBNKUNDEFINEDONSWUNDEFINEDUNDEFINEDBDPAWFMHSMZCZNDPUNDEFINEDUNDEFINEDUNDEFINEDUNDEFINEDUNDEFINEDONGSMESTEZVDTKOBXBCKQLKBGKMSMNBOWSKDSIBTGKQHBNRBNANUNDEFINEDX"
    largePlainForAnlysis = "THEPLAYFAIRCIPHERUSESAFIVEBYFIVETABLECONTAININGAKEYWORDORPHRASEMEMORIZATIONOFTHEKEYWORDANDFOURSIMPLERULESWASALLTHATWASREQUIREDTOCREATETHEFIVEBYFIVETABLEANDUSETHECIPHEXLRCKHTBRVMBRKHQCRXLRCKHTBAVHELEEATGTEENETNWEMBPQEWOVTDFHEUFIKNYLINTHESPACESINTHETABLEWITHTHELETTERSOFTHEKEYWORDDROPPINGANYDUPLICATELETXTERSTHENFILXLTHEREMAININGSPACESWITHTHERESTOFTHELETTERSOFTHEALPHABETINORDERUSUALXLYIANDHZITTFCSONCAPSEGTEENIOHWQDPUEITYITINTFEXCERUWSOFTFDNPELBEOSLLDHTYVTORIGHTORINSOMEOTHERPATXTERNSUCHASASPIRALBEGINNINGINTHEUPXPERLEFTHANDCORNERANDENDINGINTHECENTERTHEKEYWORDTOGETHERWITHTHECONVENTIONSFORFILXLINGINTHEFIVEBYFIVETABLECONSTITUTETHECIPHERKEYXLRCKHTBRVMBRKHQCROENCRYPTAMESSAGEONEWOULDBREAKTHEMESXSAGEINTODIGRAMSGROUPSOXLRCKHTBEMBLYVTERSSUCHTHATFOREXAMPLEXLRCKHTBRENZLOWORLXLRCKHTBRBECOQRVMBRKHQCRHELXLOWORLXLRCKHTBRVMBRKHQCRNDMAPTHEMOUTONTHEKEYTABLXLRCKHTBEGKMDEDERXMBRKHQCRPXPENDANUNCOMXMONMONOGRAMTOCOMPLETETHEFINALDIGRAXLRCKHTBBMHZETWOLETXTERSOFTHEDIGRAMARECONSIDEREDASTHEOPXPOSITECORNERSOFARECTANGLEINTHEKEYTABLEXLRCKHTBRCTETEDRDLWLETAVOSINHOLOHTFEROOKSNRSOFTHISRECTANGLXLRCKHTBBMHENOPDZYTIEHSLZLWRNLGISUURRULEXLRCKHTBBGLWCDPLMBRKHQCRTOEACHPAIROFLETXTERSINTHEPLAINTEXTMSLXMBRKHQCRFBOTHLETTERSARETHESAMEXLRCKHTBRCWLTVOQENBLYVTERISLEFXLRCKHTBRVMBRKHQCRDXDAXLRCKHTBRVMBRKHQCRAFTERTHEFIRSTLETTEXLRCKHTBRDKORVSQXTHEQEWPPHBWNDBOQNFTVZMBRKHQCRXLRCKHTBRVMBRKHQCRFTHELETXTERSAPPEARONTHESAMEROWOFYOURTABLXLRCKHTBBVREPLACETHEMWITHTHELETXTERSTOTHEIRIMXMEDIATERIGHTRESPECTIVELYXLRCKHTBBVRAPXPINGAROUNDTOTHELEFTSIDEOFTHEROWIFALETXTERINTHEORIGINALPAIRWASONTHERIGHTSIDEOFTHEROXLRCKHTBBMSMIFTHELETTERSAPPEARONTHESAMECOLUMNOFYOURTABLEXLRCKHTBREATORBLGEQENMHTFEKEYVTERSIMMEDIATELYBELOWRESPECTIVELYXLRCKHTBBVRAPXPINGAROUNDTOTHETOPSIDEOFTHECOLUMNIFALETXTERINTHEORIGINALPAIRWASONTHEBOTXTOMSIDEOFTHECOLUMNMSLXMBRKHQCRFTHELETXTERSARENOTONTHESAMEROWORCOLUMNXLRCKHTBREATORBLGEQENMHTFEKEYVTERSONTHESAMEROWRESPECTIVELYBUTATXTHEOTHERPAIROFCORNERSOFTHERECTANGLEDEFINEDBYTHEORIGINALPAIXLRCKHTBBMHZEORDERISIMPORTANXLRCKHTBBMFEIKEWMQBLYVTEROFTHEENCRYPTEDPAIRISTHEONETHATLIESONTHESAMEROWASTHEFIRSTLETTEROFTHEPLAINTEXTPAIXLRCKHTBRVMBRKHQCRODECRYPTXLRCKHTBEASHIEGTUBEARXMBRKHQCRPXPOSITEXLRCKHTBEGTFDNOWLXMBRKHQCRULESXLRCKHTBAGSHFZMBRKHQCRSTASXLRCKHTBRVMBRKHQCRDROPPINGANYEXTRAXLRCKHTBRVMBRKHQCRXLRCKHTBRVMBRKHQCRXLRCKHTBEAMHANBOKOYUEMEZSNDBITTFDHGTANHSWSOHBAHCMKITBSLBSHSMXLRCKHTBBV".lower()
    largeKey = "pasword"
 
    def test_PlayFairTestEnc1(self):
        algorithm = PlayFair()
        cipher = algorithm.encrypt(self.mainPlain1, self.mainKey1)
        self.assertEqual(cipher , self.mainCipher1)

    def test_PlayFairTestDec1(self):
        algorithm = PlayFair()
        plain = algorithm.decrypt(self.mainCipher1, self.mainKey1)
        self.assertTrue(plain == self.mainPlain1)

    def test_PlayFairTestEnc2(self):
        algorithm = PlayFair()
        cipher = algorithm.encrypt(self.mainPlain2, self.mainKey2)
        self.assertEqual(cipher, self.mainCipher2)

    def test_PlayFairTestDec2(self):
        algorithm = PlayFair()
        plain = algorithm.decrypt(self.mainCipher2, self.mainKey2)
        self.assertEqual(plain, self.mainPlain2)

    def test_PlayFairTestEnc3(self):
        algorithm = PlayFair()
        cipher = algorithm.encrypt(self.mainPlain3, self.mainKey3)
        self.assertEqual(cipher, self.mainCipher3 or cipher == self.mainCipher33)

    def test_PlayFairTestDec3(self):
        algorithm = PlayFair()
        plain = algorithm.decrypt(self.mainCipher3, self.mainKey3)
        self.assertEqual(plain, self.mainPlain3 or plain == self.mainPlain33)

    def test_PlayFairTestEnc4(self):
        algorithm = PlayFair()
        cipher = algorithm.encrypt(self.largePlain, self.largeKey)
        self.assertEqual(cipher, self.largeCipher)

    def test_PlayFairTestDec4(self):
        algorithm = PlayFair()
        plain = algorithm.decrypt(self.largeCipher, self.largeKey)
        self.assertEqual(plain, self.largePlain)

    def test_PlayFairTestBonusAnalysis(self):
        algorithm = PlayFair()
        plain = algorithm.analyse(self.largeCipher)

        count = 0
        for iii in range(0, len(self.largePlainForAnlysis)):
            if self.largePlainForAnlysis[iii] == plain[iii]:
                count += 1

        self.assertTrue(count * 100 / self.largePlain.Length > 50)

    def test_PlayFairTestNewEnc(self):
        algorithm = PlayFair()
        cipher = algorithm.encrypt(self.newPlain, self.newKey)
        self.assertEqual(cipher, self.newCipher)

    def test_PlayFairTestNewDec(self):
        algorithm = PlayFair()
        plain = algorithm.decrypt(self.newCipher, self.newKey)
        self.assertEqual(plain, self.newPlain)

if __name__ == '__main__':
    unittest.main()
