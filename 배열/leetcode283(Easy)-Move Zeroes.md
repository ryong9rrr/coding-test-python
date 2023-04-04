# 접근 1 : O(N^2) 스왑

- 시간복잡도 : O(N^2)
- 공간복잡도 : O(1)

가장 직관적인 방법...

## python

8777ms(5.2%), 15.5MB(51%)

```python
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        cur = set()
        for char in s:
            if char in cur:
                cur = set()
                ans += 1
            cur.add(char)

        if cur:
            ans += 1

        return ans
```

# 접근 2 : 그냥 새로운 배열을 하나 만들기

> 리트코드 풀이 1

- 시간복잡도 : O(N)
- 공간복잡도 : O(N)

## python

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        num_zeros = nums.count(0)
        ans = [num for num in nums if num != 0] + [0] * num_zeros

        for i in range(n):
            nums[i] = ans[i]
```

# 접근 3 : 접근 2 방법의 공간복잡도 최적화

> 리트코드 풀이 2

- 시간복잡도 : O(N)
- 공간복잡도 : O(1)

## python

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        last_non_zero_index = 0

        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        for i in range(last_non_zero_index, n):
            nums[i] = 0
```

## js

```js
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  const n = nums.length
  let lastNonZeroIndex = 0

  for (let i = 0; i < n; i += 1) {
    if (nums[i] !== 0) {
      nums[lastNonZeroIndex] = nums[i]
      lastNonZeroIndex += 1
    }
  }

  for (let i = lastNonZeroIndex; i < n; i += 1) {
    nums[i] = 0
  }
}
```
