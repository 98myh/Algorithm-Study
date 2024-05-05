def solution(data, col, row_begin, row_end):
    #첫번째 컬럼은 기본키 
    #col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 만약 값이 동일하면 기본키인 첫번째 컬럼의 값을 기준으로 내림차순 정렬
    #정렬된 데이터에서 s_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의
    #row_begin<=i<=row_end 인 모든 s_i 누적하여 xor한 값을 해시 값으로 반환
    
    # [[2,2,6]
    # [1,5,6]]
    #여기서 [?][1] 기준으로 정렬
    
    #정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    answer=0
    a=0
    #mod 및 xor
    for i in range(row_begin-1,row_end):
        a=0
        for j in data[i]:
            a+=(j%(i+1))
        answer=answer^a
    
    
    return answer