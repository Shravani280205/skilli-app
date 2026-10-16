def subtractProductAndSum(n: int) -> int:
    sum = 0
    mul = 1
    if n == 0:
        return 0

    for ch in str(n):
        num = int(ch)
        sum += num
        mul *= num
    return mul - sum
