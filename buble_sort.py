def buble_sort(a, n):
    for i in range(n):
        global count
        Swap = False
        for j in range(0, n-i-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                Swap = True
                count += 1

        if(not Swap):
            break


count = 0
a = [8, 3, 8, 7, 3, 1, 65, 4, 23, 45]

k = len(a)
buble_sort(a, k)
print(a, count)

# time Complexity best , avg , worst  case is O(n**2)
# Total number of swaping  is higher
# Uses - Stable  , easy to implement
