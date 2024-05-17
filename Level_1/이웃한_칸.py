def solution(board, h, w):
    answer = 0
    n = board[h][w]
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(len(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if 0 <= h_check < len(board) and 0 <= w_check < len(board):
            if board[h_check][w_check] == n:
                answer += 1

    return answer
