import sys

money=sys.stdin.readline()
money=1000-int(money)
change=[500,100,50,10,5,1]
give=0
 
for j in range(6):
    while(1):
        if money-change[j]<0:
            break
        give+=1
        money-=change[j]
print(give)
    
