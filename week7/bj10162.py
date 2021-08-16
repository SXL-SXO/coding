import sys

T=sys.stdin.readline()
T=int(T)

button=[300,60,10]
push=[0,0,0]

for i in range(3):
    while(1):
        if T-button[i]<0:
            break
        else:
            push[i]+=1
            T-=button[i]
            
    print(T)

if T==0:
    print(push[0],push[1],push[2])

else:
    print(-1)