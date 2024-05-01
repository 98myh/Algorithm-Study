def solution(t, p):
    answer = 0
    #t에서 p길이만큼 수를 짤랐을때 p보다 작거나 같은 수 카운트
    p_len=len(p)
    
    for i in range(len(t)-p_len+1):
        if i+p_len<=len(t):
            part=t[i:i+p_len]
        if int(part)<=int(p):
            answer+=1
    
    return answer