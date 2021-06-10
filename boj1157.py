word = input()

word = word.upper()
cnt = 0
while(len(word)>0):
    tmp = word[0]
    if(cnt < word.count(tmp)):
        cnt = word.count(tmp)
        tmpWord = word[0]
    elif(cnt == word.count(tmp)):
        tmpWord = '?'
    word = word.replace(word[0], '')
    #print(word)
print(tmpWord)