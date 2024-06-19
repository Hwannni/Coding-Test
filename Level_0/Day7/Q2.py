def solution(l, r):
    result = []
    for num in range(l, r + 1):
        str_num = str(num)
        if all(c in "05" for c in str_num):
            result.append(num)
    if not result:
        return [-1]
    return result
