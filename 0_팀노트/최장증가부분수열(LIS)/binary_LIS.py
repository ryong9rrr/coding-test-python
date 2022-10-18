def binary_LIS(numbers):
    DP = [numbers[0]]
    for i in range(1, len(numbers)):
        target = numbers[i]
        if target > DP[-1]:
            DP.append(target)
        else:
            idx = bisect_left(DP, target)
            DP[idx] = target
    return len(DP)