import sys

num=int(sys.stdin.readline())
person=[[0]*2 for i in range(num)]

for a in range(num):
    people=sys.stdin.readline().split()
    person[a][0]=(int(people[0]))
    person[a][1]=(people[1])
    people=[]
    
people=sorted(person, key=lambda x : x[0])

for list in people:
    print(list[0],list[1])

"""for i in range(num): #오름차순 정렬 알고리즘
    for j in range(num-1-i): #2번 실행 12 01 0젤작음 12 1작음
        if person[num-2-j][0]>person[num-1-j][0]: 
            temp_p=person[num-2-j]
            person[num-2-j]=person[num-1-j]
            person[num-1-j]=temp_p
    print(person[i][0],' ',person[i][1]) """