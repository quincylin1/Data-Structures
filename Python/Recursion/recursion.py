
def sum(nums):
    if len(nums) == 0:
        return 0
    
    num = nums.pop()
    total = sum(nums) + num
    return total

def sumList(nums):
    total = 0
    for element in nums:
        if isinstance(element, list):
            total += sumList(element)
        else:
            total += element
    return total 

def sumDigits(num):
    if num == 0:
        return 0
    return num % 10 + sumDigits(num // 10)

def findHCF(a, b):
    if b == 0:
        return a
    return findHCF(b, a%b)
    

if __name__ == '__main__':
    nums = [1, 2, [3, 4], [5, 6, 7]]
    num1 = 48
    num2 = 60
    print(findHCF(num1, num2))
    