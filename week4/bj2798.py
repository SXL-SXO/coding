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