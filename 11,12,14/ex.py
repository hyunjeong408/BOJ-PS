def a(i):
    #print(i)
    if i>1:
        a(int(i/2))
        a(int(i/2))
    print("*")

a(5)