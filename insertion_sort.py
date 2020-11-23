

def insertion_sort(a, n):
    global count
    for i in range(1, n):
        key = a[i]
        j = i-1
        while(j >= 0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
            count += 1
        a[j+1] = key


count = 0
a = [8, 3, 8, 7, 3, 1, 65, 4, 23, 45]

insertion_sort(a, len(a))
print(a, count)

# Time Complexity = Avg, Worst O(n**2) best(Already sorted) O(n)
# Uses - best for Small array , Almost sorted few element is misplace

'''


'''
