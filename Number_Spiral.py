t = int(input())
while(t != 0):
    t -= 1
    r, c = map(int, input().split(" "))
    if(r == c):
        print((r*r)-(r-1))
    elif(r > c):
        if(r % 2 == 1):
            print(((r-1)*(r-1))+c)
        else:
            print((r*r)-(c-1))
    else:
        if(c % 2 == 0):
            print((c-1)*(c-1)+r)
        else:
            print((c*c)-(r-1))
