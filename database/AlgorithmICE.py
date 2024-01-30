import re


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
        key.append(self.pretext[length-1])
        key.append(self.pretext[0])
        key.append(self.pretext[length - 2])
        key.append(self.pretext[1])
        finalkey = "".join(key)
        
        return finalkey    

    def extract_key(self):
        entext = self.posttext
        length = len(entext)
        key = entext[length-2] + entext[0] + entext[1] + entext[length-1]
        new_text = ""
        for i in range(len(entext)):
            if i == 0 or i == 1 or i == length-2 or i == length-1:
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
        
            