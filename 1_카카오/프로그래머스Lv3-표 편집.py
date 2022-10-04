import copy
def solution(n, k, cmd):
    table = [i for i in range(n)]
    snapshots = [copy.copy(table)]

    for x in cmd:
        commands = x.split(" ")
        command = commands[0]
        if command == "U" or command == "D":
            shift = int(commands[1])
            if command == "U":
                k -= shift
                if k <= 0:
                    k = 0
            else:
                k += shift
                if k >= n - 1:
                    k = n - 1

        elif command == "C":
            snapshots.append(copy.copy(table))
            del table[k]
            last_idx = len(table) - 1
            if k > last_idx:
                k = last_idx

        elif command == "Z":
            snapshot = snapshots.pop()
            if table[k] != snapshot[k]:
                k += 1
            table = snapshot
        
    result = ["X"] * n
    for x in table:
        result[x] = "O"
    
    return "".join(result)

"""
시간초과가 나는 이유는 아마 del 사용(O(N)이 추가), 마지막에 결과를 구하는 과정에서 O(N^2)이 발생했기 때문같다.
정확성 테스트
테스트 1 〉 통과 (0.04ms, 10.4MB)
테스트 2 〉 통과 (0.03ms, 10.4MB)
테스트 3 〉 통과 (0.04ms, 10.4MB)
테스트 4 〉 통과 (0.03ms, 10.4MB)
테스트 5 〉 통과 (0.12ms, 10.3MB)
테스트 6 〉 통과 (0.13ms, 10.5MB)
테스트 7 〉 통과 (0.12ms, 10.4MB)
테스트 8 〉 통과 (0.15ms, 10.4MB)
테스트 9 〉 통과 (0.13ms, 10.4MB)
테스트 10 〉 통과 (0.12ms, 10.4MB)
테스트 11 〉 통과 (1.60ms, 10.4MB)
테스트 12 〉 통과 (1.56ms, 10.6MB)
테스트 13 〉 통과 (1.57ms, 10.5MB)
테스트 14 〉 통과 (1.58ms, 10.4MB)
테스트 15 〉 통과 (1.62ms, 10.6MB)
테스트 16 〉 통과 (1.60ms, 10.7MB)
테스트 17 〉 통과 (5.63ms, 10.6MB)
테스트 18 〉 통과 (5.79ms, 10.5MB)
테스트 19 〉 통과 (5.83ms, 10.4MB)
테스트 20 〉 통과 (6.32ms, 10.7MB)
테스트 21 〉 통과 (6.33ms, 10.9MB)
테스트 22 〉 통과 (6.80ms, 11MB)
테스트 23 〉 통과 (0.03ms, 10.4MB)
테스트 24 〉 통과 (0.03ms, 10.6MB)
테스트 25 〉 통과 (0.03ms, 10.4MB)
테스트 26 〉 통과 (0.03ms, 10.4MB)
테스트 27 〉 통과 (0.04ms, 10.4MB)
테스트 28 〉 통과 (0.04ms, 10.4MB)
테스트 29 〉 통과 (0.06ms, 10.4MB)
테스트 30 〉 통과 (0.05ms, 10.4MB)
효율성 테스트
테스트 1 〉 실패 (시간 초과)
테스트 2 〉 실패 (시간 초과)
테스트 3 〉 실패 (시간 초과)
테스트 4 〉 실패 (시간 초과)
테스트 5 〉 실패 (시간 초과)
테스트 6 〉 실패 (시간 초과)
테스트 7 〉 실패 (시간 초과)
테스트 8 〉 실패 (시간 초과)
테스트 9 〉 실패 (시간 초과)
테스트 10 〉 실패 (시간 초과)
"""

############################## 더블 연결리스트 풀이 ################################3
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
        
    def desc(self, reverse = False):
        nodes = []
        if reverse == False:
            node = self.head
            while node:
                nodes.append(node.data)
                node = node.next
        else:
            node = self.tail
            while node:
                nodes.append(node.data)
                node = node.prev
        return nodes
    
    def add(self, new_node):
        if not isinstance(new_node, Node):
            return
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def remove(self, target_node):
        if not isinstance(target_node, Node):
            return
        if self.head == target_node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == target_node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev_node = target_node.prev
            next_node = target_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
    
    def insert(self, target_node):
        if not isinstance(target_node, Node):
            return
        if target_node.prev is None:
            self.head.prev = target_node
            self.head = target_node
        elif target_node.next is None:
            self.tail.next = target_node
            self.tail = target_node
        else:
            node = target_node.prev
            node.next.prev = target_node
            node.next = target_node
            
            
def solution(n, k, cmd):
    dl = DoubleLinkedList()
    stack = []
    current_node = None
    for index in range(n):
        new_node = Node(index)
        if index == k:
            current_node = new_node
        dl.add(new_node)
    
    for command in cmd:
        if command == "C":
            stack.append(current_node)
            if current_node == dl.tail:
                dl.remove(current_node)
                current_node = dl.tail
            else:
                dl.remove(current_node)
                current_node = current_node.next
        elif command == "Z":
            if stack:
                dl.insert(stack.pop())
        else:
            c, shift = command.split(" ")
            shift = int(shift)
            if c == "U":
                while shift:
                    current_node = current_node.prev
                    shift -= 1
            if c == "D":
                while shift:
                    current_node = current_node.next
                    shift -= 1
    
    result = ["X"] * n
    for x in dl.desc():
        result[x] = "O"
    
    return "".join(result)
"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.23ms, 10.5MB)
테스트 6 〉	통과 (0.24ms, 10.4MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (0.23ms, 10.5MB)
테스트 9 〉	통과 (0.13ms, 10.4MB)
테스트 10 〉	통과 (0.21ms, 10.4MB)
테스트 11 〉	통과 (0.71ms, 10.4MB)
테스트 12 〉	통과 (1.35ms, 10.6MB)
테스트 13 〉	통과 (0.71ms, 10.4MB)
테스트 14 〉	통과 (1.15ms, 10.5MB)
테스트 15 〉	통과 (1.23ms, 10.4MB)
테스트 16 〉	통과 (1.20ms, 10.4MB)
테스트 17 〉	통과 (4.27ms, 10.5MB)
테스트 18 〉	통과 (3.95ms, 10.5MB)
테스트 19 〉	통과 (3.71ms, 10.5MB)
테스트 20 〉	통과 (2.46ms, 10.5MB)
테스트 21 〉	통과 (2.27ms, 10.4MB)
테스트 22 〉	통과 (4.46ms, 10.4MB)
테스트 23 〉	통과 (0.05ms, 10.4MB)
테스트 24 〉	통과 (0.05ms, 10.4MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
테스트 26 〉	통과 (0.04ms, 10.3MB)
테스트 27 〉	통과 (0.04ms, 10.4MB)
테스트 28 〉	통과 (0.06ms, 10.3MB)
테스트 29 〉	통과 (0.07ms, 10.3MB)
테스트 30 〉	통과 (0.10ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (1512.58ms, 213MB)
테스트 2 〉	통과 (1363.22ms, 213MB)
테스트 3 〉	통과 (1533.20ms, 213MB)
테스트 4 〉	통과 (1480.66ms, 220MB)
테스트 5 〉	통과 (1368.33ms, 220MB)
테스트 6 〉	통과 (1464.70ms, 218MB)
테스트 7 〉	통과 (262.99ms, 56.5MB)
테스트 8 〉	통과 (336.03ms, 70MB)
테스트 9 〉	통과 (1471.53ms, 220MB)
테스트 10 〉	통과 (1346.79ms, 220MB)
"""