def solution(a, b):
    answer = 0

    a, b = str(a), str(b)
    new_a = int(a + b)
    new_b = int(b + a)

    if new_a > new_b:
        answer += new_a
    else:
        answer += new_b

    return answer


# 다른 사람 풀이 -> format() 사용
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
