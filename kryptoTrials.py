import random
def krypto():
    for i in range (5):
        a = random.randint(0,10)
        b = random.randint(11,17)
        c = random.randint(18,25)
        rndNmbr = random.randint(1,6)
        if(rndNmbr == 1):
            print(a, end = ' ')
        if(rndNmbr == 2):
            print(a, end = ' ')
        if(rndNmbr == 3):
            print(a, end = ' ')
        if(rndNmbr == 4):
            print(b, end = ' ')
        if(rndNmbr == 5):
            print(b, end = ' ')
        if(rndNmbr == 6):
            print(c, end = ' ')
    d = random.randint(0,10)
    e = random.randint(11,17)
    f = random.randint(18,25)
    rndNmbr = random.randint(1,6)
    if(rndNmbr == 1):
        print('Target Number: ', d)
    if(rndNmbr == 2):
        print('Target Number: ', d)
    if(rndNmbr == 3):
        print('Target Number: ', d)
    if(rndNmbr == 4):
        print('Target Number: ', e)
    if(rndNmbr == 5):
        print('Target Number: ', e)
    if(rndNmbr == 6):
        print('Target Number: ', f)
    numTries = 10
    counter = 0
    while(counter < numTries):
        guess = input()
        if ()

krypto()
