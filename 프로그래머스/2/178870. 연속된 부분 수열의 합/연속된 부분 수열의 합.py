def solution(sequence, k):
    #sequence에 연속적으로 합이 k인 것을 찾는것 단 제일 짧은 것을 찾아야함(시작 인덱스가 작은것)
    answer = [0,len(sequence)]
    
    #모든 부분 수열 찾아서 비교 -> 투 포인터 사용하니 시간 초과
#     for i in range(len(sequence)):
#         sum=k-sequence[i]
#         if sum==0:
#             answer=[i,i]
#             return answer
#         for j in range(i+1,len(sequence)):
#             sum-=sequence[j]
#             if sum<0 or j-i>=small:
#                 break
#             elif sum==0 and j-i<small:
#                 small=j-i
#                 answer=[i,j]
#                 break
                
    
    
    #while 한번으로 풀이
    #start ,end 포인터 사용
    start=0
    end=0
    
    #sum 이 0일때 찾을것
    #sum 초기값을 첫번째 뺀값으로 한다
    sum=k
    
    while True:
        sum-=sequence[end]
        if sum>0:
            end+=1
            if end==len(sequence):
                break
        else:
            if sum==0 and answer[1]-answer[0]>end-start:
                answer=[start,end]
            sum+=sequence[start]+sequence[end]
            start+=1
            
    return answer