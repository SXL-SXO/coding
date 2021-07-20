#20210721 백준 스택 만들기 문제

import sys
input=sys.stdin.readline
stack=[]
num=int(input())
for _ in range(num):
    do_what=input().split()
    if do_what[0]=='push':
        stack.append(int(do_what[1]))
    elif do_what[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif do_what[0]=='size':
        print(len(stack))
    elif do_what[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif do_what[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
