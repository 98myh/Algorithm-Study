def solution(players, callings):
    #players 플레이어 순서
    #callings 불리는 순서
    #불리면 앞과 바꿈
    change_index=0
    # 등수 딕셔너리 생성
    rank=[]
    for i in range(0,len(players)):
        rank.append(i)
        
    rank_dict=dict(zip(players,rank))
    
    for i in callings:
        change_rank=0
        # 불리는 인덱스값 찾아냄 -> 시간 초과 에러 딕셔너리로 해결해야함
        # change_index=players.index(i)   
        
        #랭크로 바꿀 인덱스 알아냄
        change_rank=rank_dict[i]
        #불린 유저 순위 올림
        rank_dict[i]-=1
        #앞의 선수 뒤로 보냄
        rank_dict[players[change_rank-1]]+=1
        
        players[change_rank],players[change_rank-1]=players[change_rank-1], players[change_rank]

        
    answer = players
    return answer


