num=int(input())
suja=input()

munja=[]

H=0

for i in range(num):
    munja.append(ord(suja[i])-96)
    if munja[i]:
        H+=munja[i]*(31**i)
        
H%=1234567891    
print(H)