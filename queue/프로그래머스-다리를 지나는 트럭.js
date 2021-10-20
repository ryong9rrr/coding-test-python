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
