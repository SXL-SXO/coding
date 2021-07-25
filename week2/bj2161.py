#카드2와 동일한 풀이이나 결과값을 달리요구 deque대신 queue사용

N=int(input())
have=[]
back=0

for i in range(N):
    have.append(i+1) 

while (1):
    if not have:
        break
    print(have.pop(0), end=' ')
    if not have:
        break
    back=have.pop(0)
    have.append(back)
    
