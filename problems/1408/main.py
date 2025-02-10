# import sys
# sys.stdin = open('/Users/chulhwanjang/boj/practice.txt','r')
end_T = input()
start_T = input()
T_1 = int(start_T[0:2]) * 3600 + int(start_T[3:5]) * 60 + int(start_T[6:8])
T_2 = int(end_T[0:2]) * 3600 + int(end_T[3:5]) * 60 + int(end_T[6:8])
h = m = s = 0
if T_1 >= T_2:
    h = (T_1 - T_2) // 3600
    m = ((T_1 - T_2) % 3600) // 60
    s = ((T_1 - T_2) % 3600) % 60
else:
    T_3 = 24 * 3600 - T_2 + T_1
    h = T_3 // 3600
    m = (T_3 % 3600) // 60
    s = (T_3 % 3600) % 60

print(str(f'{h:02d}:{m:02d}:{s:02d}'))
