#백준 9012번 ()의 짝지가 맞으면 yes 틀리면 no 반환
import sys
input=sys.stdin.readline

indata=int(input())

for k in range(indata):
    a=input()    
    passpass=[]
    for i in range(len(a)):
        if a[i]=='(':
            passpass.append(a[i])
        elif a[i]==')':
            if len(passpass)!=0:
                if passpass[-1]=='(':
                    del passpass[-1]
                else:
                    break
            else:
                passpass.append(0)
                break
                
    if (not passpass):
        print('YES')
    else:
        print('NO')
