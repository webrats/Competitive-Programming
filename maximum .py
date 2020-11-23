
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -99999999
for i in range(n):
    for j in range(i+1, n):
        res = a[j] - a[i]
        if(res > max):
            max = res

if(max > 0):
    print(max)
else:
    print(-1)
