def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    q = len(nums) // 2
    left = nums[: q]
    right = nums[q :]

    leftSorted = mergeSort(left)
    rightSorted = mergeSort(right)
    outputs = merge(leftSorted, rightSorted)
    return outputs

def merge(nums1, nums2):

    outputs = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            outputs.append(nums1[i])
            i += 1
        else:
            outputs.append(nums2[j])
            j += 1

    while i < len(nums1):
        outputs.append(nums1[i])
        i += 1

    while j < len(nums2):
        outputs.append(nums2[j])
        j += 1

    return outputs


if __name__ == '__main__':
    print(mergeSort([3, 5, 1, 2, 0]))