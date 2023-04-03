# 내가 푼 풀이 : O(N^3), 63ms(58%)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) + 1 - i):
                ans += sum(arr[j:i + j])
        return ans
    
# 리트코드 해설 (1) 3중 브루트포스 : O(N^3), 147ms(10%)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                if (j - i + 1) % 2 == 1:
                    acc = 0
                    for k in range(i, j + 1):
                        acc += arr[k]
                    ans += acc
        
        return ans
    
# 리트코드 해설 (2) 2중 브루트포스 : O(N^2), 52ms(72%)
# 어려운 아이디어..
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            acc = 0
            for j in range(i, n):
                acc += arr[j]
                ans += acc if (j - i + 1) % 2 == 1 else 0
        
        return ans
    

# 리트코드 해설 (3) 1중 브루트포스 : O(N), 30ms(90%)
# 매우매우매우 어려운 아이디어... 이 문제는 Easy로 되어있는데 난이도가 더 높아져야할듯..
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for index in range(n):
            left, right = index, n - index - 1
            num = arr[index]
            
            ans += num * (left // 2 + 1) * (right // 2 + 1)
            ans += num * ((left + 1) // 2) * ((right + 1) // 2)
        
        return ans