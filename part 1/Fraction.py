import math
numerator = int(input())
denominator = int(input())

def is_minimalist_fraction(numarator, denominator):
    return True if math.gcd(numarator, denominator) == 1 else False

def get_minimalist_fraction(numerator, denominator):
    if is_minimalist_fraction(numerator, denominator):
        return numerator, denominator
    gcd = math.gcd(numerator, denominator)
    return int(numerator / gcd), int(denominator / gcd)

print(get_minimalist_fraction(numerator, denominator))