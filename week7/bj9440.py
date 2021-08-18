# 줄로 N 그다음에 n개만큼 숫자를 입력받아 이 수를 모두 사용해서 만들 수 있는 두 개의 수를 더해주는것
# 일반적 상황: N을 입력받아 N만큼 받은 수를 오름차순으로 정렬하고 big small을 바꿔가면서 더해줘 작은 수를 만든다
# 예외 상황: 0이 있어서 0은 처음자리로 갈 수 없으므로 한칸씩 이동해서 계산하는 경우 이때 N이 짝수인지, 0이 짝수개인지 고려해주어야한다

import sys
from collections import deque

while(1):
    number=deque()
    read=sys.stdin.readline().split()
    N=int(read[0])
    if N==0:
        break 
    big=0 #만드는 큰 수 
    small=0 #만드는 작은 수
    zero=0    
    i=0 #짝수개면 i와 j가 같은 수로 같은 자리 수 홀수개면 j가 하나 작음
    j=0
    for _ in range(N):        
        number.append(int(read.pop()))
        if number[-1]==0:
            zero+=1
            number.pop()
    number=sorted(number)
    while(number):
        num=(number.pop())*10**i
        big+=num
        if (number):
            num=(number.pop())*10**i
            small+=num
            j=i+1
        i+=1
    if zero==0:
        print(small+big)
        continue
    SMALL=small//10**(j-1)
    small-=SMALL*10**(j-1)
    small=SMALL*10**(j+(zero+1)//2-1)+small
    BIG=big//10**(i-1)
    big-=BIG*10**(i-1)
    big=BIG*10**(i+zero//2-1)+big    
    print(small+big)
               
