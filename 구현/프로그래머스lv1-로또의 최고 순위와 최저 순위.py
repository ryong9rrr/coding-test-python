from collections import defaultdict
def solution(lottos, win_nums):
    #최고순위 : 0을 모두 맞았다고 가정
    #최저순위 : 0을 모두 틀렸다고 가정
    d = defaultdict(bool)
    rank = [6, 6, 5, 4, 3, 2, 1]
    win = 0
    lose = 0
    zero = 0
    for num in win_nums:
        d[num] = True
    
    for num in lottos:
        if num == 0:
            zero += 1
        if d[num]:
            win += 1
        else:
            lose += 1
    
    return [rank[zero + win], rank[6-lose]]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
"""

# 과거 풀이 -> if ~ in 은 충분히 빠르다.
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    num = 0
    unKnown = 0
    for i in lottos :
        if i in win_nums :
            num += 1
        elif i == 0 :
            unKnown += 1
    
    return [rank[num+unKnown], rank[num]]

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
"""

"""
js

function solution(lottos, win_nums) {
    
    function rank(num){
        switch(num){
            case 6 :
                return 1;
                break;
            case 5 :
                return 2;
                break;
            case 4 :
                return 3;
                break;
            case 3 :
                return 4;
                break;
            case 2 :
                return 5;
                break;
            default :
                return 6;
                break;
        }
    }
    
    let num = 0
    let unKnown = 0
    lottos.forEach(n => {
        if( win_nums.indexOf(n) !== -1 ){
            num++;
        } else if(n === 0){
            unKnown++;
        }
    })
    let high = num + unKnown;
    let low = num;
    
    return [rank(high), rank(low)];
    
}

정확성  테스트
테스트 1 〉	통과 (0.11ms, 30.1MB)
테스트 2 〉	통과 (0.11ms, 29.8MB)
테스트 3 〉	통과 (0.11ms, 30.1MB)
테스트 4 〉	통과 (0.11ms, 30MB)
테스트 5 〉	통과 (0.11ms, 29.9MB)
테스트 6 〉	통과 (0.07ms, 30MB)
테스트 7 〉	통과 (0.11ms, 29.9MB)
테스트 8 〉	통과 (0.11ms, 30MB)
테스트 9 〉	통과 (0.10ms, 30MB)
테스트 10 〉	통과 (0.12ms, 30MB)
테스트 11 〉	통과 (0.12ms, 30MB)
테스트 12 〉	통과 (0.11ms, 30.1MB)
테스트 13 〉	통과 (0.12ms, 29.9MB)
테스트 14 〉	통과 (0.08ms, 29.9MB)
테스트 15 〉	통과 (0.11ms, 30MB)
"""

def solution(lottos, win_nums):
    # 알아보지 못하는 번호가 모두 맞았다고 가정 -> 최고순위
    # 모두 틀렸다고 가정 -> 최저 순위
    # ex) 6개 모두 알아보지 못하는 경우: 최고순위 1등, 최저순위 6등(낙첨)
    
    SCORE = [6, 6, 5, 4, 3, 2, 1]
    
    win = 0
    unknown = 0
    
    for lotto in lottos:
        if lotto == 0:
            unknown += 1
            
        elif lotto in win_nums:
            win += 1
    
    return [SCORE[win + unknown], SCORE[win]]

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 9.96MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 9.97MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 9.94MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
"""


"""
js

function solution(lottos, win_nums) {
    const SCORE = [6, 6, 5, 4, 3, 2, 1];
    const result = [];
    
    //const win = lottos.filter(lotto => win_nums.find(n => n === lotto)).length;
    const win = lottos.filter(lotto => win_nums.includes(lotto)).length;
    const unknown = lottos.filter(lotto => lotto === 0).length;
    
    return [SCORE[win + unknown], SCORE[win]]
}

정확성  테스트
테스트 1 〉	통과 (0.07ms, 30MB)
테스트 2 〉	통과 (0.12ms, 30MB)
테스트 3 〉	통과 (0.12ms, 30.1MB)
테스트 4 〉	통과 (0.10ms, 30.2MB)
테스트 5 〉	통과 (0.07ms, 30MB)
테스트 6 〉	통과 (0.07ms, 30MB)
테스트 7 〉	통과 (0.09ms, 30MB)
테스트 8 〉	통과 (0.10ms, 30MB)
테스트 9 〉	통과 (0.07ms, 30.2MB)
테스트 10 〉	통과 (0.09ms, 30.1MB)
테스트 11 〉	통과 (0.07ms, 30.1MB)
테스트 12 〉	통과 (0.07ms, 30.1MB)
테스트 13 〉	통과 (0.07ms, 30.1MB)
테스트 14 〉	통과 (0.08ms, 29.9MB)
테스트 15 〉	통과 (0.07ms, 29.8MB)
"""
