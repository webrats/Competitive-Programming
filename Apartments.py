
'''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
'''
n, m, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = i = j = 0

while(i < n and j < m):
    if(a[i] < b[j]-k):
        i += 1
    elif(a[i] > b[j]+k):
        j += 1
    else:
        ans += 1
        i += 1
        j += 1


print(ans)
