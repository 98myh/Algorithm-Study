import heapq
def solution(book_time):
    #방 개수 세기
    answer = 1
    #시작 시간,종료 시간 순으로 정렬
    book_time.sort(key=lambda x:(x[0],x[1]))
    
    #시간을 계산하기 편하게 변경
    for i in range(len(book_time)):
        div=book_time[i][0].split(":")
        div2=book_time[i][1].split(":")
        book_time[i][0]=int(div[0])*60+int(div[1])
        #10분 청소시간+10 
        book_time[i][1]=int(div2[0])*60+int(div2[1])+10
    
    heap=[]        
    for s, e, in book_time:
        if not heap: # 처음일때 삽입
            heapq.heappush(heap, e)
            continue
        if heap[0] <= s: # 현제 가장 빠른 퇴실 시각이 입실 시각보다 빠르다면 기존방 할당
            heapq.heappop(heap)
        else:
            answer += 1 # 그렇지 않다면 새로운방 할당
        heapq.heappush(heap, e)

    return answer