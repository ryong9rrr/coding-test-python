function Truck(weight, time) {
  this.weight = weight;
  this.time = time;
}

function solution(bridge_length, weight, truck_weights) {
  let answer = 0;

  let queue = [];
  let head = 0;
  let tail = 0;

  let truck_index = 0;
  let total_weight = 0;
  let time = 0;

  queue[tail++] = new Truck(truck_weights[truck_index], bridge_length + time);
  total_weight += truck_weights[truck_index++];
  time++;

  while (head != tail) {
    // 1. 다리에 올라간 트럭이 다리 길이보다 작아야 함
    // 2. 다리에 올라간 트럭들 무게와 다음 올라갈 트럭의 무게를 합한 값이 weight보다 작거나 같아야함
    // 시간을 보내면서 트럭이 한 대 빠지거나, 혹은 다 빠질 때 까지 대기해줘야함

    // 다리를 지난 트럭 처리
    if (queue[head].time === time) {
      total_weight -= queue[head++].weight;
    }

    if (
      tail - head < bridge_length &&
      total_weight + truck_weights[truck_index] <= weight
    ) {
      queue[tail++] = new Truck(
        truck_weights[truck_index],
        bridge_length + time
      );
      total_weight += truck_weights[truck_index++];
    } // 시간을 단축시키는 분기
    else if (queue[head]) {
      time = queue[head].time - 1;
    }
    time++;
  }
  return time;
}

// 실패..

/*
from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque()
    bridge = deque()
    time = 1
    
    for truck in truck_weights:
        q.append(truck)
    
    while q or bridge:
        
        while q and (not bridge or (bridge and len(bridge) < bridge_length and sum([x[1] for x in bridge]) + truck <= weight)):
            x = q.popleft()
            bridge.append((time, x))
            time += 1
        
        t, x = bridge.popleft()
        time = t + bridge_length
    
    return time
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	실패 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	실패 (0.64ms, 10.2MB)
테스트 5 〉	실패 (1.08ms, 10.3MB)
테스트 6 〉	실패 (0.98ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	실패 (0.02ms, 10.3MB)
테스트 9 〉	실패 (0.36ms, 10.3MB)
테스트 10 〉	실패 (0.01ms, 10.3MB)
테스트 11 〉	실패 (0.01ms, 10.3MB)
테스트 12 〉	실패 (0.06ms, 10.3MB)
테스트 13 〉	실패 (0.08ms, 10.3MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)


from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque()
    bridge = deque()
    
    for truck in truck_weights:
        q.append(truck)
    
    while True:
        if bridge and bridge[0][0] + bridge_length == time:
            bridge.popleft()
        
        if q:
            if not bridge:
                bridge.append((time, q.popleft()))
            else:
                if len(bridge) < bridge_length and sum([x[1] for x in bridge]) + truck <= weight:
                    bridge.append((time, q.popleft()))
        
        time += 1
        if not q and not bridge:
            break
    
    return time
정확성  테스트
테스트 1 〉	통과 (0.84ms, 10.2MB)
테스트 2 〉	실패 (19.23ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	실패 (30.46ms, 10.3MB)
테스트 5 〉	실패 (253.71ms, 10.3MB)
테스트 6 〉	실패 (91.80ms, 10.3MB)
테스트 7 〉	통과 (0.83ms, 10.3MB)
테스트 8 〉	실패 (0.15ms, 10.2MB)
테스트 9 〉	실패 (3.97ms, 10.3MB)
테스트 10 〉	실패 (0.20ms, 10.3MB)
테스트 11 〉	실패 (0.01ms, 10.2MB)
테스트 12 〉	실패 (0.26ms, 10.2MB)
테스트 13 〉	실패 (1.83ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
*/
