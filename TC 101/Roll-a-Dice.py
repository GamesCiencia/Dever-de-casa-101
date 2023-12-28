import random


print("Quer jogar? 1 para sim e 0 para não")
yOrN = int(input()) 

if(yOrN == 1):
    print("sim")

    no = random.randint(1,6)
    print(no)

    if(no == 1):
        print("[1----]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[----1]")

    if(no == 2):
        print("[2----]")
        print("[     ]")
        print("[ * * ]")
        print("[     ]")
        print("[----2]")

    if(no == 1):
        print("[3----]")
        print("[     ]")
        print("[* * *]")
        print("[     ]")
        print("[----3]")

    if(no == 4):
        print("[4----]")
        print("[ * * ]")
        print("[     ]")
        print("[ * * ]")
        print("[----4]")

    if(no == 5):
        print("[5----]")
        print("[ * * ]")
        print("[  *  ]")
        print("[ * * ]")
        print("[----5]")

    if(no == 6):
        print("[6----]")
        print("[* * *]")
        print("[     ]")
        print("[* * *]")
        print("[----6]")
        
else:
    print("não")