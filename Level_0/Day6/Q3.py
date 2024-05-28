def solution(numLog):
    result = ""
    dic = {1: "w", -1: "s", 10: "d", -10: "a"}

    for i in range(1, len(numLog)):
        number = numLog[i] - numLog[i - 1]
        if number in dic:
            result += dic[number]

    return result
