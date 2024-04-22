def solution(wallpaper):
    ystart=len(wallpaper)
    yend=0
    
    xstart=len(wallpaper[0])
    xend=0
    xlist=[]
    
    #y축 시작점과 끝점을 구한다.
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            if ystart>i:
                ystart=i
            if yend<i:
                yend=i
                
        #x축 시작점 끝점 구한다  
        xlist=list(wallpaper[i])
        
        for j in range (len(xlist)):
            if xlist[j]=="#":
                if xstart>j:
                    xstart=j
                if xend<j:
                    xend=j
             
    answer = [ystart,xstart,yend+1,xend+1]
    return answer