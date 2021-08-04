#20210802
최단트리신장?에 도전

#20210803
내가 할 수 있는 기본부터 풀자해서 트리의 가장 기본문제를 풀었다.
노드만 트리를 만들 수 있는지 알았는데 알파벳덕에 배열로도 사용이 가능해서 다행이라고 생각이 든다
알파벳을 아스키코드로 바꿔서 -65해서 0~25까지에 저장하고 출력할때는 문자열로 바꿔서 생각보다 쉽게 풀었다

#20210804
리스트배열이 정수형일때 list=[1,2,3,4] 라면 ''.join(str(a) for a in list) 로 1234로 출력할 수 있다

리스트 속 숫자찾기 방법
1번
test_list = [1, 3, 4, 3, 6, 7]
print("Original list : " + str(test_list))
res_list = list(filter(lambda x: test_list[x] == 3, range(len(test_list))))
print("New indices list : " + str(res_list))

2번
test_list = [1, 3, 4, 3, 6, 7]
print("Original list : " + str(test_list))
res_list = [i for i, value in enumerate(test_list) if value == 3]
print("New indices list : " + str(res_list))
