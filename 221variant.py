# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    M, N = len(A), len(A[0])
    dp = [[0] * (N + 1) for _ in range(M+1)]
    squares= dict()

    # get the square size information
    for r in range(M):
        for c in range(N):
            if A[r][c]:
                dp[r+1][c+1] = min(dp[r][c],dp[r+1][c],dp[r][c+1]) + 1
                if dp[r+1][c+1] not in squares:
                    new_square = [1, [(r,c)]]
                    squares[dp[r+1][c+1]] = new_square
                else:
                    old_square = squares.get(dp[r+1][c+1])
                    new_square = [old_square[0]+1,old_square[1]+[(r,c)]]
                    squares[dp[r+1][c+1]] = new_square
    

    max_square = 0
    # check if 2 squares exist
    for k, v in squares.items():
        if v[0] >= 2:
            positions = v[1]
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    r1, c1 = positions[i]
                    r2, c2 = positions[j]
                    if abs(r1 - r2) >= k or abs(c1 - c2) >= k:
                        max_square = max(max_square, k*k)


    return max_square

matrix = [[True, True, True, True], 
          [True, True, True, True], 
          [True, True, True, True], 
          [True, True, True, True], 
          [True, True, True, True], 
          [True, True, True, True]]
print(solution(matrix))
