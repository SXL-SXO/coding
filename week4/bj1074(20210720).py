#z형식으로 순서대로 좌표를 훑고갈 때, 특정좌표의 순서 구하기

import sys
import time

def turn(first_r,first_c,num,result):
    global r,c
    if num==0:
        if first_r+2**num==r:
            if first_c+2**num==c:
                print(result-1)
            else:
                print(result-2)
        else:
            if first_c+2**num==c:
                print(result-3)
            else:
                print(result-4)
                
    else:
        if first_r+2**num > r:
            if first_c+2**num > c:
                turn(first_r,first_c,num-1,result-2**num*2**num-2**num*2**num-2**num*2**num)
            else:
                turn(first_r,first_c+2**num,num-1,result-2**num*2**num-2**num*2**num)
        else: 
            if first_c+2**num > c:
                turn(first_r+2**num,first_c,num-1,result-2**num*2**num)
            else:
                turn(first_r+2**num,first_c+2**num,num-1,result)

N, r, c=sys.stdin.readline().split()
#start = time.time()
N=int(N)
r=int(r)
c=int(c)

turn(0,0,N-1,2**N*2**N)
#print("time :", time.time() - start)
