def solution(num_list):
    # append 사용
    if num_list[-1] > num_list[-2]:
        last_item = num_list[-1] - num_list[-2]
        num_list.append(last_item)
    else:
        doubled_last_item = num_list[-1] * 2
        num_list.append(doubled_last_item)

    return num_list


# 다른 사람 풀이
def solution(l):
    l.append(l[-1] - l[-2] if l[-1] > l[-2] else l[-1] * 2)
    return l
