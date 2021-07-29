#N입력받고 N높이를 구한다 앞에거보다 뒤에게 크면 보이니까 간단하다
import sys

N=sys.stdin.readline()
N=int(N)

turopi=[]
for b in range(N):
    turopi.append(sys.stdin.readline())

big_f=int(turopi[0])
big_b=int(turopi[N-1])

look_f=1
look_b=1

for a in range(N):
    turopi[a]=int(turopi[a])
    turopi[N-1-a]=int(turopi[N-1-a])
    if big_f<turopi[a]:
        big_f=turopi[a]
        look_f+=1
    if big_b<turopi[N-1-a]:
        big_b=turopi[N-1-a]
        look_b+=1

print(look_f)
print(look_b)    
