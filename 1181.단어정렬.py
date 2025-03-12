N = int(input())
alp = [input() for _ in range(N)]
num = [set() for _ in range(52)]
for a in alp:
    num[len(a)].add(a)

for a in num:
    if a:
        if len(a) > 1:
            for b in sorted(a):
                print(b)
        else:
            print(*a)
