def solution(ineq, eq, n, m):
    if eq == "=":
        condition = f"{n} {ineq}= {m}"
    else:
        condition = f"{n} {ineq} {m}"

    # eval 함수를 사용하여 조건 평가
    return 1 if eval(condition) else 0
