num=int(input())
munja=input()

longlength=0

alpha=[[-1]*2 for i in range(26)]

for j in range(num):
    if alpha[ord(munja[j])-97][0]==-1:
        alpha[ord(munja[j])-97][0]=j+1
    elif alpha[ord(munja[j])-97][1]==-1:
        alpha[ord(munja[j])-97][1]=j+1 
    else:
        alpha[ord(munja[j])-97].append(j+1)

for a in alpha:
    if len(a)<2:
        a[0]=-1
            
for k in range(26):
    if alpha[k][0]!=0:
        chae=[]
        bigo=[]
        bigo=[-1+x for x in alpha[k]] #abcd 가 1234 78910 이렇게 반복되면 a는 1 7 b는 2 8 이 저장되므로 b-1로 b= 1 7로 만들어준다
        for l in range(26):
            if k!=l and alpha[l][0]!=-1:
                chae=list(set(bigo)-set(alpha[l])) #중복되는 원소가 있으면 제거한다
                if len(chae)!=len(bigo)+len(alpha[l]): #길이가 같지 않으므로 중복된것이 있었다 그러면 2번이상 반복된거
                    bigo=[]
                    bigo=list(set(alpha[l])-set(chae)) #일치하는것 고로 중복된것
                    #print(alpha[l],chae)
                    #print(bigo)
                    for m in range(len(bigo)):
                        for n in range(len(bigo)-m-1):
                            if alpha[l][alpha[l].index(bigo[m])]-1<num and alpha[l][alpha[l].index(bigo[m+n+1])]-1 and munja[alpha[l][alpha[l].index(bigo[m])]-1]==munja[alpha[l][alpha[l].index(bigo[m+n+1])]-1]: #연속적으로 중복된다
                                justlength=1
                                while(1):
                                    if longlength<justlength:
                                        longlength=justlength
                                    if num>alpha[l][alpha[l].index(bigo[m])]-1+justlength and num>alpha[l][alpha[l].index(bigo[m+n+1])]-1+justlength:
                                        print(munja[alpha[l][alpha[l].index(bigo[m])]+justlength-1],munja[alpha[l][alpha[l].index(bigo[m+n+1])]+justlength-1])                                        
                                        if alpha[l][alpha[l].index(bigo[m])]+justlength-1 == alpha[l][alpha[l].index(bigo[m])]-1 or alpha[l][alpha[l].index(bigo[m+n+1])]+justlength-1==alpha[l][alpha[l].index(bigo[m+n+1])]-1:
                                            break
                                        if munja[alpha[l][alpha[l].index(bigo[m])]+justlength-1]==munja[alpha[l][alpha[l].index(bigo[m+n+1])]+justlength-1]:    
                                            justlength+=1
                                        else:
                                            break
                                    else: 
                                        break
            
print(longlength) #답이 틀린다 왜? asdfasdfasdf이렇게 반복된 문자열은 4~11 모두 동일해서 8을 반환한다. 하지만 asdfasdfasdfasdf의 경우 값은 8이어야해서 너무 어렵다

