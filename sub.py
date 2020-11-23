
def subSeq(arr, n, k):
    mod = []
    for i in range(k + 1):
        mod.append(0)

    cumSum = 0
    for i in range(n):
        cumSum = cumSum + arr[i]
        mod[((cumSum % k)+k) % k] = mod[((cumSum % k)+k) % k] + 1

    result = 0

    for i in range(k):
        if (mod[i] > 1):
            result = result + (mod[i]*(mod[i]-1))//2

    result = result + mod[0]

    return result


t = int(input())
for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int, input().split()))
    print(subSeq(arr, n, k))
