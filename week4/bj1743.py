import sys
sys.setrecursionlimit(100000)

def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
      lis = data[res[-1]+1:]
    except:
      break     
  return res
  
def search(num, a):
    if tra_index[a]!=0:
        return 0
    else:
        tra_index[a]=num
        right=list(set(find_index(tra_1,tra_1[a]))&set(find_index(tra_2,tra_2[a]+1)))
        left=list(set(find_index(tra_1,tra_1[a]))&set(find_index(tra_2,tra_2[a]-1)))
        up=list(set(find_index(tra_1,tra_1[a]+1))&set(find_index(tra_2,tra_2[a])))
        down=list(set(find_index(tra_1,tra_1[a]-1))&set(find_index(tra_2,tra_2[a])))

        if right: #오
            tra_index[a]=num
            for r in right:
                search(num, r)
        if left: #왼
            tra_index[a]=num
            for l in left:
                search(num, l)
        if up:#상
            tra_index[a]=num
            for u in up:
                search(num, u)
        if down: #하
            tra_index[a]=num
            for d in down:
                search(num, d)
      

R, C, N = sys.stdin.readline().split()

R=int(R)
C=int(C)
N=int(N)
tra_1=[]
tra_2=[]
tra_index=[]
big=0

for _ in range(N):
    no_m=sys.stdin.readline().split()
    tra_1.append(int(no_m[0]))
    tra_2.append(int(no_m[1]))
    tra_index.append(0)


for a in range(N):
    if tra_index[a]==0:
        search(a+1,a)


for b in range(N):
    if tra_index[b]==b+1:
        if big<tra_index.count(b+1):
            big=tra_index.count(b+1)
       
print(big)	
