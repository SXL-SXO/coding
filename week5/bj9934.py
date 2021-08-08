import sys

def visit(start,last,turn):
    middle=(start+last)//2
    if start==last:
        level[turn].append(building[last])
        if turn==K-1:
            return 0
    level[turn].append(building[middle])
    visit(start,middle-1,turn+1)
    visit(middle+1,last,turn+1)

K=sys.stdin.readline()
K=int(K)
   
level=[[]*x for x in range(K)]

building=sys.stdin.readline().split()

for a in range(len(building)):
    building[a]=int(building[a])

visit(0,2**K-2,0)
    
for i in range(K):
    print(' '.join(str(j) for j in level[i]))
