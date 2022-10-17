# for ~ in도 가능
def solution(str1, str2):
    if str2 in str1:
        return 1
    return 2

# count도 가능
def solution(str1, str2):
    if str1.count(str2):
        return 1
    return 2