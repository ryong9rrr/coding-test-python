# 383ms(37.46%), 19MB(75.92%)
class SummaryRanges:

    def __init__(self):
        self.arr = set()

    def addNum(self, value: int) -> None:
        self.arr.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        left = right = -1
        for value in sorted(list(self.arr)):
            if left < 0:
                left = right = value
            elif right + 1 == value:
                right = value # 혹은 right += 1
            else:
                intervals.append((left, right))
                left = right = value
        intervals.append((left, right))
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()