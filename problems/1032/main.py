# import sys
# sys.stdin = open('/Users/chulhwanjang/boj/practice.txt','r')

N = int(input())
first_word = list(input())

for i in range(N - 1):
    other_word = input()
    for j in range(len(first_word)):
        if first_word[j] != other_word[j]:
            first_word[j] = '?'
        else:
            pass
print(''.join(first_word))
