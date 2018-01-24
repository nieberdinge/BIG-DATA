import random
file = open('rollsim.txt','r')
total = 0
doublet = 0
for x in range(0,10000):
    str = file.readline()
    if(str[0] == str[3] and str [0] == str[6]):
        total +=1
        print("I found a double at: " , x)
        print("The triple total is: " , total)
    elif(str[0] == str[3] or str[0] == str[6] or str[6] == str[3]):
        doublet +=1
        print("I found a double at: " , x)
        print("The double total is: " , doublet)
print("the total double is: " , doublet ,"The total triple is: " , total)
file.close
