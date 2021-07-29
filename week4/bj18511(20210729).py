#N ,K을 입력받고 K만큼(1~3) K로 만들수 있는 N보다 작은 수를 프린트하기
bigx=0
def num(s_kkk,leng,result,n,k,ori): #(정렬된배열, 이 자릿수의 값을 구한다, 최소값, n, k, 제일 작은 것을 만들때 len을 다시쓰기 힘드므로)
    global bigx
    if leng==-1:
        if bigx==0: #안해주면 7234 7 8 9 같은 경우는 값이 7000 999 두가지 값이 출력됨 
            print(result)
            bigx=1
            return 0
        else:
            return 0
    else:
        for i in range(k,0,-1):
            if result+(10**leng)*s_kkk[i-1]<=n: #값이 작으면 더해줌
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


            
