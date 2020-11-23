n = int(input())
i, count = 5, 0
while(n/i >= 1):
    count += n//i
    i *= 5
print(count)
