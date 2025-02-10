# yoondo=input().strip()
# N=int(input())
# team=[input().strip() for _ in range(N)]
# team_name=team[0]
# max_result=0
# for name in team:
#     test=yoondo+name
#     condition=[0,0,0,0]
#     for i in test:
#         if i=='L':
#             condition[0]+=1
#         elif i=='O':
#             condition[1]+=1
#         elif i=='V':
#             condition[2]+=1
#         elif i =='E':
#             condition[3]+=1
#     result=((condition[0]+condition[1])*(condition[0]+condition[2])*(condition[0]+condition[3])*(condition[1]+condition[2])*(condition[1]+condition[3])*(condition[2]+condition[3]))%100
#     if result>=max_result:
#         max_result=result
#         team_name=min(name,team_name)
# print(team_name)


yeondu = input()
t = int(input())
teams=[input().strip() for _ in range(t)]

ans = ""
teams.sort()
maximum = -1

for i in range(t):
    word = yeondu + teams[i]
    L = word.count('L')
    O = word.count('O')
    V = word.count('V')
    E = word.count('E')
    total = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if total > maximum:
        ans = teams[i]
        maximum = total

print(ans)