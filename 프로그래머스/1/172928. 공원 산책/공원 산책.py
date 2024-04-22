def solution(park, routes):
    #park는 공원 크기, s는 시작지점, x는 장애물, o는 통행가능
    #routes는 명령어 단 범위 벗어나거나 장애물 만나면 다음 명령어 수행
    

    #문자열 리스트로 변경
    draw_park=[]
    for i in range(len(park)):
        draw_park.append(list(park[i]))
    
    x=0
    y=0
    
    #시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=="S":
                x=j
                y=i
                break
                
    print("출발 : ",x,y)
    
    #명령 실행            
    for i in routes:
        go=[]
        go=i.split(" ")
        going=True
        if go[0]=="N":
            for j in range(int(go[1])):
                if y-j-1<0 or draw_park[y-j-1][x]=="X":
                    going=False
                    break
            if going:
                y-=int(go[1])
        elif go[0]=="S":
            for j in range(int(go[1])):
                if y+j+1>len(park)-1 or draw_park[y+j+1][x]=="X":
                    going=False
                    break
            if going:
                y+=int(go[1])
        elif go[0]=="W":
            for j in range(int(go[1])):
                if x-j-1<0 or draw_park[y][x-j-1]=="X":
                    going=False
                    break
            if going:
                x-=int(go[1])
        elif go[0]=="E":
            for j in range(int(go[1])):
                if x+j+1>len(park[0])-1 or draw_park[y][x+j+1]=="X":
                    going=False
                    break
            if going:
                x+=int(go[1])
                
    print("도착 : ",y,x)
            
            

    answer = [y,x]
    return answer