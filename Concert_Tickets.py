
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
i = j = 0
while(j < m):
    if(i < n and a[i] <= b[j]):
        print(a[i])
        i += 1
    else:
        print("-1")
    j += 1
