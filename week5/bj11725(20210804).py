#연결된 노드를 N-1만큼 입력받아 1이 루트라고 했을때 2, 3, 4.. 의 부모노드 출력하기
#큐를 사용하는 방법으로 답을 참고함 아마 이게 깊이우선, 너비우선 탐색을 할때 재귀를 반복하지않고 푸는 법인듯
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
