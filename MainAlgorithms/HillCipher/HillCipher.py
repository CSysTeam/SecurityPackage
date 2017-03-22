import math
import numpy as np

class HillCipher:
    def Analyse(self, plainText, cipherText):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        var_type= type(plainText)
        if var_type ==  str:
            plainText = [(ord(i)-97) for i in plainText]

        var_type= type(cipherText)
        if var_type ==  str:
            cipherText = cipherText.lower()
            cipherText = [(ord(i)-97) for i in cipherText]

        start_index =0
        plainMatrix = [[0 for row in range(2)] for column in range(2)]
        cipherMatrix = [[0 for row in range(2)] for column in range(2)]
        resMatrix = [[0 for row in range(2)] for column in range(2)]
        tmpres = [[0 for row in range(2)] for column in range(2)]
        res = []

        tmp = plainText[start_index:4]
        counter = 0
        for column in range(2):
            for row in range(2):
                plainMatrix[row][column] = tmp[counter]
                counter = counter+1

        tmp = cipherText[start_index:4]
        counter = 0
        for column in range(2):
            for row in range(2):
                cipherMatrix[row][column] = tmp[counter]
                counter = counter+1

        det =round((np.linalg.det(cipherMatrix)) %26, 0)

        if (det == 1):
            b = det
        else:
            c = 1/((26-det) % 26)
            if (c <1):
                i = 1
                while(c < 1):
                    c=(26*i +1)/((26-det) % 26)
                    i = i+1
            b = round((26- c),0)

        for row in range(2):
            for column in range(2):
                sign = math.pow((-1), (row+column))
                for row2 in range(2):
                    for column2 in range (2):
                        if (row2 != row) and (column2 != column):
                            tmp = cipherMatrix[row2][column2]
                resMatrix[column][row] =int(round(( b*sign* tmp % 26), 0))

        tmpres= np.matmul(plainMatrix, resMatrix) %26

        for row in range(2):
            for column in range(2):
                res.append(tmpres[row][column])

        if var_type is str:
            res = [chr(i+97) for i in res]
            res= ''.join(res)

        return res
        #raise NotImplementedError

    def Decrypt(self, cipherText, key):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """

        var_type= type(cipherText)
        if var_type ==  str:
            cipherText = cipherText.lower()
            cipherText = [(ord(i)-97) for i in cipherText]
            key = [(ord(i)-97) for i in key]

        keyLen = len(key)
        length = int(math.sqrt(keyLen))
        keyMatrix = [[0 for row in range(length)] for column in range(length)]
        resMatrix = [[0 for row in range(length)] for column in range(length)]
        extraLen = length - (len(cipherText) % length)
        cipherLen = len(cipherText)-1
        tmpres = []
        res = []
        tmparr = [[0 for row in range(length-1)]for column in range(length-1)]
        tmp = []

    #    for i in range(extraLen):
     #       cipherText.append(cipherText[cipherLen])

        counter = 0
        for row in range(length):
            for column in range(length):
                keyMatrix[row][column] = key[counter]
                counter = counter+1

        det = round(np.linalg.det(keyMatrix) %26,0)
        c = 1/((26-det) % 26)
        if (c <1):
            i = 1
            while(c < 1):
                c=(26*i +1)/((26-det) % 26)
                i = i+1
        b = (26- c)

        for row in range(length):
            for column in range(length):
                sign = math.pow((-1), (row+column))
                for row2 in range(length):
                    for column2 in range (length):
                        if (row2 != row) and (column2 != column):
                            tmp.append( keyMatrix[row2][column2])
                for i in range(length-1):
                    for j in range(length-1):
                        tmparr[i][j] = tmp.pop()
                tmpdet= np.linalg.det(tmparr)
                resMatrix[column][row] =int(round(( b*sign* tmpdet % 26), 0))

        Len  = int(len(cipherText)/length)
        counter = 0
        for num in range(Len):
            tmp = []
            for i in range(length):
                if(counter < len(cipherText)):
                    tmp.append(cipherText[counter])
                    counter = counter+1
            tmpRes= np.matmul(resMatrix, tmp) %26
            for i in range(length):
                res.append(tmpRes[i])

        if var_type is str:
            res = [chr(i+97) for i in res]
            res= ''.join(res)


        return res

    def Encrypt(self, plainText, key):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        var_type= type(plainText)
        if var_type ==  str:
            plainText = [(ord(i)-97) for i in plainText]
            key = [(ord(i)-97) for i in key]

        keyLen = len(key)
        length = int(math.sqrt(keyLen))
        keyMatrix = [[0 for row in range(length)] for column in range(length)]
        extraLen = (len(plainText) % length)
        plainLen = len(plainText)-1
        tmpRes = []
        res = []

        for i in range(extraLen):
            plainText.append(plainText[plainLen])

        counter = 0
        for row in range(length):
            for column in range(length):
                keyMatrix[row][column] = key[counter]
                counter = counter+1

        Len  = int(len(plainText)/length)
        counter = 0
        for num in range(Len):
            tmp = []
            for i in range(length):
                if(counter < len(plainText)):
                    tmp.append(plainText[counter])
                    counter = counter+1
            tmpRes= np.matmul(keyMatrix, tmp) %26
            for i in range(length):
                res.append(tmpRes[i])

        if var_type is str:
            res = [chr(i+97) for i in res]
            res= ''.join(res)
            res = res.upper()



        return res
        # raise NotImplementedError

    def Analyse3By3Key(self, plain3, cipher3):
        """
            @Params1: str, str
            @return1: str
            @Params2: list(int), list(int)
            @return2: list(int)
        """
        var_type= type(plain3)
        if var_type ==  str:
            plain3 = [(ord(i)-97) for i in plain3]

        var_type= type(cipher3)
        if var_type ==  str:
            cipher3 = cipher3.lower()
            cipher3 = [(ord(i)-97) for i in cipher3]

        start_index =0
        plainMatrix = [[0 for row in range(3)] for column in range(3)]
        cipherMatrix = [[0 for row in range(3)] for column in range(3)]
        resMatrix = [[0 for row in range(3)] for column in range(3)]
        tmpres = [[0 for row in range(3)] for column in range(3)]
        res = []

        tmp = plain3[start_index:9]
        counter = 0
        for column in range(3):
            for row in range(3):
                plainMatrix[row][column] = tmp[counter]
                counter = counter+1

        tmp = cipher3[start_index:9]
        counter = 0
        for column in range(3):
            for row in range(3):
                cipherMatrix[row][column] = tmp[counter]
                counter = counter+1

        det =round((np.linalg.det(cipherMatrix)) %26, 0)

        if (det == 1):
            b = det
        else:
            c = 1/((26-det) % 26)
            if (c <1):
                i = 1
                while(c < 1):
                    c=(26*i +1)/((26-det) % 26)
                    i = i+1
            b = round((26- c),0)

        for row in range(3):
            for column in range(3):
                sign = math.pow((-1), (row+column))
                for row2 in range(3):
                    for column2 in range (3):
                        if (row2 != row) and (column2 != column):
                            tmp = cipherMatrix[row2][column2]
                resMatrix[column][row] =int(round(( b*sign* tmp % 26), 0))

        tmpres= np.matmul(plainMatrix, resMatrix) %26

        for row in range(3):
            for column in range(3):
                res.append(tmpres[row][column])

        if var_type is str:
            res = [chr(i+97) for i in res]
            res= ''.join(res)

        return res
        #raise NotImplementedError

