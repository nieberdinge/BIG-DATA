import random
file = open('rollsim.txt','a')
for x in range(0,10000):
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    r3 = random.randint(1,6)
    file.write(str(r1) + "," + str(r2) + "," + str(r3) + "Roll  number: " +x +"\n")
    
file.close
