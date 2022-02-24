def findPair(nums, target):
    for i in range(len(nums)):
        remainder = target - nums[i]
        for j in range(i, len(nums)):
            if remainder - nums[j] == 0:
                return (nums[i], nums[j])

    return []

def findPairBS(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low < high:
        if nums[low] + nums[high] == target:
            return (nums[low], nums[high])

        elif nums[low] + nums[high] < target:
            low += 1

        elif nums[low] + nums[high] > target:
            high -= 1

    return []

def findPairDict(nums, target):
    d = {}

    for i, e in enumerate(nums):
        if target - e in d:
            return (nums[d.get(target - e)], nums[i])
        d[e] = i

    return []
if __name__ == '__main__':
    print(findPairDict([8, 7, 2, 5, 3, 1], 10))

