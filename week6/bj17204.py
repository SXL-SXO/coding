import sys
sys.setrecursionlimit(10**6)

N,K=sys.stdin.readline().split()
N=int(N)
K=int(K)

num=[]
next_num=0
turn=0

for a in range(N):
    read=sys.stdin.readline()
    num.append(int(read))

while(1):
    turn+=1
    next_num=num[next_num]
    if next_num==K:
        print(turn)
        break
    if turn==N:
        print(-1)
        break       
