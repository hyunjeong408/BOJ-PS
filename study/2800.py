from itertools import combinations

inputStr = input()

startParen = []
idxStack = []

for i in range(len(inputStr)):
    if inputStr[i] == '(':
        startParen.append(i)
    elif inputStr[i] == ')':
        idxStack.append((startParen.pop(), i))

idxs = [i+1 for i in range(len(idxStack))]
combi = []
for i in range(len(idxStack)):
    combi += list(combinations(idxs, i+1))

strList = []
for c in combi:
    removeIdx = []
    for k in c:
        removeIdx.append(idxStack[k-1][0])
        removeIdx.append(idxStack[k-1][1])
    s = ''
    for i in range(len(inputStr)):
        if i not in removeIdx:
            s += inputStr[i]
    if s not in strList:
        strList.append(s)

strList.sort()
for l in strList:
    print(l)
