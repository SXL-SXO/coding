from collections import deque

N=int(input())
queue=deque([]) #deque는 앞쪽에서 입력 삭제 지원

for i in range(N):
    queue.append(i+1) 

while (len(queue)>1):
    queue.popleft()
    num=queue.popleft()
    queue.append(num)
    
print(queue[0])
