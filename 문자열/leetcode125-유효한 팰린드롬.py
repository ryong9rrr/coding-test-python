# 44ms, 리스트 사용
def isPalindrome(self, s):
    strs = [] 
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    return strs == strs[::-1]

# 20ms, 정규표현식 사용
def isPalindrome(self, s):
    s = s.lower()
    # regex에 포함되지 않으면 제거하겠다. (^ 은 not 을 의미)
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]

"""js // 106ms

var isPalindrome = function(s) {
    const reg = /[^a-zA-Z0-9]/g
    
    s = s.replace(reg, "").toLowerCase()
    
    // reverse() 메서드는 문자열에 사용할 수 없다.
    return s === [...s].reverse().join("")
};
"""