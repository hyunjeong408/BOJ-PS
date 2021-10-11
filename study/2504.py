exp = input()
stack = []
openstr = '(['
fg = True
for s in exp:
    if s in openstr:
        stack.append(s)
    elif s == ')':
        if not stack:
            fg = False
            break
        elif stack[-1] == '(':
            stack.pop()
            stack.append(2)
        elif (stack[-1] == '[') or (stack[-1] == ']'):
            fg = False
            break
        else:
            tmp = 0
            while type(stack[-1]) == type(1):
                tmp += stack.pop()
                if not stack:
                    break;
            if not stack:
                fg = False
                break
            elif stack[-1] == '(':
                stack.pop()
                stack.append(tmp*2)
            else:
                fg = False
                break
    elif s == ']':
        if not stack:
            fg = False
            break
        elif stack[-1] == '[':
            stack.pop()
            stack.append(3)
        elif (stack[-1] == '(') or (stack[-1] == ')'):
            fg = False
            break
        else:
            tmp = 0
            while type(stack[-1]) == type(1):
                tmp += stack.pop()
                if not stack:
                    break;
            if not stack:
                fg = False
                break
            elif stack[-1] == '[':
                stack.pop()
                stack.append(tmp*3)
            else:
                fg = False
                break
    else:
        fg = False
        break

if stack:
    for i in stack:
        if type(i) != type(1):
            fg = False
            break

if fg:
    ans = 0
    for i in stack:
        ans += i
    print(ans)
else:
    print(0)
    exit()