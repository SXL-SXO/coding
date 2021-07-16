import sys
input=sys.stdin.readline

indata=int(input()) #입력받는데이터개수

for k in range(indata): #데이터개수만큼실핼
    a=input() #데이터입력
    passpass=[] #빈스텍만들기
    for i in range(len(a)):
        if a[i]=='(':
            passpass.append(a[i]) #(면passpass에 젤 뒤에 넣기
        elif a[i]==')':
            if len(passpass)!=0:
                if passpass[-1]=='(': #)면 passpass에 젤 뒤가 (면 젤 뒤에꺼 지우기
                    del passpass[-1]
                else:
                    passpass.append(0)
                    break #없으면 짝꿍이 없는거니까 종료
            else:
                passpass.append(0)
                break #없으묜 짝꿍없는거니까 종료
                
    if (not passpass):
        print('YES') #비어있으면 내가 0 안추가한거니까 맞음
    else:
        print('NO')
