def solution(today, terms, privacies):
    #today를 기준
    #약관 별 term
    #privacies는 약관 가입 날짜
    #privacies 가입 날짜에서 term을 더해서 today 넘지 않았으면 answer.append() 
    #=> if privacies+term<=today : answer.append()
    answer = []
    term_dict={}
    today_year,today_month,today_day=today.split(".")
    # today_year,today_month,today_day=int(today_year),int(today_month),int(today_day)
    today_total=12*28*int(today_year)+28*int(today_month)+int(today_day)
    count=1
    for i in terms:
        fir,sec=i.split()
        term_dict[fir]=int(sec)
        
    for i in privacies:
        #day와 약관 나눔
        day,category=i.split()
        #년,월,일 나눔
        year,month,day=day.split('.')
        # year,month,day=int(year),int(month),int(day)
        total_term=12*28*int(year)+28*int(month)+int(day)
        # month+=term_dict[category]
        total_term+=term_dict[category]*28
        # if month>12:
        #     year+=month//12
        #     month=month%12
        
        #기간 넘은거 answer에 추가
        # if today_year>year:
        #     answer.append(count)
        # elif today_year==year and today_month>month:
        #     answer.append(count)
        # elif today_year==year and today_month==month and today_day>=day:
        #     answer.append(count)
        if today_total>=total_term:
            answer.append(count)
        count+=1
        
    return answer