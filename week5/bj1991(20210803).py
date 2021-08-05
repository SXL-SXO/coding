#A부터 연결된 값을 입력받아 전 중 후 출력?
#알파벳이라서 생각보다 쉽게 풀었으나 답 참고함
import sys

def PRE(thing1):
    preo.append(thing1[0])
    if ord(thing1[1])!=46:
        PRE(tree[ord(thing1[1])-65])       
    if ord(thing1[2])!=46:
        PRE(tree[ord(thing1[2])-65])
        
def IN(thing2):
    if ord(thing2[1])!=46:
        IN(tree[ord(thing2[1])-65])
        ino.append(thing2[0])
        if ord(thing2[2])!=46:
            IN(tree[ord(thing2[2])-65])
    elif ord(thing2[2])!=46:
        ino.append(thing2[0])
        IN(tree[ord(thing2[2])-65])
    else:
        ino.append(thing2[0])
        
def POST(thing3):
    if ord(thing3[1])!=46:
        POST(tree[ord(thing3[1])-65])
    if ord(thing3[2])!=46:
        POST(tree[ord(thing3[2])-65])
    posto.append(thing3[0])

N=sys.stdin.readline()
N=int(N)

tree=[]
preo=[]
ino=[]
posto=[]

tree=[[chr(x+65)] for x in range(26)]

for _ in range(N):
    read=sys.stdin.readline().split()
    tree[ord(read[0])-65].append(read[1])
    tree[ord(read[0])-65].append(read[2])

PRE(tree[0])
IN(tree[0])
POST(tree[0]) 
 
print(''.join(str(a) for a in preo))
print(''.join(str(b) for b in ino))
print(''.join(str(c) for c in posto))
