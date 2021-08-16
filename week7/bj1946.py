#입사면접을 봤는데 서류도 면접도 다른 지원자보다 등수가 낮으면 무조건 탈락한다. 이때 최대 합격자는?
#나는 for문을 2번 돌려서 다른사람들과 하나하나 비교하는 방식을 썼더니 시간초과가 떴다. 
#그래서 sort로 [0]의 등수를 순서대로 해서 앞등수보다 뒤에 등수가 [1]도 크면 탈락한다
#이때 1등과 꼴등을 동시에 할 수 있기때문에 best는 N+1에서 시작해야 한다

import sys
from collections import deque

T=sys.stdin.readline()
T=int(T)

for z in range(T):
    N=sys.stdin.readline()
    N=int(N)

    poss=0
    imposs=0

    best=N+1
    sample=[]
    
    for _ in range(N):
        sample.append(list(map(int,sys.stdin.readline().split())))
    
    sample.sort()
    
    for i in range(N):        
        if sample[i][1]<best:
            poss+=1
            best=sample[i][1]
        else:
            imposs+=1
    if poss+imposs==N:
        print(poss)
        
    
