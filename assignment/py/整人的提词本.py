def decompile(string: str):
    string = '((' + string + '))'
    stack = []
    for char in string:
        if char == ')':
            temp = []
            while 1:
                try:
                    x = stack.pop()
                    if x == '(':
                        raise EOFError
                    else:
                        temp.append(x)
                except EOFError:
                    break
            stack += temp
        else:
            stack.append(char)
    return ''.join(stack)
print(decompile(input()))