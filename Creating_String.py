from itertools import permutations

l = [''.join(i) for i in set(permutations(input()))]
print(len(l), *sorted(l))
