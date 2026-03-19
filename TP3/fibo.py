import time

def fibonacci1(n):
    if n < 2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)


def fibonacci2(n, F):
    if F[n] != -1:
        return F[n]
    if n < 2:
        F[n] = 1
        return 1
    r = fibonacci2(n-1, F) + fibonacci2(n-2, F)
    F[n] = r
    return r

def fibonacci3(a, b, n):
    if n == 0:
        return b
    new_a = a + b
    new_b = a
    return fibonacci3(new_a, new_b, n-1)


print(fibonacci3(1,1, 10))