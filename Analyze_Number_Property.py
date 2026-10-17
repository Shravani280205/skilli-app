from math import isqrt

def analyzeNumber(n: int) -> dict:
    is_prime = n > 1
    if is_prime:
        for i in range(2, isqrt(n)+1):
            if n % i == 0:
                is_prime = False
                break
    result = {
        "is_even" : n % 2 == 0,
        "is_positive" : n > 0,
        "is_prime" : is_prime,
        "is_perfect_square" : n >= 0 and isqrt(n) ** 2 == n,
        "digit_count" : len(str(abs(n)))
    }

    return result
