def is_valid_expression(expression):
    stack = []
    matching_parentheses = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':

            if stack and stack[-1] == matching_parentheses[char]:
                stack.pop()
            else:
                stack.append(char)
        print(stack)
    return len(stack) == 0



bad_expression = "([a+b]{c+d}))"
print(is_valid_expression(bad_expression))