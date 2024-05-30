def solution(arr, queries):
    for s, e, k in queries:
        # s와 e는 범위, k는 배수 조건
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1
    return arr