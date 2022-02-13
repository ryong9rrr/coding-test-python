def check_mht(close, place):
    n = len(close)
    # 사람들의 조합
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = close[i]
            x2, y2 = close[j]
            # 맨해튼거리 측정
            distance = abs(x1 - x2) + abs(y1 - y2)
            # 1이라면 거리두기를 지키지 않은 것
            if distance == 1:
                return 0
            # 2라면 파티션 유무를 확인
            elif distance == 2:
                if x1 == x2 and place[x1][y2 - 1] == "O":
                    return 0
                elif y1 == y2 and place[x2 - 1][y1] == "O":
                    return 0
                elif place[x1][y2] == "O" or place[x2][y1] == "O":
                    return 0
    return 1
    

def solution(places):
    result = []
    for place in places:
        # 가까이 앉은 사람들을 찾습니다.
        close = []
        for n in range(5):
            for m in range(5):
                if place[n][m] == "P":
                    close.append((n, m))
        result.append(check_mht(close, place))
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.05ms, 10.3MB)
테스트 20 〉	통과 (0.04ms, 10.3MB)
테스트 21 〉	통과 (0.03ms, 10.3MB)
테스트 22 〉	통과 (0.06ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.05ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
테스트 27 〉	통과 (0.05ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.03ms, 10.3MB)
테스트 30 〉	통과 (0.02ms, 10.4MB)
"""


"""js
// matrix: string[][] => [number, number][]
function getSeats(matrix){
    const seats = [];
    for (let n = 0; n < 5; n++){
        for (let m = 0; m < 5; m++){
            if (matrix[n][m] === "P"){
                seats.push([n, m])
            }
        }
    }
    return seats
}

// seats: [number, number][], place: string[][] => number
function checkMht(seats, place){
    const n = seats.length;
    for (let i = 0; i < n - 1; i++){
        for (let j = i + 1; j < n; j++){
            const [x1, y1] = seats[i]
            const [x2, y2] = seats[j]
            const mht = Math.abs(x1 - x2) + Math.abs(y1 - y2)
            if (mht === 1) return 0;
            else if (mht === 2) {
                if (x1 === x2 && place[x1][y2 - 1] === "O") return 0;
                else if (y1 === y2 && place[x2 - 1][y1] === "O") return 0;
                else if (place[x1][y2] === "O" || place[x2][y1] === "O") return 0;
            }
        }
    }
    return 1;
}

function solution(places) {
    const result = [];
    places.forEach(place => {
        const peopleSeats = getSeats(place);
        result.push(checkMht(peopleSeats, place))
    })
    return result;
}

정확성  테스트
테스트 1 〉	통과 (0.24ms, 30.2MB)
테스트 2 〉	통과 (0.20ms, 30.3MB)
테스트 3 〉	통과 (0.22ms, 30.1MB)
테스트 4 〉	통과 (0.18ms, 30.3MB)
테스트 5 〉	통과 (0.21ms, 30.3MB)
테스트 6 〉	통과 (0.20ms, 30.2MB)
테스트 7 〉	통과 (0.18ms, 30.2MB)
테스트 8 〉	통과 (0.21ms, 30.2MB)
테스트 9 〉	통과 (0.21ms, 30.3MB)
테스트 10 〉	통과 (0.20ms, 30.1MB)
테스트 11 〉	통과 (0.20ms, 29.9MB)
테스트 12 〉	통과 (0.20ms, 30.2MB)
테스트 13 〉	통과 (0.20ms, 30.2MB)
테스트 14 〉	통과 (0.21ms, 30.1MB)
테스트 15 〉	통과 (0.20ms, 30.1MB)
테스트 16 〉	통과 (0.17ms, 30.2MB)
테스트 17 〉	통과 (0.20ms, 30MB)
테스트 18 〉	통과 (0.22ms, 30.1MB)
테스트 19 〉	통과 (0.19ms, 29.9MB)
테스트 20 〉	통과 (0.21ms, 30.1MB)
테스트 21 〉	통과 (0.20ms, 30MB)
테스트 22 〉	통과 (0.20ms, 30MB)
테스트 23 〉	통과 (0.18ms, 30.3MB)
테스트 24 〉	통과 (0.20ms, 29.9MB)
테스트 25 〉	통과 (0.16ms, 30.1MB)
테스트 26 〉	통과 (0.18ms, 30.3MB)
테스트 27 〉	통과 (0.19ms, 30.1MB)
테스트 28 〉	통과 (0.19ms, 30.1MB)
테스트 29 〉	통과 (0.19ms, 30.3MB)
테스트 30 〉	통과 (0.16ms, 30MB)
"""