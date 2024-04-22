def solution(friends, gifts):
    total_gift=[[0 for i in range(len(friends))]for j in range(len(friends))]
    gisu=dict.fromkeys(friends,0)
    for i in gifts:
        a=[]
        a=i.split(" ")
        fir=0
        sec=0
        for j in range(len(friends)):
            if a[0]==friends[j]:
                fir=j
                gisu[friends[j]]+=1
            elif a[1]==friends[j]:
                sec=j
                gisu[friends[j]]-=1
        total_gift[fir][sec]+=1
        
    # 주고 받은 선물, 지수 다 구함
    # 선물 갯수 비교해서 다음 달 선물 예측
    max=0
    for z in range(len(total_gift)):
        small_sum=0
        for x in range(len(total_gift)):
            if total_gift[z][x]>total_gift[x][z]:
                small_sum+=1
            elif total_gift[z][x]==total_gift[x][z] and gisu[friends[z]]>gisu[friends[x]]:
                small_sum+=1
        if max<small_sum:
            max=small_sum
                
    answer = max
    return answer

