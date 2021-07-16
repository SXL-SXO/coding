#백준 2164 카드는 1~N까지 1이 제일 위에 있다. 첫번째카드는 버리고 두번째카드는 제일 밑으로 둘 때 마지막에 남는 카드 출력

#파이썬에서 큐를 지원하는 것을 알고 답 찾아봄
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

'''1번째 시도-시간초과
N=int(input())
que=[]

for i in range(N):
    que.append(i)
    

for j in range(N-1):
    a=que[1]
    for k in range(N-3-j):
        que[k]=que[k+2] #이부분에서 시간초과 발생한듯 큐를 앞으로 당기기 실패
    if len(que)==3:
        print(que[0])
        break
    else:
        que[-2]=a #당겨졌으므로 뒤 두개 남음 끝에는 2번째꺼 추가
        del que[-1] #남은 배열 제거

2번째 시도-메모리초과
N=int(input())
que=[]

def card(a):
    if len(a)==2:
        print(a[1]) #두개있으면 2번째가 나와야함
    else:
        b=a[1] #두번째꺼 저장해서
        a.append(b) #끝에 추가
        card(a[2:]) #이부분에서 메모리초과 발생한듯 당기기에서 시간초과? 해서 그럼 잘라서 재귀로 해보자 했으나 실패

for i in range(N):
    que.append(i+1) #처음에 숫자리스트만들기
      
card(que)

문제자체의 규칙을 찾아 해결할려고 했으나 찾은듯 못찾은 규칙으로 실패
1시간 20분정도가 지나서 답 찾아봄
'''
