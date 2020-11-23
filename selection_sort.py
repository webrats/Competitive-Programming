def selection(a, n):
    min_index = 0
    for i in range(n):
        global count
        min_index = i
        for j in range(i, n):
            if(a[min_index] > a[j]):
                min_index = j
        a[min_index], a[i] = a[i], a[min_index]
        count += 1


a = [8, 3, 8, 7, 3, 1, 65, 4, 23, 45]

count = 0
n = len(a)
selection(a, n)
print(a, count)

# time complexity O(n**2)
# n number of swap only need
# inplace sort no extra memory
# default implimentation is not stable but can be stable
