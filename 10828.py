import sys
stack=[]
num=int(input())
for _ in range(num):
    what_do=str(sys.stdin.readline().split())
    do_what=what_do[0]
    if do_what=='push':
        what=what_do[1]
        stack.append(int(what))
    elif do_what=='pop':
        if len(stack)==0:
            print(-1)
        else:
            stack.pop()
    elif do_what=='size':
        print(len(stack))
    elif do_what=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif do_what=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
