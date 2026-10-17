def sumOfSeries(n: int, a: int, d: int) -> int:
    if n <= 0:
        return 0

    sum = 0
    for i in range(n):
        sum += a + i * d
    return sum
