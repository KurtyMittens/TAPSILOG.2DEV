class AlgorithmICE(object):
    def __init__(self):
        self.tabularecta = self.create_tabula_recta()
        self.z1a26 = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q"]
        self.key = ""
        self.pretext = ""
        self.posttext = ""

    def change_key(self, key):
        self.key = key

    def change_pretext(self, text):
        self.pretext = text

    def change_posttext(self, text):
        self.posttext = text

    def create_key(self):
        length = len(self.pretext)
        key = []
        key.append(self.pretext[length - 1])
        key.append(self.pretext[0])
        key.append(self.pretext[length - 2])
        key.append(self.pretext[1])
        finalkey = "".join(key)

        return finalkey

    def extract_key(self):
        entext = self.posttext
        length = len(entext)
        key = entext[length - 2] + entext[0] + entext[1] + entext[length - 1]
        new_text = ""
        for i in range(len(entext)):
            if i == 0 or i == 1 or i == length - 2 or i == length - 1:
                new_text = new_text + ""
            else:
                new_text = new_text + entext[i]

        self.change_posttext(new_text)

        return key

    def numToTextConvert(self, num):
        plaintext = str(num)
        separated = []
        digits = []
        for x in plaintext:
            if x.isnumeric() == True:
                digits.append(x)
            else:
                temp = "".join(digits)
                digits = []
                separated.append(temp)
                separated.append(x)
        temp = "".join(digits)
        separated.append(temp)

        final = []

        for pair in separated:
            if pair.isnumeric() == False:
                final.append(pair)
                continue
            else:
                nums = self.z1a26_encode(pair)
                az = self.encode(nums)
                final.append(az)

        return "".join(final)

    def textToNumConvert(self, num):
        plaintext = str(num)
        separated = []
        digits = []
        for x in plaintext:
            if x.isalpha() == True:
                digits.append(x)
            else:
                temp = "".join(digits)
                digits = []
                separated.append(temp)
                separated.append(x)
        temp = "".join(digits)
        separated.append(temp)

        final = []

        for pair in separated:
            if pair.isalnum() == False:
                final.append(pair)
                continue
            else:
                nums = self.decode(pair)
                az = self.z1a26_decode(nums)
                final.append(az)

        return "".join(final)

    def booleanEncode(self, boolean):
        if boolean == 0:
            boolean = "False"
            f = self.encode(boolean)
            return f
        elif boolean == 1:
            boolean = "True"
            t = self.encode(boolean)
            return t

    def booleanDecode(self, boolean):
        boolean = self.decode(boolean)
        if boolean == "TRUE":
            return 1
        elif boolean == "FALSE":
            return 0

    def z1a26_encode(self, plaintext):
        ciphertext = []
        plntext = [int(x) for x in str(plaintext)]
        for x in plntext:
            y = int(x)
            ciphertext.append(self.z1a26[y])
            continue
        temp = "".join(ciphertext)
        return temp

    def z1a26_decode(self, ciphertext):
        plaintext = []
        for x in ciphertext:
            for y in range(len(self.z1a26)):
                if x == self.z1a26[y]:
                    plaintext.append(str(y))
                    continue
        temp = "".join(plaintext)
        return temp

    def create_tabula_recta(self):
        tabularecta = []

        for r in range(0, 26):
            offset = 0
            row = []
            for column in range(0, 26):
                row.append(chr(r + 65 + offset))
                offset += 1
                if offset > (25 - r):
                    offset = offset - 26
                    tabularecta.append(row)

        return tabularecta

    def encrypt_checker(self):
        if len(self.pretext) < 4:
            return self.special_key()
        else:
            return self.create_key()

    def special_key(self):
        length = len(self.pretext)
        key = []
        if length == 1:
            key.append(self.pretext[0])
            key.append(self.pretext[0])
            key.append(self.pretext[0])
            key.append(self.pretext[0])
        elif length == 2:
            key.append(self.pretext[0])
            key.append(self.pretext[1])
            key.append(self.pretext[0])
            key.append(self.pretext[1])
        elif length == 3:
            key.append(self.pretext[1])
            key.append(self.pretext[2])
            key.append(self.pretext[1])
            key.append(self.pretext[0])
        finalkey = "".join(key)
        return finalkey

    def get_keyword_repeated(self, keyword, length):
        keyword = keyword.upper()
        keywordrepeated = []
        keywordlength = len(keyword)
        keywordindex = 0

        for i in range(0, length):
            keywordrepeated.append(keyword[keywordindex])
            keywordindex += 1
            if keywordindex > keywordlength - 1:
                keywordindex = 0

        return "".join(keywordrepeated)


