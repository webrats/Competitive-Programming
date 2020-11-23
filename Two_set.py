n = int(input())

f = int((n*(n+1))/2)
list1, list2 = [], []

l1, l2, c1, c2 = 0, 0, 0, 0
if(f % 2 == 0):
    for i in range(n, 0, -1):
        if(l1+i <= (f/2)):
            l1 += i
            list1.append(i)
            c1 += 1
        else:
            l2 += i
            c2 += 1
            list2.append(i)
    print("YES")
    print(c1)
    print(*list1)
    print(c2)
    print(*list2)
else:
    print("NO")
