# # BIT Land
# # BIT LAND is a unique and beautiful place. It's an awesome Coding hub but recently it's being haunted by a monster named Dumit. Dumit is an evil creature who is hell-bent on destroying the coding culture of BIT Land. The Executive body of BIT Land is forced to cater to his needs in order to save the coding culture of BIT Land. Recently he gave a task and threatened the Executive body if it's not finished in stipulated time.

# Dumit gave a number S of length N. The task is to convert that number into an even number.
# An even number is a  number consisting of digits from 0-9 where the frequency of
# each digit must be a multiple of 2. Number in BIT LAND can start with 0.
# You can remove any number of digits from the original number.
# You have to remove digits in such a manner that you obtain an even string of
# largest length and the difference between the index of first and last digit
# removed should be minimum possible.

# # print the minimum possible difference. In case it's impossible to
# create an even number or If the removal of digits is not required, print -1

# Input:
# The first line of input contains a single integer N, the size of the given number
# The Second line of input contains the number S

# Output:
# print the minimum possible difference if the answer exists, otherwise print -1

# Constraints:
# 1 <= N <= 100000
# 0 <= S[i] <= 9

# Sample Input          Sample Input
# 5                     4
# 12111                 2113
# Sample Output         Sample Output
# 0                     3

# Explanation:
#     First Test Case: you only need to remove digit "2" present at 1st index.
#     Second Test Case: you need to remove digits "2" and "3" to make the number even.


t = int(input())
n = int(input())
temp = []
for i in range(t):
    temp.append(int(n%10))
    n = int(n/10)
temp.reverse()
x = []
for i in range(10):
    x.append(temp.count(i))
y = []
for i in range(10):
    if(x[i]%2 == 1):
        y.append(temp.index(i))
print(max(y) - min(y))