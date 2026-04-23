# Largest number by Sampad Paul
from math import inf


def largest_num(nums):
    if len(nums) == 0:
        return "No numbers provided"
    largest = -inf
    for num in nums:
        if num > largest:
            largest = num
    return largest


nums = list(map(float, input("Enter numbers separated by space: ").split()))
print(largest_num(nums))
