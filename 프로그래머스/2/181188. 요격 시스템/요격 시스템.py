def solution(targets):
    #x좌표 범위 나타냄 [시작,끝]
    #시작과 끝사이 발사하여 요격 가능
    #최소한으로 모든 미사일을 요격해야함
    
    answer=0
    
    #끝 순서대로 정렬해줌
    targets.sort(key = lambda x:x[1])
    
    start=0
    for i in targets:
        #만약 최솟값이 start보다 크다면 answer+1 , start=i[1]
        if i[0]>=start:
            answer+=1
            start=i[1]
    
    return answer