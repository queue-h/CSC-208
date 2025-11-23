from datetime import datetime
import numpy as np

def linear_min(nums):
    start = datetime.now()
    min = nums[0]
    for num in nums:
        if num < min:
            min = num
    end = datetime.now()
    return f"Minimum = {min}\nNumber of Seconds = {(end-start).total_seconds()}"

def exponential_min(nums):
    start = datetime.now()
    for index1 in range(len(nums)):
        for index2 in range(index1):
            if nums[index1] < nums[index2]:
                min = nums[index1]
            else:
                min = nums[index2]
    end = datetime.now()
    return f"Minimum = {min}\nNumber of Seconds = {(end-start).total_seconds()}"

nums = np.random.uniform(low=-1000, high=1000, size=10000)
print(linear_min(nums))
print(exponential_min(nums))