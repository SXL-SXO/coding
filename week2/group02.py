def solution(board, moves):
    answer = 0
    baguni=[]
    
    for list in moves: #움직일 인형 리스트
        number_m=list-1 #인형번호가 1번부터 시작하니까 0부터 시작하게 수정 움직일 행 표현
        for list in board:
            number_b=list[number_m] #행별로 내려가 특정자리
            if number_b: #0이 아닐때 무조건 빼와야하니까
                baguni.append(number_b)
                list[number_m]=0
                if len(baguni)>=2:
                    if baguni[-1]==baguni[-2]: #마지막꺼와 새로 들어오는게 같으면 마지막꺼 pop, answer+2
                        baguni.pop()
                        baguni.pop()
                        answer+=2
                    break
                else:
                    break
    return answer