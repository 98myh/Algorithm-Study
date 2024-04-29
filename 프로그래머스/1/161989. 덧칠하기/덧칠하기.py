def solution(n, m, section):
    #n미터의 길이가 있는 벽을 한번 칠할때 m만큼 칠한다
    #section에 있는것을 덧칠해야할 경우 덧칠을 다 할 경우 최소한으로 몇번만하면 되는가?
    answer=1
    paint=section[0]
    for i in range(1,len(section)):
        if paint+m<=section[i]:
            answer+=1
            paint=section[i]
        
    
    return answer