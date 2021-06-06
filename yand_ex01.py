def ex01():
    datat = raw_input()
    temp = datat.split(' ')
    datam = raw_input()
    troom = int(temp[0])
    tcond = int(temp[1])
    mode = datam
    t_exit = troom
    if (tcond < troom) and (mode == "auto" or mode == "freeze"):
        t_exit = tcond
    elif (tcond > troom) and (mode == "auto" or mode == "heat"):
        t_exit = tcond
    print(str(t_exit))

def ex02():
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (b + c > a) and (c + a > b):
        print("YES")
    else:
        print("NO")

def ex03():
    a = [""] * 4
    for i in range(4):
        a[i] = raw_input()

    for i in range(4):
        a[i] = a[i].replace("+7", "8")
        a[i] = a[i].replace("-", "")
        a[i] = a[i].replace("(", "")
        a[i] = a[i].replace(")", "")
        if len(a[i]) == 7:
            a[i] = "8495" + a[i]
    for i in range(3):
        if (a[0] == a[i + 1]):
            print ("YES")
        else:
            print ("NO")

def ex04():
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    if a == 0 and b == c ** 2 and c >= 0:
        print ("MANY SOLUTIONS")
    elif a == 0 or c < 0:
        print ("NO SOLUTION")
    else:
        x = (c ** 2 - b) / a
        if (c ** 2 - b) % a == 0:
            print (str(x))
        else:
            print ("NO SOLUTION")

def ex05():
    data = raw_input().split(' ')
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])
    maxs = 1000 * 1000 * 2
    mina = 0
    minb = 0
    if (max(max(a, b), max(c, d)) * (min(a, b) + min(c, d))) < maxs:
        maxs = max(max(a, b), max(c, d)) * (min(a, b) + min(c, d))
        mina = max(max(a, b), max(c, d))
        minb = min(a, b) + min(c, d)
    if (max(max(a, b), min(c, d)) * (min(a, b) + max(c, d))) < maxs:
        maxs = max(max(a, b), min(c, d)) * (min(a, b) + max(c, d))
        mina = max(max(a, b), min(c, d))
        minb = min(a, b) + max(c, d)
    if ((max(a, b) + min(c, d)) * max(min(a, b), max(c, d))) < maxs:
        maxs = (max(a, b) + min(c, d)) * max(min(a, b), max(c, d))
        mina = max(a, b) + min(c, d)
        minb = max(min(a, b), max(c, d))
    print mina, minb

def ex06():
    data = raw_input().split(' ')
    n = int(data[0])
    k = int(data[1])
    m = int(data[2])
    zag = 0
    det = 0
    while n >= k and k >= m:
        n = n - k
        zag += 1
        if n < k:
            det += zag * (k / m)
            n += zag * (k % m)
            zag = 0
    print det

def ex07():
    a = int(raw_input())
    b = int(raw_input())
    f = int(raw_input())
    c = int(raw_input())
    d = int(raw_input())
    if a > max(b, f):
        a = f
    elif b > max(a, f):
        b = f
    if (a <= c and b <= d) or (a <= d and b <= c):
        print "YES"
    else:
        print "NO"