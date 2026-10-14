#  Sum of Array Elements

def Sum_of_Array_Element(n, arr):
    total = 0
    for i in range(n):
        total += arr[i]
    return total

#  Reverse Array

def ReverseArray(arr):
    return arr[::-1]

# Checked array is sorted or not

def isArraySorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True