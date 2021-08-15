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
        for i in range(8):
            if  m+x_next[i]==-1 or m+x_next[i]==5 or n+y_next[i]==-1 or n+y_next[i]==5:
                    continue
            if i<4 and meeting[m+x_next[i]][n+y_next[i]]=='P':
                poss=0
                break
            if i>3 and meeting[m+x_next[i]][n+y_next[i]]=='P':
                if meeting[m+x_next[i]][n]!='X' or meeting[m][n+y_next[i]]!='X':
                    poss=0
                    break
    return poss
def solution(places):
    answer = []    
    for k in range(5):
        check_place=places[k]
        result=check(check_place)
        answer.append(result)
    return answer