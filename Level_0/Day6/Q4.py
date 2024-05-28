def solution(arr, queries):

    for query in queries:
        x, y = query
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    return arr
