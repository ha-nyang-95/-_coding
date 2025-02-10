N, M = map(int, input().split())
box_num = list(map(int, input().split()))
book_num = list(map(int, input().split()))
print(sum(box_num) - sum(book_num))
