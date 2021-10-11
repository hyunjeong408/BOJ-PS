inputStr = input().replace('()', '*')
pipeCnt = 0
total = 0

for i in inputStr:
    if i == '(': #새파이프시작
        pipeCnt += 1
        total += 1
    elif i == ')': #파이프 하나 끝
        pipeCnt -= 1
    else: #레이저 절단
        total += pipeCnt

print(total)