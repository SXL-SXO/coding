import sys
from collections import deque
   
N=sys.stdin.readline()
N=int(N)

thing=[[] for x in range(N)]
tree=[[] for x in range(N)]
for _ in range(N-1):
    read=sys.stdin.readline().split()
    thing[int(read[1])-1].append(int(read[0]))
    thing[int(read[0])-1].append(int(read[1]))

son=deque()
son.append(1)

while(1):
    if not son:
        break
    temp=son.popleft()
    while thing[temp-1]:
        nomean=thing[temp-1].pop()
        tree[nomean-1].append(temp)
        son.append(nomean)
        thing[nomean-1].remove(temp)
    
for i in range(1,N):
    print(tree[i][0])