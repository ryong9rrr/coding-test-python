# num의 길이는 최대 1000
# 파이썬은 매우 큰 수도 처리가능 : 309ms(76.40%), 15MB(65.15%)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = int("".join(map(str, num)))

        return map(int, str(number + k))
    
# 길이가 최대 1000일 수 있는 문자열을 바로 숫자로 바꿔버리면 오버플로우가 일어난다(파이썬 제외)
# 따라서 수학적으로, 매우 교과서적인 방법(Schoolbook)으로 덧셈을 한다.
# k의 최대 크기가 1000이므로 항상 1000 + 한자리의 숫자의 연산만 하게 된다.
# 240ms(99.94%), 15.1MB(65.15%)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i], 10)
            if k == 0:
                break
            if i > 0:
                num[i - 1] += k
        
        if k > 0:
            num = list(map(int, str(k))) + num

        return num