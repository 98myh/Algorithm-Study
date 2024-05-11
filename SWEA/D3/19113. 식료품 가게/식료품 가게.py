# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    '''
    철수는 25% 할인된 가격으로 판매 => 물건은 정상가격의 75%이다 3/4 => 원가로 되려면 4/3 곱해주면 됨
    모든 물건의 정상가는 4의 배수 정수 => 할인된 가격도 정수
    모든 판매 물품의 할인된 판매가격+정상가격 프린터 출력

    어느 가격표가 할인 가격표인지 구분

    첫번째 입력 상점의 품목 수
    두번째 프린터 인쇄한 2n개의 정수
    '''
    #첫번째 입력
    sale_num=int(input())
    
    #두번째 입력
    printer=list(map(int,input().split()))

    result=[]
    
    i=0
    while True:
        if printer[i]*4//3 in printer:
            result.append(printer[i])
            printer.remove(printer[i]*4//3)
       	if len(result)==sale_num:
            break
        i+=1
        
    
   
    f=' '.join(map(str,result))
    print("#"+str(test_case)+" "+f)
    
