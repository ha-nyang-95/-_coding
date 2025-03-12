import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    L = sys.stdin.readline().split()
    if L[0] == 'push':
        stack.append(int(L[1]))
    elif L[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif L[0] == 'size':
        print(len(stack))
    elif L[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif L[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
