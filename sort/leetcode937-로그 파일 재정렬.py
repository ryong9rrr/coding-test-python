# 문자열 정렬
def reorderLogFiles(self, logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    
    l = []
    d = []
    
    for log in logs:
        x = log.split()[1].isdigit()
        if x:
            d.append(log)
        else:
            l.append(log)
    
    # 첫번째 기준이 같으면 두번째 기준으로 정렬한다.
    l = sorted(l, key = lambda x: (x.split()[1:], x.split()[0]))
    
    return l + d

"""js // 89ms

var reorderLogFiles = function(logs) {
    function isDigit(string) {
      return !Number.isNaN(Number(string));
    }
    
    function compare(a, b){
        let i = 1;
        while (a[i] && b[i]) {
            if (a[i] !== b[i]) {
                return (a[i] > b[i]) - (a[i] < b[i])
            } else i++;
        }
        if (b[i]) return -1
        return (a[0] > b[0]) - (a[0] < b[0])
    }
    
    const d = [];
    const l = [];
    
    for (const log of logs){
        const arr = log.split(" ");
        isDigit(arr[1]) ? d.push(log) : l.push(arr)
    }
    l.sort(compare)
    const sortedL = l.map(s => s.join(" "))
    return [...sortedL, ...d]
};
"""