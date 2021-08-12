import sys
import copy
sys.setrecursionlimit(10**6)
def check(aa,bb):
    xx=[0,0,1,-1]
    yy=[1,-1,0,0]
    for k in range(4):
        ii=xx[k]+aa
        jj=yy[k]+bb
        if ii==-1 or jj==-1 or ii==N or jj==N:
            continue
        if visit[ii][jj]>0:
            visit[ii][jj]=-1
            check(ii,jj)

N=sys.stdin.readline()
N=int(N)

long_where=0
live=0
where=[]

for d in range(N):
    where.append(list(map(int,sys.stdin.readline().split())))
    this=max(where[d])
    if long_where<this:
        long_where=this
        
if long_where>101:
    long_where=101
           
for c in range(long_where+1):   
    live_now=0
    for x in range(N):
        for y in range(N):
            if where[x][y]==c:
                where[x][y]=0
    visit=copy.deepcopy(where)
    for i in range(N):
        for j in range(N):
            if visit[i][j]>0:
                check(i,j)
                live_now+=1    
    if live_now>live:
        live=live_now
                    
print(live)                