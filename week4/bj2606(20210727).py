#컴퓨터갯수와 연결갯수를 입력받아 1번 컴퓨터가 몇개와 연결되어있는지 알아보는 문제
change=0 #연결갯수(여기서는 바이러스감염갯수)
def var(comnum,lin):
    computer[comnum-1][1]=1
    global change
    change+=1
    for list in lin:
        if computer[list-1][1]!=1:
            computer[list-1][0].remove(comnum)
            var(list,computer[list-1][0])
        
import sys

N=sys.stdin.readline()
L=sys.stdin.readline()

N=int(N)
L=int(L)

computer=[]

for i in range(N):
    computer.append([[],0]) #[0]은 연결된 컴퓨터번호가 들어갈 곳, 0은 감염되지 않은 상태를 나타냄

for j in range(L):
    link=sys.stdin.readline().split()
    a=0
    b=0
    #밑의 반복문은 문자열 숫자로 입력받기
    for k in range(len(link[0])):
        a=a+(ord(link[0][k])-48)*(10**(len(link[0])-1-k))
    for e in range(len(link[1])):
        b=b+(ord(link[1][e])-48)*(10**(len(link[1])-1-e))
    computer[a-1][0].append(b)
    computer[b-1][0].append(a)  

var(1,computer[0][0])

print(change-1)

        
