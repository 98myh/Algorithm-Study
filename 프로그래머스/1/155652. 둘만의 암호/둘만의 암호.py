def solution(s, skip, index):
    #s 바꿀문자
    #skip은 뛰어넘을 문자
    #index는 +할 것
    answer = ''
    
    
    list_s=list(s)
    list_skip=list(skip)

    
    #아스키코드로 전환해서 더하기
    for i in range(len(list_s)):
        text=ord(list_s[i])
        j=0
        
        while j<index:
            text+=1
            if text>122:
                text=97
            if chr(text) not in list_skip:
                j+=1
                
        answer+=chr(text)   
    return answer