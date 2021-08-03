import sys

N=sys.stdin.readline()
N=int(N)

turn=1
name=666  
 
while(1):
    if N==turn:
        print(name)
        break
    name+=1        
    num=name
    succes=0
    while(num>0):
        if num%10==6:
            succes+=1            
            if succes==3:
                succes=0
                turn+=1
                break
        elif succes>0:
            succes=0
        num=num//10 
