# Assignment_number_1= Linear Data Structures
# Question_number_6 = Write a program to convert prefix expression to infix expression.


def Prefix_To_Infix(prefix):
    stack = []
    i = len(prefix) - 1

    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1     
    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/ABC"
    print(Prefix_To_Infix(str))