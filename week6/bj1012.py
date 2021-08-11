import sys
import copy
from collections import deque

def visit_check(a,b):
    x1=[0,0,1,-1]
    y1=[1,-1,0,0]
    for i in range(4):        
        next_x=a+x1[i]
        next_y=b+y1[i]
        if next_x==-1 or next_x==w or next_y==-1 or next_y==h:
            continue
        for c in range(len(bea)):
            if bea[c][0]==next_x and bea[c][1]==next_y:
                del bea[c]
                visit_check(next_x,next_y)
                break


case=sys.stdin.readline()
case=int(case)
bea=deque()


while (1):
    w,h,k=map(int,sys.stdin.readline().split())
    bea.clear()
    case-=1
    bug=0
    for c in range(k):
        w1,h1=sys.stdin.readline().split()
        w1=int(w1)
        h1=int(h1)
        bea.append([w1,h1])
        
    while bea:
        x,y=bea.popleft()
        visit_check(x,y)
                       
        bug+=1
            
    print(bug)
    
    if case==0:
        break