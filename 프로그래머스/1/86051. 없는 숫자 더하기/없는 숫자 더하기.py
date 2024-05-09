def solution(numbers):
    result=[]
    for i in range(0,10):
        if i not in numbers:
            result.append(i)
    
    answer = sum(result)
    return answer