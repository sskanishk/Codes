"""

USe stack to check whether or not a string has balanced usage of pararnthesis

(), ()(), (({[]}))  -> correct
)), ()), ({){[)]}), [][]]] ==> incorrecrt or imbalance


"""

from Stack_Operation import Stack


def is_matching(p1, p2):
    if p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False


def is_paranthesis_balanced(par_string):
    # stack object is called from another file named as Stack_Operations
    # to usse is_empty, pop like functions
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(par_string) and is_balanced:
        pararnthesis = par_string[index]

        if pararnthesis in '{[(':
            s.push(pararnthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_matching(top, pararnthesis):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


x = "()(){(){[]}}"
print(is_paranthesis_balanced(x))