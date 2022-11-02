class Toekum:

    def __init__(self,input):
        self.lst=input.split(",")
        self.nowText,self.oldText,self.command="","",""
        self.lstword=[]

    def __run__(self):
        for i in self.lst : 
            if i =="R":
                self.lstword.clear()
                print("game restarted")
            elif i =="X": break
            else :
                self.command,self.nowText=i.split(" ")
                if self.command=="P": 
                    print("'"+str(self.nowText)+"' -> ",end="")
                    if self.lstword==[] or (self.oldText[-1].lower()==self.nowText[1].lower() and self.nowText[0].lower()==self.oldText[-2].lower()):
                        self.lstword.append(self.nowText)
                        print(str(self.lstword))
                    else:print("game over")
                else:
                    print("'"+str(self.command),str(self.nowText)+"' is Invalid Input !!!",end="")
                    break
                self.oldText=self.nowText

text=input("*** TorKham HanSaa ***\nEnter Input : ")
A=Toekum(text)           
A.__run__()
