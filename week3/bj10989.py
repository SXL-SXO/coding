#입력받는개수 받고 개수만큼 입력받아 올림차순정렬
#2750 2751이랑 같은 줄 알았는데 계속 에러 
import sys
#import time

num=int(sys.stdin.readline())

numarr=[0]*10000
#[[0]*_ for _ in range(10001)] 이거는 2차원 용 안되더라,,,

for i in range(num):
    number=int(sys.stdin.readline())
    numarr[number-1]=numarr[number-1]+1
    
for j in range(10000):
    if numarr[j]:
        for k in range(numarr[j]): # 0이면 실행안되고 종료되는 건 줄 알았는데 안되는 듯
            print(j+1)

'''
#메모리에러라서 메모리 줄일려고 int대신 char 썼는데 타임에러
for a in range(num):
    number=sys.stdin.readline()
    leng=len(number)-2
    numarr[leng]=numarr[leng]+number+" "
#start = time.time()          
for b in range(5):
    if len(numarr[b])>0:  
        for list in sorted(numarr[b].split()):
            print(list)
#print("time :", time.time() - start)'''
