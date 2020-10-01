c = []
t = int(input())
for i in range(t):
    c.append(0)
    a = int(input(""), 2)
    b = int(input(""), 2)
    d = 0
    while b > 0:
        y = (a & b)
        a = (a ^ b)
        d += 1
        b = (y*2)
    c[i] = d
for i in range(t):
    print(c[i])
