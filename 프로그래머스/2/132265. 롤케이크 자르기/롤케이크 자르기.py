def solution(topping):
    #갯수 상관없이 토핑의 갯수가 공평해야함
    #공평하게 나눌수 없다면 0 리턴
    answer = 0
    a={}
    b={}
    
    #첫번째 총 갯수를 dict으로 만듬
    for i in topping:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    #두번째 첫번째를 하나씩 없애면서 dict 갯수 비교 answer+1
    for i in topping:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
        a[i]-=1
        if a[i]==0:
            del a[i]
        if len(a)==len(b):
            answer+=1
    
    
    
    return answer