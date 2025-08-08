"""

Problem: 1. Two Sum
Difficulty: Easy


Approach:
1. Created a Hash map to keep track of numbers we have seen
2. for each number, we check if its complement(target - num) is in the map
3. if yes, we return the indices

"""

def TwoSums(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i