import numpy as np
def solution(board, moves):
    LEN = len(board)
    board_cols = np.array(board)
    new_board = []
    for i in range(LEN) :
        new_board.append( list(reversed([x for x in board_cols[:,i] if x!=0])) )
        
    print( new_board )
    
    count = 0
    basket = []
    for move in moves :
        if len(new_board[move-1]) != 0 :
            basket.append( new_board[move-1].pop() )
            if len(basket) >= 2 :
                if basket[-1] == basket[-2] :
                    basket.pop()
                    basket.pop()
                    count += 2
    return count

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 27.7MB)
테스트 2 〉	통과 (0.07ms, 27.7MB)
테스트 3 〉	통과 (0.07ms, 27.7MB)
테스트 4 〉	통과 (0.94ms, 27.9MB)
테스트 5 〉	통과 (0.12ms, 27.8MB)
테스트 6 〉	통과 (0.10ms, 27.9MB)
테스트 7 〉	통과 (0.15ms, 27.8MB)
테스트 8 〉	통과 (0.46ms, 27.7MB)
테스트 9 〉	통과 (0.38ms, 27.9MB)
테스트 10 〉	통과 (0.39ms, 27.9MB)
테스트 11 〉	통과 (0.79ms, 28MB)
"""

from collections import deque
def solution(board, moves):
    result = 0
    #인형이 담길 배열
    stack = deque()
    b = len(board)
    for j in moves:
        for i in range(b):
            if board[i][j-1] != 0:
                x = board[i][j-1]
                board[i][j-1] = 0
                if stack and x == stack[-1]:
                    result += 2
                    stack.pop()
                    break
                stack.append(x)
                break
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (1.12ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.28ms, 10.3MB)
테스트 9 〉	통과 (0.24ms, 10.2MB)
테스트 10 〉	통과 (0.29ms, 10.2MB)
테스트 11 〉	통과 (0.66ms, 10.4MB)
"""

"""
js

function solution(board, moves) {
    
    const LEN = board.length;
    let newBoard = [];
    let col = [];
    for(let i=0; i<LEN; i++){
        for(let row=0; row<LEN; row++){
            if( [...board][row][i] !== 0 ){
                col.push( [...board][row][i] );
            }
        }
        col.reverse();
        newBoard.push(col);
        col = [];
    }
    
    let count = 0;
    let basket = [];
    
    for(const i in moves){
        if( newBoard[moves[i]-1].length !== 0 ) {
            basket.push( newBoard[moves[i]-1].pop() )
            if( basket.length >= 2 ){
                if (basket[basket.length-1] == basket[basket.length-2]){
                    basket.pop()
                    basket.pop()
                    count += 2
                }
            }
        }
    }
    return count
}

정확성  테스트
테스트 1 〉	통과 (0.15ms, 29.8MB)
테스트 2 〉	통과 (0.11ms, 29.8MB)
테스트 3 〉	통과 (0.15ms, 30.3MB)
테스트 4 〉	통과 (0.81ms, 30.5MB)
테스트 5 〉	통과 (0.15ms, 30.3MB)
테스트 6 〉	통과 (0.14ms, 30MB)
테스트 7 〉	통과 (0.13ms, 30.1MB)
테스트 8 〉	통과 (0.58ms, 30.3MB)
테스트 9 〉	통과 (0.22ms, 30.1MB)
테스트 10 〉	통과 (0.38ms, 30.5MB)
테스트 11 〉	통과 (0.72ms, 30.4MB)
"""

# 2022년 7월 풀이, 훨씬 더 직관적이고 나은 풀이 같다. 심지어 시간도 더 짧아졌다.
from collections import deque
def solution(board, moves):
    SIZE = len(board)
    matrix = [deque() for _ in range(SIZE)]
    
    # matrix 초기화
    for y in range(SIZE):
        for x in range(SIZE):
            if board[x][y] != 0:
                matrix[y].append(board[x][y])
                
    basket = []
    result = 0
    
    for col in moves:
        x = col - 1
        if matrix[x]:
            target = matrix[x].popleft()
            if basket and basket[-1] == target:
                basket.pop()
                result += 2
            else:
                basket.append(target)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.30ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.11ms, 10.3MB)
테스트 9 〉	통과 (0.10ms, 10.1MB)
테스트 10 〉	통과 (0.11ms, 10.3MB)
테스트 11 〉	통과 (0.23ms, 10.3MB)
"""

"""
js // Queue 클래스 모듈을 이용한 풀이

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.front = this.tail = null;
    this.size = 0;
  }

  get peek() {
    return (this.front && this.front.value) || null;
  }

  enqueue(newValue) {
    const newNode = new Node(newValue);
    if (!this.front) {
      this.front = this.tail = newNode;
    } else {
      this.tail = this.tail.next = newNode;
    }
    this.size++;
  }

  dequeue() {
    if (!this.front) return null;
    const extracted = this.front.value;
    this.front = this.front.next;
    this.size--;
    return extracted;
  }
}

function solution(board, moves) {
    const SIZE = board.length;
    const matrix = Array.from({length: SIZE}, (v) => new Queue())
    
    // matrix 초기화
    for(let y = 0; y < SIZE; y++){
        for (let x = 0; x < SIZE; x++){
            if (board[x][y]) {
                matrix[y].enqueue(board[x][y])
            }
        }
    }
    
    const basket = [];
    let result = 0;
    
    for (const col of moves) {
        const x = col - 1;
        if (matrix[x].size) {
            const target = matrix[x].dequeue();
            const basketLen = basket.length;
            const basketTailItem = basket[basketLen - 1]
            if (basketLen > 0 && basketTailItem === target) {
                basket.pop();
                result += 2;
            } else {
                basket.push(target);
            }
        }
    }
    
    return result
}

정확성  테스트
테스트 1 〉	통과 (0.37ms, 29.8MB)
테스트 2 〉	통과 (0.39ms, 30MB)
테스트 3 〉	통과 (0.22ms, 30.1MB)
테스트 4 〉	통과 (0.82ms, 29.8MB)
테스트 5 〉	통과 (0.39ms, 29.9MB)
테스트 6 〉	통과 (0.43ms, 30.1MB)
테스트 7 〉	통과 (0.41ms, 29.9MB)
테스트 8 〉	통과 (0.53ms, 29.9MB)
테스트 9 〉	통과 (0.51ms, 30MB)
테스트 10 〉	통과 (0.52ms, 30MB)
테스트 11 〉	통과 (0.60ms, 30MB)
"""