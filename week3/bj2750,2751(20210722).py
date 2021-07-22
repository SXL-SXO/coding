#입력받는 개수 받고 개수만큼 입력받아 올림차순정렬
#두 문제 모두 이 코드로 가능
import sys

num=int(sys.stdin.readline())
number=[]

for a in range(num):
    number.append(int(sys.stdin.readline()))   

s_number=sorted(number)

for list in s_number:
    print(list)
