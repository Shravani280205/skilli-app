def highestOccurringElement(nums):
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    highest = max(freq, key=freq.get)
    return highest
