# Method 1 (Use Sorting)

def AnagramCheck(str1, str2):
    if len(str1) != len(str2):
        return False

    x1 = sorted(str1)
    x2 = sorted(str2)

    for i in range(0, len(str1)):
        if x1[i] != x2[i]:
            return False

    return True

str1 = "test"
str2 = "ttew"
if AnagramCheck(str1, str2) == True:
    print("yes")
else:
    print('No')


# Bit Manipulation (XOR)

# def AnagramCheck(str1, str2):
#     if(len(str1) != len(str2)):
#         return False
#
#     value = 0
#
#     for i in range(0, len(str1)):
#         value = value ^ ord(str1[i])
#         value = value ^ ord(str2[i])
#
#     return value == 0
#
# str1 = "qwertyuiop"
# str2 = "poiuytqwr"
# if(AnagramCheck(str1, str2)):
#     print('Yes')
# else:
#     print('No')