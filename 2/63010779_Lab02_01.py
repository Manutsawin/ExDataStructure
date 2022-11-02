class translator:

    def __init__(self):
            self.lstnum=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
            self.lstchar=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    def deciToRoman(self, num):
        str1=""
        index=0
        while num>0:
            if num>=self.lstnum[index]: 
                num-=self.lstnum[index]
                str1=str1+self.lstchar[index]
            elif index < 12: index+=1
        return str1

    def romanToDeci(self, s):
        num=0
        k=0
        for i in range(len(s)) : 
            if(k==1):
                k=0
                continue 
            for loop in range(13):
                if i+1<len(s):
                    if  s[i]+s[i+1] == self.lstchar[loop]:
                        num+=self.lstnum[loop]
                        k=1
                        break
                if s[i] == self.lstchar[loop] :   
                    num+=self.lstnum[loop] 
                    break
        return num

num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))