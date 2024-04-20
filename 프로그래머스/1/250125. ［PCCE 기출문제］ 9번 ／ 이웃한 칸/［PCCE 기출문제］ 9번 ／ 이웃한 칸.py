def solution(board, h, w):
    # board 는 색깔표
    # h,w는 좌표
    # 좌표를 기준으로 상하좌우에 이웃하는 보드와 같은색 + 하여 return
    count=0
    #상하는 h 
    #좌우는 w 
    # index 넘어가지 않도록 할것!! (for 문으로 a[-1,1] 확인한 결과 런타임 에러 발생)
    color=board[h][w]
    
    if w+1<=(len(board)-1) and board[h][w+1]==color:
        count+=1
    if w-1>=0 and board[h][w-1]==color:
        count+=1
    if h+1<=(len(board)-1) and board[h+1][w]==color:
        count+=1
    if h-1>=0 and board[h-1][w]==color:
        count+=1
            
    
    answer = count
    return answer