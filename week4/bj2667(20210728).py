#백준 N을 입력받고 0과 1로 이루어진 NxN을 입력해서 2667번 1로 표시된 곳에 연결된 숫자를 세고(긱 단지) 연결된 숫자의 개수(단지 내 세대 수) 개수를 출력 

ment=2 #아파트표식? 0과 1로 표시되어잇으므로 2부터 

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
    apt__=sys.stdin.readline() #문자열 입력
    apt.append([]) #2차원으로 만들기위해 추가
    for b in range(N):
        apt[a].append(int(apt__[b])) #2차원 배열로 만듦
       
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
