const divmod = (a, b) => {
  return [Math.floor(a / b), a % b]
}

const convertTime = (time) => {
  const [hour, minute] = time.split(":")
  return parseInt(hour, 10) * 60 + parseInt(minute)
}

const intervalMinute = (startTime, endTime) => {
  return convertTime(endTime) - convertTime(startTime)
}

const getRunningSheet = (sheet, runningMinute) => {
  const len = sheet.length
  if (len === runningMinute) {
    return sheet
  }

  if (runningMinute < len) {
    return sheet.slice(0, runningMinute)
  }

  const [a, b] = divmod(runningMinute, len)
  return sheet.repeat(a) + sheet.slice(0, b)
}

const replaceMelody = (melody) => {
  const specialMelodies = [
    ["C#", "c"],
    ["D#", "d"],
    ["F#", "f"],
    ["G#", "g"],
    ["A#", "a"],
  ]

  for (const [origin, replaced] of specialMelodies) {
    const regexp = new RegExp(origin, "g")
    melody = melody.replace(regexp, replaced)
  }

  return melody
}

const compare = (a, b) => {
  return a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]
}

function solution(m, musicinfos) {
  const target = replaceMelody(m)
  const result = []

  for (let i = 0; i < musicinfos.length; i += 1) {
    const musicinfo = musicinfos[i]
    const [startTime, endTime, title, originSheet] = musicinfo.split(",")
    const sheet = replaceMelody(originSheet)
    const runningMinute = intervalMinute(startTime, endTime)
    const runningSheet = getRunningSheet(sheet, runningMinute)
    if (runningSheet.includes(target)) {
      result.push([runningMinute, i, title])
    }
  }

  if (result.length === 0) {
    return "(None)"
  }

  return result.sort(compare)[0][2]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.32ms, 33.5MB)
// 테스트 2 〉	통과 (0.33ms, 33.5MB)
// 테스트 3 〉	통과 (0.47ms, 33.5MB)
// 테스트 4 〉	통과 (0.30ms, 33.5MB)
// 테스트 5 〉	통과 (0.33ms, 33.6MB)
// 테스트 6 〉	통과 (0.37ms, 33.6MB)
// 테스트 7 〉	통과 (0.58ms, 33.6MB)
// 테스트 8 〉	통과 (0.55ms, 33.6MB)
// 테스트 9 〉	통과 (0.60ms, 33.6MB)
// 테스트 10 〉	통과 (0.59ms, 33.6MB)
// 테스트 11 〉	통과 (0.55ms, 33.6MB)
// 테스트 12 〉	통과 (0.63ms, 33.6MB)
// 테스트 13 〉	통과 (0.59ms, 33.6MB)
// 테스트 14 〉	통과 (0.56ms, 33.6MB)
// 테스트 15 〉	통과 (0.54ms, 33.6MB)
// 테스트 16 〉	통과 (0.85ms, 33.6MB)
// 테스트 17 〉	통과 (0.55ms, 33.7MB)
// 테스트 18 〉	통과 (0.85ms, 33.6MB)
// 테스트 19 〉	통과 (0.66ms, 33.6MB)
// 테스트 20 〉	통과 (0.62ms, 33.6MB)
// 테스트 21 〉	통과 (0.59ms, 33.6MB)
// 테스트 22 〉	통과 (0.54ms, 33.6MB)
// 테스트 23 〉	통과 (0.56ms, 33.6MB)
// 테스트 24 〉	통과 (0.59ms, 33.6MB)
// 테스트 25 〉	통과 (0.32ms, 33.6MB)
// 테스트 26 〉	통과 (0.34ms, 33.6MB)
// 테스트 27 〉	통과 (0.56ms, 33.6MB)
// 테스트 28 〉	통과 (0.54ms, 33.6MB)
// 테스트 29 〉	통과 (2.81ms, 34.6MB)
// 테스트 30 〉	통과 (2.62ms, 34.6MB)
