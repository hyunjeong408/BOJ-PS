n = int(input())
words = []
for i in range(n):
    words.append(input())

def checkGroup(word):
    index = -1
    word = list(word)
    while(len(word)>0):
        tmpWord = word[0]
        index = word.index(tmpWord)
        while(index != -1):
            del word[index]
            if tmpWord in word:
                nxtIdx = word.index(tmpWord)
                if nxtIdx != 0:
                    return False
                index = nxtIdx
            else:
                if len(word)==0:
                    break
                tmpWord = word[0]
                index = word.index(tmpWord)
    return True
cnt = 0
for w in words:
    if(checkGroup(w)):
        cnt += 1
print(cnt)