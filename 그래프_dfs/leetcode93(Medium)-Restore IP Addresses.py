# 38ms(63.98%), 13.8MB(74.89%)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s.isdigit():
            return []
        
        result = []

        def dfs(index, array):
            if not 0 <= int(array[-1]) <= 255 or len(array) > 4:
                return
            
            if index >= len(s):
                if len(array) == 4:
                    for item in array:
                        if len(item) > 1 and item[0] == "0":
                            return
                    result.append(".".join(array))
                return
            
            case1 = array[:]
            case1.append(s[index])

            case2 = array[:]
            case2[-1] += s[index]

            dfs(index + 1, case1)
            dfs(index + 1, case2)


        dfs(1, [s[0]])

        return result
    
# 조금 더 나아보이는 방법 : 55ms(21.4%), 13.9MB(74.89%)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def is_valid(string):
            if not string.isdigit() or int(string) > 255:
                return False
            if len(string) > 1 and string[0] == "0":
                return False
            return True

        def dfs(string, array):
            if len(array) == 3:
                if is_valid(string):
                    result.append(".".join(array + [string]))
                return
            
            for i in range(1, 4):
                substr = string[:i]
                if is_valid(substr):
                    dfs(string[i:], array + [substr])
        
        dfs(s, [])

        return result