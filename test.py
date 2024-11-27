def maximal_two_nonoverlapping_squares(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    squares = []
    
    # Build the DP table
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 1
                # Store the square information
                squares.append((dp[i][j], i, j))
    
    # Sort squares by size (largest first)
    squares.sort(reverse=True, key=lambda x: x[0])
    
    # Find the two largest non-overlapping squares
    def is_non_overlapping(s1, s2):
        size1, x1, y1 = s1
        size2, x2, y2 = s2
        # Bounding box of the first square
        x1_min, y1_min = x1 - size1 + 1, y1 - size1 + 1
        x2_min, y2_min = x2 - size2 + 1, y2 - size2 + 1
        # Check for overlap
        return not (x1_min <= x2 <= x1 and y1_min <= y2 <= y1 or
                    x2_min <= x1 <= x2 and y2_min <= y1 <= y2)
    
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            if is_non_overlapping(squares[i], squares[j]):
                return squares[i][0] ** 2 + squares[j][0] ** 2
    
    return 0  # If no two non-overlapping squares are found


matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0]
]

print(maximal_two_nonoverlapping_squares(matrix))