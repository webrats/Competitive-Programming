s = input()
h = o = ''
for i in set(s):
    c = s.count(i)
    h = h + i * (c//2)
    o = o + (i * (c % 2))
print(len(o) < 2 and h+o+h[::-1] or "NO SOLUTION")
