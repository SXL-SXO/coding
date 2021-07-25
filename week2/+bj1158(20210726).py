#숫자 두 개 n,k 입력받아서 1~n 중 k번째 숫자를 계속 꺼내와서 만드는 요세푸스 수열 프린트

import sys

n, k=sys.stdin.readline().split() #n0은 몇번까지 있는지 n1은 몇번째마다 제거할껀지

n=int(n)
k=int(k)

list_=[]
yosa_list=[]

for i in range(n):
    list_.append(i+1)

out=k
o_index=list_.index(out)

while(1):        
    out=list_.pop(o_index) #k번째 값 나와라
    yosa_list.append(str(out))
    o_index=k+o_index-1 #다음으로 k번째 값 나와라    
    if not list_: #비었으면 종료
        break
    while o_index>=len(list_):
        o_index=o_index-len(list_)
        
print("<",", ".join(yosa_list)[:],">", sep='')
#화가나게도 이 프린트때문에 두 번이나 틀렸다,,
