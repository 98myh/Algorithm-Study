import math

def solution(arrayA, arrayB):
    #A 최대 공약수 B 최대 공약수 구한다
    #A 최대 공약수로 B의 모든 요소 나누었을때 나누어지지 않는다면 return A 최대공약수
    #B 최대 공약수로 A의 모든 요소 나누었을때 나누어지지 않는다면 return B 최대공약수
    #아니면 retrun 0
    answer=0
    maxA=arrayA[0]
    maxB=arrayB[0]
    #최대 공약수 구하기
    if len(arrayA)>1:
        for i in range(len(arrayA)-1):
            maxA=math.gcd(maxA,arrayA[i+1])
            maxB=math.gcd(maxB,arrayB[i+1])
            
    #maxA로 B나누었을때 나머지가 있어야함
    a_check=0
    for i in arrayB:
        if i%maxA==0:
            a_check=1
    
    b_check=0
    for i in arrayA:
        if i%maxB==0:
            b_check=1
    
    #결과적으로 check가 0 나와야함 -> 비교해서 return
    if a_check==0 and b_check==0:
        return maxA if maxA>maxB else maxB
    elif a_check==0 and b_check==1:
        return maxA
    elif a_check==1 and b_check==0:
        return maxB
    else:return 0
    return answer
