

from itertools import *
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def minsum(nums, totalsum, currsum, i):
    if i == 0:
        return abs(totalsum-2*currsum)
    else:
        return min(minsum(nums, tostalsum, currsum+nums[i], i-1), minsum(nums, totalsum, currsum, i-1))


n = int(input())
nums = list(map(int, input().split()))
s = sum(nums)
print(minsum(nums, s, 0, n-1))
