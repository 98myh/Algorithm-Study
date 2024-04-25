def solution(plans):
    
    #끝나는 순서대로 출력
    #시작은 처음부터 하지만 중간에 다른과제 할 시간이 되면 하던 과제 멈춰둠
    #그리고 멈춘 과제가 여러개일 때는 최근에 멈춘 과제부터 시작해서 끝냄
    
    #[과제, 시작시간, 완료시간]
    
    remind=[] #남은것
    end=[] #끝낸것
    
    #plane 시간 변경 -> 12:00=720
    for i in range(len(plans)):
        clock=plans[i][1].split(":")
        #분으로 바꿔서 저장
        plans[i][1]=int(clock[0])*60+int(clock[1])
        
    #시작 순으로 sort
    plans.sort(key=lambda x:x[1])
    print(plans)
    
    for i in range(len(plans)):
        #과제를 제 시간에 끝냈다면
        if i<len(plans)-1 and int(plans[i][1])+int(plans[i][2])<=int(plans[i+1][1]):
            #끝난거 추가
            end.append(plans[i][0]) 
            #남은시간 구하기
            timeout=int(plans[i+1][1])-(int(plans[i][1])+int(plans[i][2]))
            
            #시간 남았다면 멈췄던 과제 실행
            while timeout>0 and len(remind)>0:
                if timeout-remind[-1][2]>=0:
                    timeout-=remind[-1][2]
                    end.append(remind[-1][0])
                    remind.pop()
                else:
                    remind[-1][2]-=timeout
                    break
                    

        #마지막은 무조건 end에 추가       
        elif i==len(plans)-1:
            end.append(plans[i][0])        
                
        #과제가 제 시간에 끝나지 않았다면 remind에 추가
        else:
            plans[i][2]=int(plans[i][1])+int(plans[i][2])-int(plans[i+1][1])
            remind.append(plans[i])
        
    
    #남아있는 과제 끝에서부터 차례로 끝내기
    while len(remind)>0:
        end.append(remind[-1][0])
        remind.pop()
        
    answer = end
    return answer