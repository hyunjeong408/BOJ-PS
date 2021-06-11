n, m = map(int, input().split())

result = [0]*m
visitied = [0]*(n+1)

def dfs(depth, n, m):
    if depth == m+1:  # 최종 깊이까지 들어갔을 때
        for i in range(m):
            print(result[i],end=' ')
        print()
        return
    for k in range(1,n+1):
        if visitied[k] == 0:
            visitied[k] = 1
            result[depth-1] = k
            dfs(depth+1, n, m)
            visitied[k] = 0

dfs(1, n, m)