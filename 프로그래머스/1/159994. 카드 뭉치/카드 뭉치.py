def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    one=0
    two=0
    
    for i in range(len(goal)):
        if one<len(cards1) and cards1[one]==goal[0]:
            goal.remove(cards1[one])
            print(goal)
            one+=1
        elif two<len(cards2) and cards2[two]==goal[0]:
            goal.remove(cards2[two])
            print(goal)
            two+=1
        else:
            return 'No'
    
    return answer