def solution(numbers, hand):
    answer = ""
    key_pad = [["*",7,4,1],[0,8,5,2],["#",9,6,3]];
    
    key_matrix = []
    
    for num in numbers :
        for x in range(0,3) :
            for y in range(0,4) :
                if num == key_pad[x][y] :
                    key_matrix.append([x,y])
                    
    tempL = [0,0]
    tempR = [2,0]
    
    for key in key_matrix :
        L = abs( tempL[0]-key[0] ) + abs( tempL[1]-key[1] )
        R = abs( tempR[0]-key[0] ) + abs( tempR[1]-key[1] )
        
        if key[0] == 0 :
            answer += "L"
            tempL = [key[0], key[1]]
        elif key[0] == 2 :
            answer += "R"
            tempR = [key[0], key[1]]
        else :
            if L == R :
                if hand == "right" :
                    answer += "R"
                    tempR = [key[0], key[1]]
                else :
                    answer += "L"
                    tempL = [key[0], key[1]]
            else :
                if L > R :
                    answer += "R"
                    tempR = [key[0], key[1]]
                else :
                    answer += "L"
                    tempL = [key[0], key[1]]
    
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.4MB)
테스트 9 〉	통과 (0.07ms, 10.4MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.17ms, 10.3MB)
테스트 12 〉	통과 (0.16ms, 10.3MB)
테스트 13 〉	통과 (0.32ms, 10.2MB)
테스트 14 〉	통과 (0.69ms, 10.3MB)
테스트 15 〉	통과 (1.45ms, 10.3MB)
테스트 16 〉	통과 (1.60ms, 10.2MB)
테스트 17 〉	통과 (2.94ms, 10.3MB)
테스트 18 〉	통과 (2.74ms, 10.3MB)
테스트 19 〉	통과 (2.59ms, 10.2MB)
테스트 20 〉	통과 (2.80ms, 10.3MB)
"""

def solution(numbers, hand):
    def get_distance(left, right, target):
        [la, lb] = left
        [ra, rb] = right
        [ta, tb] = target
        lr = abs(la-ta) + abs(lb-tb)
        rr = abs(ra-ta) + abs(rb-tb)
        # 오른손거리가 더 길다면
        if lr < rr:
            return 0
        elif lr == rr:
            return 1
        else:
            return 2
    # 1, 4, 7을 누를때는 무조건 왼손
    # 3, 6, 9를 누를때는 무조건 오른손
    # 2, 5, 8, 0을 누를때는 가까운손
    # 거리가 같다면 hand로
    phone = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2],
        0: [3,1],
    }
    current_left = [3,0]
    current_right = [3,2]
    result = ""
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            current_left = phone[number]
            result += "L"
        
        elif number == 3 or number == 6 or number == 9:
            current_right = phone[number]
            result += "R"
        else:
            x = get_distance(current_left, current_right, phone[number])
            if x == 0:
                current_left = phone[number]
                result += "L"
            elif x == 1:
                if hand == "left":
                    current_left = phone[number]
                    result += "L"
                else:
                    current_right = phone[number]
                    result += "R"
            elif x == 2:
                current_right = phone[number]
                result += "R"
                
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.09ms, 10.4MB)
테스트 15 〉	통과 (0.18ms, 10.3MB)
테스트 16 〉	통과 (0.28ms, 10.3MB)
테스트 17 〉	통과 (0.33ms, 10.3MB)
테스트 18 〉	통과 (0.32ms, 10.3MB)
테스트 19 〉	통과 (0.36ms, 10.3MB)
테스트 20 〉	통과 (0.32ms, 10.4MB)
"""