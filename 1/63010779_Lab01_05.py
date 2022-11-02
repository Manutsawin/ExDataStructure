num =[int(e)for e in input("Enter All Bid : ").split()]
max_num = max(num)
if len(num)<2:print("not enough bidder")
elif num.count(max_num)>1:print("error : have more than one highest bid")
else: 
    num.remove(max_num)
    print("winner bid is "+str(max_num)+" need to pay "+str(max(num)))