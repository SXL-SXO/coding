#카카오채용연계 2021 거리두기문제
#테스트3번에서 오류가 남 POP로 대각선이 아닌 방향으로 앉는 경우를 고려하지 못했음.
from collections import deque
def check(where):
    meeting=[[]*x for x in range(5)]
    poss=1
    inter=deque()
    for a in range(5):
        no_mean=where[a]        
        for b in range(5):
            if no_mean[0]=='P':
                inter.append([a,b])
            meeting[a].append(no_mean[0])
            no_mean=no_mean[1:]
    x_next=[0,0,1,-1,1,1,-1,-1,]
    y_next=[1,-1,0,0,1,-1,1,-1]
    while(inter):
        m,n=inter.pop()
        for i in range(12):
            if poss==0:
                break
            if  m+x_next[i]<0 or m+x_next[i]>4 or n+y_next[i]<0 or n+y_next[i]>4:
                    continue
            if meeting[m+x_next[i]][n+y_next[i]]=='P':       
                if i<4:
                    poss=0
                    break
                if i>3 and i<8:
                    if meeting[m+x_next[i]][n]!='X' or meeting[m][n+y_next[i]]!='X':
                        poss=0
                        break
                if i>7 and i<10:
                    if meeting[m][n+y_next[i]//2]!='X':
                        poss=0
                        break
                if i>9:
                    if meeting[m+x_next[i]//2][n]!='X':
                        poss=0
                        break
        '''
        for i in range(8):
            if  m+x_next[i]==-1 or m+x_next[i]==5 or n+y_next[i]==-1 or n+y_next[i]==5: 
                    continue
            if i<4 and meeting[m+x_next[i]][n+y_next[i]]=='P': #거리가 한 칸인 경우
                poss=0
                break
            if i>3 and meeting[m+x_next[i]][n+y_next[i]]=='P': #거리가 두 칸인 경우
                if meeting[m+x_next[i]][n]!='X' or meeting[m][n+y_next[i]]!='X':
                    poss=0
                    break
        '''
    return poss
def solution(places):
    answer = []    
    for k in range(5):
        check_place=places[k]
        result=check(check_place)
        answer.append(result)
    return answer
