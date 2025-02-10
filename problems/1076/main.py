color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
color_list = [input().strip() for _ in range(3)]
first_num = int(str(color.index(color_list[0])) + str(color.index(color_list[1])))
second_num = 10 ** color.index(color_list[2])
print(first_num*second_num)
