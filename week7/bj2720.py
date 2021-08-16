import sys

T=sys.stdin.readline()
T=int(T)

for i in range(T):
    money=sys.stdin.readline()
    money=int(money)
    change=[25,10,5,1]
    give=[0,0,0,0]
    
    for j in range(4):
        while(1):
            if money-change[j]<0:
                break
            give[j]+=1
            money-=change[j]
    print(give[0],give[1],give[2],give[3])
    
