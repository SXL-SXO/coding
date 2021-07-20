#백준 2504번 ()[]를 입력받아 각 규칙에 맞게 값 구하기

#아직 못품,,

import sys
input=sys.stdin.readline

f_code=input()
passpass=[]
devresult=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dev=0 #check
devplus=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def what_thing(a):
    global dev
    for i in range(len(a)):
        if a[i]=='[' or a[i]=='(':
            passpass.append(a[i])
            if (i-1>=0) and ((a[i-1]==')') or (a[i-1]==']')):
                dev+=1
            devplus[dev]+=1    
        elif a[i]==']':
            if passpass[-1]=='['and(not passpass):
                del passpass[-1]
                if a[i-1]=='[':
                    devresult[dev]=3
                    devplus[dev]-=1
                else:
                    devplus[dev]-=1
                    if devplus[dev]<0:
                        for j in range(dev):
                            if devresult[dev-(j+1)]!=0:
                                devresult[dev]+=devresult[dev-(j+1)]
                                devresult[dev-(j+1)]=0
                                break                                                                   
                    devresult[dev]*=3
            else:
                print(0)
                break
                
        elif a[i]==')':
            if passpass[-1]=='('and(not passpass):
                del passpass[-1]
                if a[i-1]=='(':                   
                    devplus[dev]-=1
                    devresult[dev]=2
                else :
                    devplus[dev]-=1
                    if devplus[dev]<0:
                        for j in range(dev):
                            if devresult[dev-(j+1)]!=0:
                                devresult[dev]+=devresult[dev-(j+1)]
                                devresult[dev-(j+1)]=0
                                break                                                                    
                    devresult[dev]*=2
            else:
                print(0)
                break
                
    if (not passpass):
        for j in range(dev):
            if devresult[dev-(j+1)]!=0:
               devresult[dev]+=devresult[dev-(j+1)]
               devresult[dev-(j+1)]=0
        print(devresult[dev])

        
        
what_thing(f_code)
