
a = list(map(int, input().split(" ")))
best_max, so_far_max = 0, 0
for i in range(len(a)):
    so_far_max += a[i]
    best_max = max(best_max, so_far_max)
    if(so_far_max < 0):
        so_far_max = 0
print(best_max)
