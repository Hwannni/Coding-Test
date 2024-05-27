def solution(num_list):
    odd_str = ''.join([str(num) for num in num_list if num % 2 != 0])
    even_str = ''.join([str(num) for num in num_list if num % 2 == 0])
    return int(odd_str) + int(even_str) if odd_str and even_str else int(odd_str or '0') + int(even_str or '0')
