import sys
N=sys.stdin.readline()
N=int(N)

bigger=[]

rank=1
same=1

for a in range(N):
    people=sys.stdin.readline().split()
    people[0]=int(people[0])
    people[1]=int(people[1])
    bigger.append([people[0],people[1]])

#bigger[몸무게, 키, 순서, 나보다 큰사람?]

for i in range(N):
    bigman=0
    for j in range(N):      
        if bigger[i][0]<bigger[j][0] and bigger[i][1]<bigger[j][1]:
            bigman+=1
    bigger[i].append(bigman+1)

for list in bigger:
    print(list[2])