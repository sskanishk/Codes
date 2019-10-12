# # x = int(input())
# #
# # for i in range(x):
# #     numbers = list(map(int, input().split()))
# #     while(number[0] >= numbers[1]):
# #         y =
#
# h = [2, 300, 4, 5, 6, 7]
# print(sum(h))
# #
# # print(22%3)
# #
# #
# print(sorted(h))
#
#
# A simple Python3 program
# to calculate Euler's
# Totient Function

# Function to return
# gcd of a and b

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

# for n in range(1, 11):
#     print("phi(", n, ") = ",
#           phi(n), sep="")

x = int(input())
for i in range(x):
    phi(int(input()))





















































































































































































# z = input()
# for i in z:
#     print(z[i:i+3])

# x = int(input())
# y = []
# for i in range(x):
#     y.append(int(input()))
#
# for i in range(x):
#     if y[i] < 9:
#         print(-1)
#     else:
#         count = 0
#         while(y[i] % 10 == 9):
#             y[i] = y[i] - 9
#             count += 1
#         print(count)

# x = int(input())
# y = []
# for i in range(x):
#     y.append(int(input()))
#
# for i in range(x):
#     if y[i] > 9:
#         temp = 10 - (y[i]%10)
#         if (y[i]-(temp * 9) >= 0):
#             print(temp)
#         else:
#             print(-1)
#     else:
#         print(-1)

# n = int(input())
# x = int(input())
# y = [1, 2, 1, 1, 1]
# for i in range(n):
#     y.append(int(x%10))
#     x = int(x/10)
# y.reverse()
# s =[]
# t = []
# for i in range(10):
#     s.append(y.count(i))
# for i in range(10):
#     if(s[i]%2 == 1):
#         t.append(y.index(i))
# print(max(t) - min(t))

# y = [1, 2, 1, 1, 1]
# s =[]
# t = []
# for i in range(10):
#     s.append(y.count(i))
#
# for i in range(10):
#     if(s[i]%2 == 1):
#         t.append(y.index(i))
#
# print(s)
# print(t)
# print(0%2)
# print(4%2)
# print(1%2)




# n=int(input())
# for _ in range (n):
#     x=int(input())
#     if(x<9):
#         print(-1)
#     else:
#         p=x%10
#         l=10-p
#         if(x-(l*9)>=0):
#             print(l)
#         else:
#             print(-1)


# print(27%9)
# 0
# print(28%9)
# 1
# print(209%9)
# 2
# print(209//9)
# 23

# T = int(input())
# N = []
# K = []
# temp = []
# f = []
# for i in range(T):
#     N = list(map(int, input().split()))
#     K = list(map(int,input().strip().split()))[:N[0]]
#     for i in range(len(K)):
#         if K[i] % N[1] == 0:
#             temp.append(K[i]*N[1])
#         elif K[i] % N[1] != 0:
#             temp.append(K[i] // N[1])
#     f.append(max(temp) - min(temp))
#     # print(temp)
#     # temp.clear()
# print(*f, sep = "\n")

# for i in range(T):
#     for i in range(len(K)):
#         if K[i] % N[1] == 0:
#             temp.append(K[i]*N[1])
#         elif K[i] % N[1] != 0:
#             temp.append(K[i] // N[1])
#     print(max(temp) - min(temp))
#     print(temp)
#     temp.clear()



# string = input()
# for i in range(len(string)):asdfghjkl
#     print(string[i:i+3])

# string = input()
# y = []
# for i in range(len(string)):
#     y.append(string[i:i+3])
#
# print(y[0:len(string)-2])

# string = input()
# y = []
# x = []
# for i in range(len(string)):
#     y.append(string[i:i+3])
#
# x = y[0:len(string)-2]
#
#
# count = 0
# if 'aaa' in x:
#     count += 1
# elif 'aba' in x:
#     count += 1
# elif 'bab' in x:
#     count += 2
#
# print(count)





# x = int(input())
# y = []
# for i in range(x):
#     y.append(int(input())
#
#
# for i in range(x):
#     if(y[i] % 10 == 9):
#         print(9)
#     elif(y[i] % 2 == 0):
#         print(y[i] // 9)
#     else:
#         print(-1)

# print(27%9)
# print(27//9)

# x = int(input())
# y = []
# for i in range(x):
#     y.append(int(input()))
#
# print(y)

# x = int(input())
# y = []
# for i in range(x):
#     y.append(int(input()))
#
# for i in range(x):
#     if(y[i]%10 == 9):
#         print(1)
#     elif(y[i]%2 == 0):
#         print(y[i] // 9)
#     else:
#         print(-1)





# for i in range()






# l = []
# t = int(input())
# for i in range(t):
#     l.append(int(input()))
#
# p =[]
# for num in range(251):
#    # prime numbers are greater than 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            p.append(num)
# f=[]
# for i in range(l[i]):
#     for i in range():
#         f.append(p[i+1] - p[i])
#     print(*f)

# class SinglyLinkedList:
#     def __init__(self):
#         self.data = []
#
# def insert_node(self, val):
#     self.data.append(val)
#
#     def printLinkedList(self):
#         print(self.data)



# def printLinkedList(head):
#     for i in range(len(llist)):
#         print(temp.data, sep = " ")
#         temp = temp.next
#
#
# if __name__ == '__main__':
#     llist_count = int(input())
#
#     llist = SinglyLinkedList()
#
#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)
#
#     printLinkedList(llist.head)











