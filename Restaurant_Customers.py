
from sys import stdin, stdout


n = int(stdin.readline())
arr = []
leav = []
for i in range(n):
    a, b = map(int, stdin.readline().split())
    arr.append(a)
    leav.append(b)

arr.sort()
leav.sort()

i = j = 0
cus = mx = 0
while(i < n and j < n):
    if (arr[i] < leav[j]):
        cus += 1
        i += 1
    else:
        cus -= 1
        j += 1
    if(mx < cus):
        mx = cus
print(mx)
