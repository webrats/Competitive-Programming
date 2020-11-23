for t in range(int(input())):
    a, b = map(int, input().split())
    print('YNEOS'[(a+b) % 3 > 0 or min(a, b) < abs(a-b)::2])
