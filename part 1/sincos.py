import math
def sinTaylor(x):
    #x = x / 180 * math.pi
    n = 0
    sum = 0
    while (x**n) / math.factorial(n) != 0:
        term = ((-1)**n) / math.factorial(2*n+1) * (x**(2*n+1)) 
        sum = sum + term
        n += 1
    return sum

def cosTaylor(x):
    n = 0
    sum = 0
    while (x ** n) / math.factorial(n) != 0:
        sum = sum + ((-1) ** n) / math.factorial(2 * n) * (x ** (2 * n))
        n += 1
    print(sum)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def taylor_sine(x):
    sine = 0
    n = 0
    term = x  # the first term in the series is x
    while term != 0:
        term = (-1)**n / math.factorial(2*n + 1) * x**(2*n + 1)
        sine += term
        n += 1
    return sine

print(taylor_sine(0.9685222523158571))