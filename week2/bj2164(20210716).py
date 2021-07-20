#백준 2164번 N장의 카드가 올림차순으로 놓여있다 첫번째카드는 버리고 두번째카드는 제일 뒤로 보낸다. 그리고 이를 반복한다. 마지막에 남는 카드는?

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
