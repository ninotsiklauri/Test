n = str(input("შემოიტანეთ string: "))

def Pairs(open, close):
    if open == '(' and close == ')':
        return True
    return False

def Balanced(A):
    stack = []
    for i in range(len(A)):
        if A[i] == '(':
            stack.append(A[i])
        elif A[i] == ')':
            if Pairs(stack[-1], A[i] or len(stack) != 0):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        print("სწორი მიმდევრობაა")
    else:
        print("არასწორი მიმდევრობაა")

Balanced(n)
