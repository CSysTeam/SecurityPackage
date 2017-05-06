class RC4:
    def Encrypt(self, plainText, key):
        #raise NotImplementedError
        K = key
        T = ""
        S = [0 for n in range(256)]
        pi =[0 for n in range(len(plaintext))]
        k =[0 for n in range(len(plaintext))]
        cipher = ""

        for letter in range (len(plaintext)):
            pi[letter] = ord(plaintext[letter])

        for index in range(256):
            S[index] = index

        T = K
        if len(T) < 256:
            loops = 256 - len(T)
            tmp = 0
            for loop in range(loops):
                T += K[tmp]
                tmp += 1
                if tmp == 4:
                    tmp = 0


        j=0
        for i in range(256):
            j = (j + S[i] + ord(T[i])) % 256
            S[i] , S[j] = S[j] , S[i]

        i = 0
        j = 0

        for n in range(len(plaintext)):
            i = (i+1) % 256
            j = (j + S[i]) % 256
            S[i] , S[j] = S[j] , S[i]
            t = (S[i] + S[j]) % 256
            k = S[t]
            cipher += chr((pi[n] ^ k))

        return cipher



    def Decrypt(self, cipherText, key):
        K = key
        T = ""
        S = [0 for n in range(256)]
        ci =[0 for n in range(len(cipherText))]
        k =[0 for n in range(len(cipherText))]
        plain = ""

        for letter in range (len(cipherText)):
            ci[letter] = ord(cipherText[letter])

        for index in range(256):
            S[index] = index

        T = K
        if len(T) < 256:
            loops = 256 - len(T)
            tmp = 0
            for loop in range(loops):
                T += K[tmp]
                tmp += 1
                if tmp == 4:
                    tmp = 0


        j=0
        for i in range(256):
            j = (j + S[i] + ord(T[i])) % 256
            S[i] , S[j] = S[j] , S[i]

        i = 0
        j = 0

        for n in range(len(cipherText)):
            i = (i+1) % 256
            j = (j + S[i]) % 256
            S[i] , S[j] = S[j] , S[i]
            t = (S[i] + S[j]) % 256
            k = S[t]
            plain += chr((ci[n] ^ k))

        return plain
