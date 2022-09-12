function solution(nums) {
  const canPeek = Math.floor(nums.length / 2)
  const items = new Set(nums)

  return Math.min(canPeek, [...items].length)
}
