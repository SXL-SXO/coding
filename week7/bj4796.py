import sys
i=0
while(1):
    i+=1
    L,P,V=map(int,sys.stdin.readline().split())
    if L==0 and P==0 and V==0:
        break
    poss=V//P*L
    if V%P>L:
        print('Case %d: %d'%(i,poss+L))
        continue
    print('Case %d: %d'%(i,poss+V%P))
    