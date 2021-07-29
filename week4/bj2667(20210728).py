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
    

#타임오버
'''
def turn(by,num,N):
    by_change=by
    if num!=N:
        beayeol_c_1=[]
        beayeol_c_2=[]
        beayeol_c_3=[]
        beayeol_r_1=[]
        beayeol_r_2=[]
        beayeol_r_3=[]
        for i in range(2**num*2**num): #[a,b]로 추가할려고 했으나 배열 속 배열검색법을 몰라서 이렇게 함
            beayeol_r_1.append(by[0][i])
            beayeol_c_1.append(by[1][i]+2**num)
            beayeol_r_2.append(by[0][i]+2**num)
            beayeol_c_2.append(by[1][i])
            beayeol_r_3.append(by[0][i]+2**num)
            beayeol_c_3.append(by[1][i]+2**num)
        #beayeol=[2**num+x for x in by[x]]도 가능
        by[0]=by[0]+beayeol_r_1+beayeol_r_2+beayeol_r_3
        by[1]=by[1]+beayeol_c_1+beayeol_c_2+beayeol_c_3
        turn(by,num+1,N)

import sys

N, r, c=sys.stdin.readline().split()
N=int(N)
r=int(r)
c=int(c)

by=[[0,0,1,1],[0,1,0,1]]

turn(by,1,N)

for a in range(len(by[0])):
    if by[0][a]==r and by[1][a]==c:
        where=a
        break

print(where)
'''
