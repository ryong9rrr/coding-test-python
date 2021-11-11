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