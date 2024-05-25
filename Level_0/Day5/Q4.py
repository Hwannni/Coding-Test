def solution(num_list):
    # 모든 원소들의 합을 받는 변수
    number_a = 0

    # 모든 원소들의 곱을 받는 변수
    # 곱을 받는 변수는 1로 초기화를 해야 정상적인 연산 가능
    number_b = 1

    # for문을 통해 모든 원소들의 곱과 합을 변수에 담음
    for i in num_list:
        number_a += i
        number_b *= i

    # number_a를 이용하여 제곱값을 담은 변수 생성
    number_c = number_a ** 2

    # if문을 통해 조건 생성 후 결과값 리턴
    return 1 if number_b < number_c else 0