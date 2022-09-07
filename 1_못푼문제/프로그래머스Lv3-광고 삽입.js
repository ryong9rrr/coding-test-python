// 2021 KAKAO BLIND RECRUITMENT
// 슬라이딩 윈도우 문제? 풀다 말았다..
const makeSeconds = (time) => {
  const [h, m, s] = time.split(':')
  return 3600 * Number(h) + 60 * Number(m) + Number(s)
}

function solution(play_time, adv_time, logs) {
  TIME_TABLE = {}

  logs.forEach((v, i) => {
    const [start, end] = v.split('-')
    const interval = makeSeconds(end) - makeSeconds(start)
    TIME_TABLE[i] = {
      id: i,
      start,
      end,
      interval,
    }
  })

  console.log(TIME_TABLE)
}
