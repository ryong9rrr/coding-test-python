# 인덱스를 이용한 스왑 // 160ms
def reverseString(self, s):
    for i in range(len(s)//2):
        s[i], s[-1-i] = s[-1-i], s[i]

# 투 포인터를 이용한 스왑 // 160ms
def reverseString(self, s):
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 리스트이기 때문에 reverse()함수 사용가능, 파이써닉한 방식 // 172ms
def reverseString(self, s):
    s.reverse()

"""js
// 투포인터 / 106ms
var reverseString = function(s) {
    let left = 0;
    let right = s.length - 1;
    
    while (left < right) {
        let temp = s[left]
        s[left] = s[right]
        s[right] = temp;
        left++;
        right--;
    }
};

// 배열 메서드 reverse() 사용 // 100ms
var reverseString = function(s) {
    s.reverse()
};
"""