def g(b, n, d):
    mysum = 1
    for i in range(1, d + 1):
        mysum += b ** i
    return mysum - (n + 1)


def dg(b, d):
    mysum = 1
    for i in range(1, d):
        mysum += (i + 1) * b ** i
    return mysum


def newton(b0, g, dg, nc, d):
    b = [b0]
    for n in range(0, 10):
        b.append(b[n] - g(b[n], nc, d) / dg(b[n], d))
    return b
