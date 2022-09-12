# 첫번째 풀이
def solution(nums):
    pick = len(nums) // 2
    nums = set(nums)
    if pick <= len(nums):
        return pick
    else:
        return len(nums)

# 두번째 풀이
def solution(nums):
    canPeek = len(nums) // 2
    items = set(nums)
    
    return canPeek if len(items) > canPeek else len(items)

# 세번째 풀이
def solution(nums):
    kinds = len(set(nums))
    result = len(nums) // 2

    return min(kinds, result)