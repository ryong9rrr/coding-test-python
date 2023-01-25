/*
기본시간, 기본요금, 단위시간, 단위요금 = fees

1. 차량의 누적 주차 시간을 구한다. 만약 차량이 마지막으로 나간 기록이 없다면 마지막으로 나간 시간을 23:59으로 정한다.

2. 차량의 주차 요금을 계산한다.
= 기본요금 + ((차량의 누적 주차 시간 - 기본시간) / 단위 시간)을 올림 x 단위 요금

3. 차량 번호를 오름차순대로 정렬한 후 그 차량의 주차 요금을 배열에 담아 리턴한다.
*/

const calculateFee = (fees, accMinutes) => {
  const [baseTime, baseFee, unitTime, unitFee] = fees
  if (baseTime >= accMinutes) {
    return baseFee
  }
  return baseFee + Math.ceil((accMinutes - baseTime) / unitTime) * unitFee
}

const convertTime = (time) => {
  return time.split(":").map((t) => Number(t))
}

const timeForMinute = (hour, minute) => {
  return hour * 60 + minute
}

const calculateMinuteInterval = (inTime, outTime) => {
  return (
    timeForMinute(...convertTime(outTime)) -
    timeForMinute(...convertTime(inTime))
  )
}

class Car {
  constructor(inTime) {
    this._state = "IN"
    this._lastInTime = inTime
    this._accMinutes = 0
  }

  get state() {
    return this._state
  }

  get accMinutes() {
    return this._accMinutes
  }

  update(stateType, time) {
    switch (stateType) {
      case "IN":
        this._in(time)
        return
      case "OUT":
        this._out(time)
        return
      default:
        throw new Error(`${stateType} is invalid..`)
    }
  }

  _in(time) {
    this._state = "IN"
    this._lastInTime = time
  }

  _out(time) {
    this._state = "OUT"
    this._accMinutes += calculateMinuteInterval(this._lastInTime, time)
  }
}

class TimeTable {
  constructor() {
    this._table = {}
  }

  get table() {
    return this._table
  }

  get carIds() {
    return Object.keys(this._table).sort()
  }

  registry(registryType, carId, time) {
    switch (registryType) {
      case "IN":
        this._inCar(carId, time)
        return
      case "OUT":
        this._outCar(carId, time)
        return
      default:
        throw new Error(`${registryType} is isvalid.`)
    }
  }

  getRestCarIds() {
    return Object.keys(this._table).filter(
      (carId) => this._table[carId].state === "IN",
    )
  }

  handleRest() {
    this.getRestCarIds().forEach((carId) => {
      this.registry("OUT", carId, "23:59")
    })
  }

  _inCar(carId, inTime) {
    if (!this._table[carId]) {
      this._table[carId] = new Car(inTime)
      return
    }
    const car = this._table[carId]
    car.update("IN", inTime)
  }

  _outCar(carId, outTime) {
    if (!this._table[carId]) {
      throw new Error(`${carId} is not exist.`)
    }
    const car = this._table[carId]
    car.update("OUT", outTime)
  }
}

function solution(fees, records) {
  const timeTable = new TimeTable()

  records.forEach((record) => {
    const [time, carId, registryType] = record.split(" ")
    timeTable.registry(registryType, carId, time)
  })

  timeTable.handleRest()

  return timeTable.carIds.map((carId) =>
    calculateFee(fees, timeTable.table[carId].accMinutes),
  )
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.47ms, 33.5MB)
// 테스트 2 〉	통과 (0.60ms, 33.5MB)
// 테스트 3 〉	통과 (0.92ms, 33.4MB)
// 테스트 4 〉	통과 (0.69ms, 33.5MB)
// 테스트 5 〉	통과 (1.79ms, 33.6MB)
// 테스트 6 〉	통과 (1.74ms, 33.6MB)
// 테스트 7 〉	통과 (7.61ms, 34.6MB)
// 테스트 8 〉	통과 (2.46ms, 34.3MB)
// 테스트 9 〉	통과 (1.47ms, 33.8MB)
// 테스트 10 〉	통과 (3.60ms, 34.4MB)
// 테스트 11 〉	통과 (6.49ms, 34.7MB)
// 테스트 12 〉	통과 (6.77ms, 34.7MB)
// 테스트 13 〉	통과 (0.49ms, 33.5MB)
// 테스트 14 〉	통과 (0.53ms, 33.4MB)
// 테스트 15 〉	통과 (0.38ms, 33.5MB)
// 테스트 16 〉	통과 (0.31ms, 33.4MB)
