#브르투포스 실행 블랙잭 변형 N,M을 입력받아서 N만큼의 카드를 입력받고 카드 중 3개를 뽑았을때의 합이 M보다 작거나 같고 가장 근접한 수 출력
#내 수준에서도 간단하게 끝내기 가능한 기본
import sys

N,M=sys.stdin.readline().split()

N=int(N)
M=int(M)

card=sys.stdin.readline().split()

for a in range(N):
	card[a]=int(card[a])

most=0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if card[i]+card[j]+card[k]>most and card[i]+card[j]+card[k]<=M:
                most=card[i]+card[j]+card[k]
				
print(most)
