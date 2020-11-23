'''

from sys import stdin, stdout

'''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, x = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
f = 0
r = n-1
l = 0
while(l <= r):
    if(a[l]+a[r] < x):
        l += 1
    elif(a[l]+a[r] > x):
        r -= 1
    else:
        print(l+1, r+1)
        f = 1

if(f == 0):
    print('IMPOSSIBLE')
