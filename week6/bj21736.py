import sys
sys.setrecursionlimit(10**6)
def check(aa,bb):
    xx=[0,0,1,-1]
    yy=[1,-1,0,0]
    for k in range(4):
        ii=xx[k]+aa
        jj=yy[k]+bb
        if ii==-1 or jj==-1 or ii==N or jj==M:
            continue
        if visit[ii][jj]=='X':
            continue
        if visit[ii][jj]=='O':
            visit[ii][jj]='V'
            check(ii,jj)
        if visit[ii][jj]=='P':
            meet[0]+=1
            visit[ii][jj]='V'
            check(ii,jj)

N,M=sys.stdin.readline().split()
N=int(N)
M=int(M)

visit=[[]*x for x in range(N)]
iam=[]
meet=[0]
people=0

for d in range(N):
    read=sys.stdin.readline()
    for e in range(M):
        visit[d].append(read[0])    
        if visit[d][e]=='I':
            iam.append([d,e])
        if visit[d][e]=='P':
            people+=1
        read=read[1:]
    
x,y=iam.pop()

check(x,y)

if meet[0]==0:
    print('TT')
else:
    print(meet[0])

                    
