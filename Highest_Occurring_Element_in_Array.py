# def highestOccurringElement(nums):
#     freq = {}

#     for n in nums:
#         freq[n] = freq.get(n, 0) + 1

#     highest = max(freq, key=freq.get)
#     return highest

def highestOccurringElement(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    highest = 0
    element = nums[0]

    for i in freq:
        if freq[i] > highest:
            highest = freq[i]
            element = i

    return element
