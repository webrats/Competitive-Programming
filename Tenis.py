

a = 0
b = 0
t = 0
t1 = 0
t2 = 0
while(True):
    A = input()
    if(A == "A" or A == "B"):
        if(A == "A"):
            a += 1
            t1 += 1
            t2 = 0
        else:
            b += 1
            t2 += 1
            t1 = 0
        if(t == 0 and ((a == 4 and b <= 2) or (b == 4 and a <= 2))):
            if(a > b):
                print("Player A wins")
            else:
                print("Player B wins")
            break
        if((t2 or t1) and (t == 1) and ((a - b >= 2) or (b-a >= 2))):
            if(a > b):
                print("Player A wins")
            else:
                print("Player B wins")
            break
        if((a > 4 or b > 4) and a == b):
            t = 1

    else:
        print(">>> Invalid Input!!!")
