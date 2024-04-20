def solution(n, words):
    reword=[]
    for i in range(len(words)):
        if words[i] in reword:
            #몇번째 사람이 몇번째에 걸렸는지 리턴
            # ex 9번째 순서에 걸렸으면 3번사람이 3번째에 걸린것
            # 8번째 순서에 걸렸으면 2번사람이 3번째에 걸린것
            
            return [(i+1)%n if (i+1)%n!=0 else n, -(-(i+1)//n)]
        
        #끝말잇기 틀린 경우
        elif i-1>=0 and words[i-1][-1]!=words[i][0]:
            ## ex 첫번째 사람이 3번째에 걸림 => [1,3] 5번 순서에서 틀림
            return [(i+1)%n if (i+1)%n!=0 else n, -(-(i+1)//n)]
        #5번째 틀렸으니 순서%인원 = 순서인 사람 5%2=1 , 순서//인원 = 몇번째 인지 5//2==2
        else:
            reword.append(words[i])
        
    answer = [0,0]
    return answer