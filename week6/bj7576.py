import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)
        
def change(b,a):
    tomato[a][b]=1
    after.append(b)
    after.append(a)
    good[0]-=1
    return 0

M,N=map(int,sys.stdin.readline().split())

before=deque()
tomato=[]
after=deque()
good=[N*M]
change_s=[]
day=0

for i in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))
    for j in range(M):
        if tomato[i][j]==1:
            good[0]-=1
            before.append(j)
            before.append(i)
        elif tomato[i][j]==-1:
            good[0]-=1
            
while(1):
    if day!=0:
        before=copy.deepcopy(after)        
    after.clear()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]    
    while before:
        change_s.clear()
        change_s.append(before.popleft())
        change_s.append(before.popleft())        
        for i in range(4):
            next_x=change_s[0]+dx[i]
            next_y=change_s[1]+dy[i]
            if next_x==-1 or next_y==-1 or next_x==M or next_y==N:
                continue
            if tomato[next_y][next_x]==0:
                change(next_x,next_y) 
    if after:
        day+=1        
        continue
    if good[0]==0:
        print(day)
        break
    print(-1)
    break
       