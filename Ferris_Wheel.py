'''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
'''
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 0
j = n-1
ans = 0
while(i <= j):
    if(a[j] + a[i] <= x):
        i += 1
    j += 1
    ans += 1


print(ans)
