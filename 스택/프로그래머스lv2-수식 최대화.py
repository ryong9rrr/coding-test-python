from collections import deque
import itertools

def oper(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b

def precs():
    precs = list(itertools.permutations(['*', '+', '-']))
    array = []
    for a, b, c in precs:
        array.append({a: 1, b: 2, c: 3})
    return array

def split_expression(strings):
    array = ['']
    for char in list(strings):
        if not char.isdigit():
            array.append(char)
            array.append('')
            continue
        array[-1] += char
    return array

def operate(exp_array, prec):
    numbers = deque()
    ops = deque()
    for char in exp_array:
        # 일단 숫자면 푸시
        if char.isdigit():
            numbers.append(int(char))
        else:
            #숫자가 아니면 우선순위 비교
            #ops가 비어있으면 그냥 푸시
            if not ops:
                ops.append(char)
            else:
                #ops가 있으면 우선순위 비교
                #먼저들어간게 우선순위가 같거나 높으면 연산
                while numbers and ops and prec[char] <= prec[ops[-1]]:
                    b, a = numbers.pop(), numbers.pop()
                    op = ops.pop()
                    numbers.append(oper(a, b, op))
                ops.append(char)

    while numbers and ops:
        b, a = numbers.pop(), numbers.pop()
        op = ops.pop()
        numbers.append(oper(a, b, op))

    return numbers[0]


def solution(expression):
    exp_array = split_expression(expression)

    result = 0
    for prec in precs():
        answer = operate(exp_array, prec)
        result = max(result, abs(answer))
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.6MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.07ms, 10.5MB)
테스트 4 〉	통과 (0.07ms, 10.5MB)
테스트 5 〉	통과 (0.08ms, 10.5MB)
테스트 6 〉	통과 (0.22ms, 10.5MB)
테스트 7 〉	통과 (0.09ms, 10.5MB)
테스트 8 〉	통과 (0.09ms, 10.5MB)
테스트 9 〉	통과 (0.10ms, 10.6MB)
테스트 10 〉	통과 (0.11ms, 10.5MB)
테스트 11 〉	통과 (0.11ms, 10.6MB)
테스트 12 〉	통과 (0.12ms, 10.5MB)
테스트 13 〉	통과 (0.13ms, 10.5MB)
테스트 14 〉	통과 (0.15ms, 10.5MB)
테스트 15 〉	통과 (0.15ms, 10.5MB)
테스트 16 〉	통과 (0.06ms, 10.5MB)
테스트 17 〉	통과 (0.07ms, 10.5MB)
테스트 18 〉	통과 (0.06ms, 10.6MB)
테스트 19 〉	통과 (0.06ms, 10.5MB)
테스트 20 〉	통과 (0.06ms, 10.6MB)
테스트 21 〉	통과 (0.13ms, 10.6MB)
테스트 22 〉	통과 (0.15ms, 10.5MB)
테스트 23 〉	통과 (0.05ms, 10.5MB)
테스트 24 〉	통과 (0.26ms, 10.6MB)
테스트 25 〉	통과 (0.15ms, 10.5MB)
테스트 26 〉	통과 (0.05ms, 10.6MB)
테스트 27 〉	통과 (0.15ms, 10.5MB)
테스트 28 〉	통과 (0.16ms, 10.5MB)
테스트 29 〉	통과 (0.14ms, 10.5MB)
테스트 30 〉	통과 (0.15ms, 10.6MB)
"""