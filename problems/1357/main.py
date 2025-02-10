def Rev(x,y):
    x=int(x[::-1])
    y=int(y[::-1])
    z =str(x+y)[::-1]
    return int(z)

X,Y=input().split()
print(Rev(X,Y))