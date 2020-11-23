

n = int(input())

a = list(map(int, input().split(" ")))

tsum = int((n*(n+1))/2)

print(tsum - sum(a))
