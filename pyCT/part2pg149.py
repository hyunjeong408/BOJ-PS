n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs_cnt_icecream(x, y):
    if x<0 or x>=n or y<0 or y>=m: #범위를 벗어난 경우
        return False
    if graph[x][y]==0: #아직 방문하지 않은 경우
        graph[x][y] = 1
        dfs_cnt_icecream(x-1, y)
        dfs_cnt_icecream(x, y+1)
        dfs_cnt_icecream(x+1, y)
        dfs_cnt_icecream(x, y-1)
        return True
    return False

count = 0
for x in range(n):
    for y in range(m):
        if dfs_cnt_icecream(x, y):
            count += 1

print(count)