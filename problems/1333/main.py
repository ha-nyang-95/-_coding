N,L,D=map(int,input().split())
L_sum=L
L_max=N*L+5*(N-1)
D_sum=D
for i in range(N):
    if D_sum in range(L_sum,L_sum+5):
        print(D_sum)
        break
    else:
        if L_sum+L+5==L_max:
            if L_sum+L>D_sum:
                print(D_sum+D)
                break
            else:
                print(D_sum)
                break
        else:
            L_sum+=L+5
            if L_sum>D_sum:
                D_sum+=D



n, l, d = map(int, input().split())

music = [True] * ((n * l) + (5 * (n - 1)))

for i in range(n):
    play_time = (l + 5) * i
    for j in range(play_time, play_time + l):
        music[j] = False
answer = 0
while answer < len(music):
    if music[answer]:
        break
    answer += d
print(answer)
