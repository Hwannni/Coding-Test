# 딕셔너리와 for문 이용
def solution(n, control):
    dic = {
        "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10
    }
    
    for char in control:
        if char in dic:
            n += dic[char] 

    return n

#  값은 여전히 나오지만 채점에서 불통
def solution(n, control):
    answer = 0
    
    for char in control:
        if char == 'w':
            answer += 1
        elif char == 's':
            answer -= 1
        elif char == 'd':
            answer += 10
        elif char == 'a':
            answer -= 10

    return answer


# 내가 쓴 코드를 간략하게 작성 -> 다른 사람이 작성한 코드
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])