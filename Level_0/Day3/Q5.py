def solution(a, b):
    answer = 0
    c = int(f"{a}{b}")
    d = 2 * a * b
    if c > d:
        answer = c
    elif c < d:
        answer = d
    else:
        answer = c

    return answer


# 다른 사람 풀이 -> max()함수를 적절히 이용
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
