def solution(keymap, targets):
    answer = []
    #keymap의 순서대로 셋팅되어있음
    #targets을 입력하려고 할때 keymap에서 최소 몇번을 눌러야 되는지 합해서 출력
    #딕셔너리를 사용해서 keymap의 키 할당
    key={}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in key:
                key[keymap[i][j]]=j+1
            else:
                if key[keymap[i][j]]>j+1:
                    key[keymap[i][j]]=j+1
    
    for i in range(len(targets)):
        total=0
        for j in range(len(targets[i])):
            if targets[i][j] in key:
                total+=key[targets[i][j]]
            else: 
                total=-1
                break
        answer.append(total)    
        
    return answer