class ICE(AlgorithmICE):
    def __init__(self):
        super().__init__()
            
    def encode(self, plaintext):
        self.change_pretext(plaintext)
        
        plaintext = str(plaintext)
        separated = []
        word = []
        nums = []
        for x in plaintext:
            if x.isalpha() == True and len(nums) == 0:
                word.append(x)
            elif x.isalpha() and len(nums) > 0:
                temp = "".join(nums)
                nums = []
                separated.append(temp)
                word.append(x)
            elif x == " ":
                if len(word) > 0:
                    temp = "".join(word)
                    word = []
                    separated.append(temp)
                if len(nums) > 0:
                    temp2 = "".join(nums)
                    nums = []
                    separated.append(temp2)
                separated.append(",")
            elif x.isnumeric() == True:
                if len(word) != 0:
                    temp = "".join(word)
                    word = []
                    separated.append(temp)
                nums.append(x)
            else:
                if len(word) > 0:
                    temp = "".join(word)
                    word = []
                    separated.append(temp)
                if len(nums) > 0:
                    temp2 = "".join(nums)
                    nums = []
                    separated.append(temp2)
                separated.append(x)
        if len(word) > 0:
            temp = "".join(word)
            word = []
            separated.append(temp)
        if len(nums) > 0:
            temp2 = "".join(nums)
            nums = []
            separated.append(temp2)
            
        #return separated        
        
        ciphertext = []
        
        for word in separated:
            if word.isnumeric() == True:
                numholder = []
                for x in word:
                    if x.isnumeric() == True:
                        temp = self.z1a26_encode(x)
                        numholder.append(temp)
                num = "".join(numholder)
                
                self.change_pretext(num)
                x = self.encrypt_checker()
                self.change_key(x)
                
                keywordrepeated = self.get_keyword_repeated(self.key, len(self.pretext))
                encrypt = []
                
                for index, letter in enumerate(num):
                    wordindex = ord(letter.upper()) - 65
                    keywordindex = ord(keywordrepeated[index]) - 65
                    encipheredletter = self.tabularecta[keywordindex][wordindex]
                    encrypt.append(encipheredletter)
                enword = "".join(encrypt)
                enkey = self.key.upper()
                final = "=" + enkey[1] + enkey[(len(enkey)-2)] + enword + enkey[0] + enkey[(len(enkey)-1)] + "="
                ciphertext.append(final)
             
            elif word.isalnum() == False:
                ciphertext.append(word)
                continue
            else:
                self.change_pretext(word)
                x = self.encrypt_checker()
                self.change_key(x)
                
                keywordrepeated = self.get_keyword_repeated(self.key, len(self.pretext))
                
                encrypt = []
                
                for index, letter in enumerate(word):
                    wordindex = ord(letter.upper()) - 65
                    keywordindex = ord(keywordrepeated[index]) - 65
                    encipheredletter = self.tabularecta[keywordindex][wordindex]
                    encrypt.append(encipheredletter)
                enword = "".join(encrypt)
                enkey = self.key.upper()
                final = enkey[1] + enkey[(len(enkey)-2)] + enword + enkey[0] + enkey[(len(enkey)-1)]
                ciphertext.append(final)
        
        return "".join(ciphertext)
    
    def decode(self, text):
        self.change_posttext(text)
        
        text = str(text)
        num = 0
        separated = []
        word = []
        nums = []
        for x in text:
            if x.isalpha() == True and num == 0:
                word.append(x)
            elif x.isalpha() and num == 1:
                nums.append(x)
            elif x == ",":
                if len(word) > 0:
                    temp = "".join(word)
                    word = []
                    separated.append(temp)
                if len(nums) > 0:
                    temp2 = "".join(nums)
                    nums = []
                    separated.append(temp2)
                separated.append(" ")
            elif x == "=" and num == 0:
                if len(word) != 0:
                    temp = "".join(word)
                    word = []
                    separated.append(temp)
                nums.append(x)
                num += 1
            elif x == "=" and num == 1:
                nums.append(x)
                temp = "".join(nums)
                nums = []
                separated.append(temp)
                num -= 1
            else:
                if len(word) > 0:
                    temp = "".join(word)
                    word = []
                    separated.append(temp)
                separated.append(x)
        if len(word) > 0:
            temp = "".join(word)
            word = []
            separated.append(temp)
        
        #return separated
        
        plaintext = []
        
        for word in separated:
            if word[0] == "=" and word[len(word) - 1] == "=":
                new_text = ""
                for i in range(len(word)):
                    if i == 0 or i == len(word)-1:
                        new_text = new_text + ""
                    else:
                        new_text = new_text + word[i]
                
                self.change_posttext(new_text)
                x = self.extract_key()
                self.change_key(x)
                
                keywordrepeated = self.get_keyword_repeated(self.key, len(self.posttext))
                
                decrypt = []
                final_word = []
                
                for index, letter in enumerate(self.posttext):
                    keywordindex = ord(keywordrepeated[index]) - 65
                    decipheredletter = chr(self.tabularecta[keywordindex].index(letter) + 65)                    
                    decrypt.append(decipheredletter)
                enword = "".join(decrypt)
                for x in enword:
                    temp = self.z1a26_decode(x)
                    final_word.append(temp)
                temp2 = "".join(final_word)
                plaintext.append(temp2)
                
            elif word.isalpha() == False:
                plaintext.append(word)
                continue
            
            else:
                self.change_posttext(word)
                x = self.extract_key()
                self.change_key(x)
                
                keywordrepeated = self.get_keyword_repeated(self.key, len(text))
                
                decrypt = []
                
                for index, letter in enumerate(self.posttext):
                    keywordindex = ord(keywordrepeated[index]) - 65
                    decipheredletter = chr(self.tabularecta[keywordindex].index(letter) + 65)                    
                    decrypt.append(decipheredletter)
                enword = "".join(decrypt)
                plaintext.append(enword)
        
        return "".join(plaintext)

a = ICE()
