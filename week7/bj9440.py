import sys
from collections import deque

while(1):
    number=deque()
    read=sys.stdin.readline().split()
    N=int(read[0])
    if N==0:
        break 
    big=0
    small=0
    zero=0    
    i=0
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
               