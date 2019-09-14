import random
def krypto():
    for i in range (5):
        a = random.randint(0,10)
        b = random.randint(0,10)
        c = random.randint(0,10)
        d = random.randint(11,17)
        e = random.randint(11,17)
        f = random.randint(18,25)
        rndNmbr = random.randint(1,6)
        if(rndNmbr == 1):
            print(a, end = ' ')
        if(rndNmbr == 2):
            print(b, end = ' ')
        if(rndNmbr == 3):
            print(c, end = ' ')
        if(rndNmbr == 4):
            print(d, end = ' ')
        if(rndNmbr == 5):
            print(e, end = ' ')
        if(rndNmbr == 6):
            print(f, end = ' ')
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = random.randint(0,10)
    d = random.randint(11,17)
    e = random.randint(11,17)
    f = random.randint(18,25)
    rndNmbr = random.randint(1,6)
    if(rndNmbr == 1):
        print('Target Number: ', a)
    if(rndNmbr == 2):
        print('Target Number: ', b)
    if(rndNmbr == 3):
        print('Target Number: ', c)
    if(rndNmbr == 4):
        print('Target Number: ', d)
    if(rndNmbr == 5):
        print('Target Number: ', e)
    if(rndNmbr == 6):
        print('Target Number: ', f)

krypto()
