#접근 k만큼 실제로 실행하는 것은 시간이 너무 많이 걸려서 x
#그래서 k가 food_time의 len보다 큰 지 확인하고 그만큼을 빼고 계산할려 했으나 효율성에서 전부 에러
#atlast라는 변수를 두어 적어도 이만큼 있어야한다. 이만큼 없으면 너는 안먹고 skip된다고 생각. 처음 atlast는 0부터 시작
#특정경우, k가 0인 경우 등이 많이 빠져보여서 다시 수정 중
#만약 k가 제일 짧은 시간이 필요한 food*음식가지 수 보다 크다면 그만큼을 빼주고 순서를 고려 음식 3가지 숫자가 1 3 5 k는 7이면 k는 3을 빼도 가능하기때문에 실행 but 성공은 하나임
import sys
def solution(food_times, k):
    start_food=min(food_times)
    foods=len(food_times)
    eat_food=[]
    max_eat=0
    
    max_eat=sum(food_times)
    
    for i in range(foods):
        if food_times[i]>start_food:
            eat_food.append([food_times[i]-start_food,i+1])
    if max_eat<=k:
        return -1

    k-=foods*start_food
    
    while(1):
        foods=len(eat_food)
        start_food=min(eat_food)
        if k<start_food*foods:
            for a in range(start_food):
                if k<(a+1)*foods:
                    k-=a*foods
                    break
                turn+=1                
            return eat_food[k][1]+1  
        new=[]
        for j in range(foods):
            if eat_food[j][0]>start_food:
                new.append([eat_food[j][0]-start_food,eat_food[j][1]])
        
        eat_food=copy.deepcopy(new)
        k-=foods*start_food

a=list(map(int,sys.stdin.readline().split()))
b=map(int,sys.stdin.readline())

solution(a,b)