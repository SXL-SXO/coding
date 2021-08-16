import sys

order=list(map(int,sys.stdin.readline().split()))
bsd=min(order)
    
b_m=sorted(list(map(int,sys.stdin.readline().split())))
s_m=sorted(list(map(int,sys.stdin.readline().split())))
d_m=sorted(list(map(int,sys.stdin.readline().split())))

set_money=0
not_set=0

for _ in range(bsd):
    set_money+=b_m.pop()+s_m.pop()+d_m.pop()
    
while(b_m):
    not_set+=b_m.pop()
while(s_m):
    not_set+=s_m.pop()
while(d_m):
    not_set+=d_m.pop()
    
print(set_money+not_set)
print(int(set_money*0.9+not_set))