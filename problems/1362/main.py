# senario = []
# while True:
#     list_test = input().split()
#     if list_test == ['0', '0']:
#         break
#     senario.append(list_test)
#
# count = 0
# for i, j in senario:
#     if i.isdecimal() and j.isdecimal():
#         o = int(i)
#         w = int(j)
#         count += 1
#         continue
#
#     if i == '#' and j == '0':
#         if o * 0.5 < w < o * 2:
#             print(f'{count} :-)')
#         elif w == 0:
#             print(f'{count} RIP')
#         else:
#             print(f'{count} :-(')
#         continue
#
#     if i == 'F':
#         w += int(j)
#         w -= int(j)
#     else:
#         pass


count = 0
while True:
    death = 0
    count += 1
    o, w =map(int,input().split())
    if o == 0 and w == 0:
        break
    while True:
        a,b = input().split()
        b = int(b)
        if a == '#' and b == 0:
            break
        if a == 'F':
            w += b
        elif a == 'E':
            w -= b
        if w <= 0 :
            death = 1
    print(count,end=' ')
    if death == 1:
        print("RIP")
    else:
        if w > o/2 and w < o*2:
            print(":-)")
        else:
            print(":-(")