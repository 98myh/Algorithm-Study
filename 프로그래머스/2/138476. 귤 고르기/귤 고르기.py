def solution(k, tangerine):
    fruit={}
    for i in tangerine:
        if i not in fruit:
            fruit[i]=1
        else:
            fruit[i]+=1
    fruit=list(fruit.values())
    fruit.sort()
    
    
    for i in range(len(tangerine)-k):
        fruit[0]-=1
        if fruit[0]==0:
            fruit.pop(0)
        
    answer = len(fruit)
    return answer