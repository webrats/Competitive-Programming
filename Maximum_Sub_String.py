s = input()
p = ""
t, ans = 0, 0
for i in s:
    if i == p:
        t += 1
        if(t > ans):
            ans = t

    else:
        p = i
        t = 0
print(ans+1)
