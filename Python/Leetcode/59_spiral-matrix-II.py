def generate_spiral(n):
    dx, dy = 0, 1  # direction pointers
    matrix = [[None] * n for _ in range(n)]
    x, y = 0, 0  # starting point
    for i in range(1, n*n + 1):
        matrix[x][y] = i
        # check next position
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] is None:
            x, y = nx, ny  # proceed to next position
        else:
            dx, dy = dy, -dx  # change direction
            x, y = x + dx, y + dy  # proceed to next position
    return matrix