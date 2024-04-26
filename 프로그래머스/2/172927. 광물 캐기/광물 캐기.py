def solution(picks, minerals):
    #pick= [다이아 갯수, 철 갯수, 돌 갯수]
    #minerals=[캐야할 광물들]
    answer = 0
    
    pick_sum=0
    for i in picks:
        pick_sum+=i
    #광물 개수가 곡갱이 보다 많다면 삭제
    if pick_sum*5<len(minerals):
        minerals=minerals[:pick_sum*5]
    #최소의 피로도로 캘것, 5개의 광물을 캐고 나면 더이상 사용할 수 없음
    #minerals tired index로 변환
    tired_index=[[1,1,1],[5,1,1],[25,5,1]]
    
    fives=[]
    five=[]
    #광물 index로 변환 및 5개씩 나눠주기
    for i in range(len(minerals)):
        if minerals[i]=="diamond":
            minerals[i]=0
        elif minerals[i]=="iron":
            minerals[i]=1
        elif minerals[i]=="stone":
            minerals[i]=2
            
        five.append(minerals[i])
        if len(five)==5 or i==len(minerals)-1:
            fives.append(five)
            five=[]
    
    #5개씩 나눈 광물 피로도 구하기
    tired_check=[]
    for i in range(len(fives)):
        sum=[0,0,0]
        for j in range(len(fives[i])):
            sum[0]+=1
            sum[1]+=tired_index[1][fives[i][j]]
            sum[2]+=tired_index[2][fives[i][j]]
        tired_check.append(sum)
        
    #돌,철 내림차순으로 정렬
    tired_check.sort(key=lambda x:(-x[2],-x[1]))
    
    
    print(tired_check)
    #정렬된것을 차례로 다이아->철->돌 순으로 광물 캐기
    for i in tired_check:
        if picks[0]:
            picks[0]-=1
            answer+=i[0]
        elif picks[1]:
            picks[1]-=1
            answer+=i[1]
        elif picks[2]:
            picks[2]-=1
            answer+=i[2]
    return answer


 