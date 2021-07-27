ment=2

def dfs_apt(N,a,b):
    global ment
    if b==0:#예외인 경우:a=0 위로 갈 수 없음 a=N-1 밑으로 갈 수 없음 b=0 전으로 갈 수 없음 b=N-1 다음으로 갈 수 없음
        if a==0:
            if apt[a+1][b]==1:
                apt[a+1][b]=ment
                aptment[ment-2][1].append([a+1,b])
                dfs_apt(N,a+1,b)
            if apt[a][b+1]==1:
                apt[a][b+1]=ment
                aptment[ment-2][1].append([a,b+1])
                dfs_apt(N,a,b+1)    
        elif a==N-1:
            if apt[a-1][b]==1:
                apt[a-1][b]=ment
                aptment[ment-2][1].append([a-1,b])
                dfs_apt(N,a-1,b)
            if apt[a][b+1]==1:
                apt[a][b+1]=ment
                aptment[ment-2][1].append([a,b+1])
                dfs_apt(N,a,b+1)
        else:
            if apt[a-1][b]==1:
                apt[a-1][b]=ment
                aptment[ment-2][1].append([a-1,b])
                dfs_apt(N,a-1,b)
            if apt[a+1][b]==1:
                apt[a+1][b]=ment
                aptment[ment-2][1].append([a+1,b])
                dfs_apt(N,a+1,b)
            if apt[a][b+1]==1:
                apt[a][b+1]=ment
                aptment[ment-2][1].append([a,b+1])
                dfs_apt(N,a,b+1)
    elif b==N-1:         
        if a==0:
            if apt[a+1][b]==1:
                apt[a+1][b]=ment
                aptment[ment-2][1].append([a+1,b])
                dfs_apt(N,a+1,b)
            if apt[a][b-1]==1:
                apt[a][b-1]=ment
                aptment[ment-2][1].append([a,b-1])
                dfs_apt(N,a,b-1)
        elif a==N-1:
            if apt[a-1][b]==1:
                apt[a-1][b]=ment
                aptment[ment-2][1].append([a-1,b])
                dfs_apt(N,a-1,b)
            if apt[a][b-1]==1:
                apt[a][b-1]=ment
                aptment[ment-2][1].append([a,b-1])
                dfs_apt(N,a,b-1)
        else:
            if apt[a-1][b]==1:
                apt[a-1][b]=ment
                aptment[ment-2][1].append([a-1,b])
                dfs_apt(N,a-1,b)
            if apt[a+1][b]==1:
                apt[a+1][b]=ment
                aptment[ment-2][1].append([a+1,b])
                dfs_apt(N,a+1,b)
            if apt[a][b-1]==1:
                apt[a][b-1]=ment
                aptment[ment-2][1].append([a,b-1])
                dfs_apt(N,a,b-1)
    else: 
        if a==0:
            if apt[a+1][b]==1:
                apt[a+1][b]=ment
                aptment[ment-2][1].append([a+1,b])
                dfs_apt(N,a+1,b)
            if apt[a][b+1]==1:
                apt[a][b+1]=ment
                aptment[ment-2][1].append([a,b+1])
                dfs_apt(N,a,b+1)
            if apt[a][b-1]==1:
                apt[a][b-1]=ment
                aptment[ment-2][1].append([a,b-1])
                dfs_apt(N,a,b-1)                
        elif a==N-1:
            if apt[a-1][b]==1:
                apt[a-1][b]=ment
                aptment[ment-2][1].append([a-1,b])
                dfs_apt(N,a-1,b)
            if apt[a][b+1]==1:
                apt[a][b+1]=ment
                aptment[ment-2][1].append([a,b+1])
                dfs_apt(N,a,b+1)
            if apt[a][b-1]==1:
                apt[a][b-1]=ment
                aptment[ment-2][1].append([a,b-1])
                dfs_apt(N,a,b-1)
        else:
            if apt[a-1][b]==1:
                apt[a-1][b]=ment
                aptment[ment-2][1].append([a-1,b])
                dfs_apt(N,a-1,b)
            if apt[a][b+1]==1:
                apt[a][b+1]=ment
                aptment[ment-2][1].append([a,b+1])
                dfs_apt(N,a,b+1)
            if apt[a+1][b]==1:
                apt[a+1][b]=ment
                aptment[ment-2][1].append([a+1,b])
                dfs_apt(N,a+1,b)
            if apt[a][b-1]==1:
                apt[a][b-1]=ment
                aptment[ment-2][1].append([a,b-1])
                dfs_apt(N,a,b-1)
import sys

N=(sys.stdin.readline())
N=int(N)

apt=[]
aptment=[]
leng=[]

for a in range(N):
    apt__=sys.stdin.readline()
    apt.append([])
    for b in range(N):
        apt[a].append(int(apt__[b]))
       
for i in range(N):
    for j in range(N):
        if apt[i][j]==1:
            aptment.append([ment,[[i,j]]])
            apt[i][j]=ment
            dfs_apt(N,i,j)
            ment+=1

for list in aptment:
    leng.append(len(list[1]))

leng.sort()
            
print(ment-2)

for list in leng:
    print(list)
