import sys
from collections import deque

N=sys.stdin.readline()
N=int(N)
price=list(map(int,sys.stdin.readline().split()))
kcal=sys.stdin.readline()
kcal=int(kcal)

total_kcal=kcal
total_money=price[0]
toping=deque()
for _ in range(N):
    read=sys.stdin.readline()
    toping.append(int(read))
    
toping=sorted(toping)

while(1):
    next_kcal=total_kcal+toping.pop()
    next_money=total_money+price[1]

    if total_kcal//total_money>next_kcal//next_money:
        print(total_kcal//total_money)
        break
    if not toping:
        print(next_kcal//next_money)
        break
    
    total_kcal=next_kcal
    total_money=next_money
