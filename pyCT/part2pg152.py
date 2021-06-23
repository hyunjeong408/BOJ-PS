from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def escape_bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tmpX = x+dx[i]
            tmpY = y+dy[i]
            if tmpX < 0 or tmpX >= n or tmpY < 0 or tmpY >= m:
                continue
            if maze[tmpX][tmpY] == 0:
                continue
            if maze[tmpX][tmpY] == 1:
                maze[tmpX][tmpY] = maze[x][y] + 1
                queue.append((tmpX, tmpY))
    return maze[n-1][m-1]

print(escape_bfs(0, 0))