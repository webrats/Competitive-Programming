
a = int(input())


if(a > 1):
    while(a != 1):
        print(a, end=" ")
        if(a % 2 == 0):
            a = int(a/2)
        else:
            a = (a*3)+1
    print(a, end=" ")
else:
    print(a)
