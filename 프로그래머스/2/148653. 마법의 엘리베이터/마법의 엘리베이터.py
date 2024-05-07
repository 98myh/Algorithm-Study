def solution(storey):
    answer = 0
    
    #만약 앞자리 수가 0.5보다 크면 한자리더 큰 수를 뺀다
    while True:
        if round(storey/10**(len(str(storey))),1)>0.5:
            answer+=1
            storey=abs(storey-10**(len(str(storey))))
        else:
            answer+=storey//10**(len(str(storey))-1)
            storey=abs(storey%10**(len(str(storey))-1))
        
        if storey==0:
            break

    return answer