bigx=0
def num(s_kkk,leng,result,n,k,ori):
    global bigx
    if leng==-1:
        if bigx==0:
            print(result)
            bigx=1
            return 0
        else:
            return 0
    else:
        for i in range(k,0,-1):
            if result+(10**leng)*s_kkk[i-1]<=n:
                result+=(10**leng)*s_kkk[i-1]
                break
            if i==1:
                num(s_kkk,ori-1,0,N,K,ori-1)   
    num(s_kkk,leng-1,result,n,k,ori)
import sys
N, K=sys.stdin.readline().split()
kkk=sys.stdin.readline().split()

leng=len(N)
K=int(K)
N=int(N)

for a in range(K):
    kkk[a]=ord(kkk[a])-48
 
s_kkk=sorted(kkk)

num(s_kkk,leng-1,0,N,K,leng-1,)


            