# 투 포인터 + 슬라이딩 윈도우 // 232ms
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left, right) :
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # s[1:1] = ""을 리턴함(에러 X)
            return s[left+1 : right]
        
        # 2글자보다 작거나 그 자체가 팰린드롬이면 바로 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ""
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            
        return result

"""js
/**
 * @param {string} s
 * @return {string}
 */

function max(...args){
    return args.sort((a, b) => b.length - a.length)[0];
}

var longestPalindrome = function(s) {
    
    if (s.length < 2 || s === [...s].reverse().join("")) return s
    
    function expand(left, right){
        while (left >= 0 && right < s.length && s[left] == s[right]){
            left--;
            right++;
        }
        return s.slice(left + 1, right)
    }
    
    let result = "";
    
    for(let i = 0; i < s.length - 1; i++){
        result = max(result, expand(i, i + 1), expand(i, i + 2));
    }
    return result
    
};
"""