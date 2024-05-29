# GPT 힘을 크게 빌림 ㅠㅠ
def solution(arr, queries):
    result = []

    for query in queries:
        s, e, k = query
        found = False
        min_value = float("inf")

        for i in range(s, e + 1):
            if arr[i] > k:
                min_value = min(min_value, arr[i])
                found = True

        if found:
            result.append(min_value)
        else:
            result.append(-1)

    return result
