n = int(input())
cnt = 0
cols = [-1]*n

def isPossible(lv):
    for i in range(lv):
        #같은 열에 위치
        if cols[i] == cols[lv]:
            return False
        #대각선에 위치
        elif abs(cols[i]-cols[lv]) == abs(i-lv):
            return False
    return True

def nQueen(lv):
    global cnt
    if lv == n:
        cnt += 1
        return 0
    else: #현재 lv에서
        for i in range(n): #가능한 열 위치
            cols[lv] = i
            if isPossible(lv):
                nQueen(lv+1)
nQueen(0)
print(cnt)