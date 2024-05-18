def solution(my_string, overwrite_string, s):
    start_string = my_string[:s]
    end_string = my_string[s + len(overwrite_string) :]
    answer = start_string + overwrite_string + end_string
    return answer
