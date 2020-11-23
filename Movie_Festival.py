
from sys import stdin, stdout
'''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
'''

n = int(input())
ls = [[int(i) for i in stdin.readline().split()] for j in range(n)]

ls.sort(key=lambda x: x[1])


current_end = ls[0][1]
movie = 1

for start, end in ls:
    if(current_end <= start):
        movie += 1
        current_end = end

print(movie)
