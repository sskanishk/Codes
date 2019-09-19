# Given three strings A, B and C.
# Write a function that checks whether C is an interleaving of A and B.
# C is said to be interleaving of A and B,
# if it contains all characters of A and B and order of all characters
# in individual strings is preserved.

# incase of small and big letter use .lower(), .upper()

def interleaving(str, str1, str2):
    if len(str) != (len(str1)+len(str2)):
        return False


    x1 = sorted(str.lower())
    str3 = str1 + str2
    x2 = sorted(str3)

    for i in range(len(str)):
        if x1[i] != x2[i]:
            return False

    return True

str = "APPLEball"
str1 = "apple"
str2 = "ball"

if(interleaving(str, str1, str2)):
    print("Yes")
else:
    print('No')