N, m, M, T, R = map(int, input().split())
hour = 0
count = 0
current_status = m

while True:
    hour += 1
    if M - m < T:
        print(-1)
        break
    if current_status + T <= M:
        count += 1
        current_status += T
    else:
        if current_status - R < m:
            current_status = m
        else:
            current_status -= R
    if count == N:
        print(hour)
        break
