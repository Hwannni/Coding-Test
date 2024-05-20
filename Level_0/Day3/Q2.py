def solution(arr):
    answer = ""
    for i in range(len(arr)):
        answer += arr[i]
    return answer


# 다른 사람 풀이 -> 조인 사용
def solution(arr):
    return "".join(arr)
