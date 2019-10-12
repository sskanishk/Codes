import itertools
inputx = input()
x = list(inputx)
print(x)
count = 0
for i in range(len(x)):
    if x[i] == '?':
        count += 1

lst = list(itertools.product([0, 1], repeat=count))
print(lst)
print(pow(2,count))

for i in range(len(lst)):
    temp = []
    temp_arr = x.copy()
    q = 0
    for j in range(len(lst[i])):
        temp.append(lst[i][j])
    for k in temp_arr:
        if k == '?':
            ind = temp_arr.index('?')
            temp_arr[ind] = temp[q]
            q+=1
    temp_arr = list(map(str, temp_arr))
    print("".join(temp_arr))

#  ?  ?  ?
#  1/0   1/0  1/0
# 0 0 0
# 0 0 1
# 0 0
# 0 1
# 1 0
# 1 1
# 101?101?01
