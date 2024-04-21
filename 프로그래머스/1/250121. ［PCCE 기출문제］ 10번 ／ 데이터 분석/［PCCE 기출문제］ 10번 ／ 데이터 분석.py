def solution(data, ext, val_ext, sort_by):
    # ext - 기준
    # val_ext - 뽑아낼 정보의 기준값
    # sort_by - 정렬할 기준
    
    #기준인 인덱스 뽑아내서 val_ext를 조건으로 sort_by 할 것
    
    ext_list=["code","date","maximum","remain"]
    ext_index=0
    sort_index=0
    
    #인덱스 뽑아냄
    for i in range(len(ext_list)):
        if ext==ext_list[i]:
            ext_index=i
        if sort_by==ext_list[i]:
            sort_index=i
    
    #기준으로 데이터를 뽑아냄
    select_list=[]
    
    for j in range(len(data)):
        if val_ext>data[j][ext_index]:
            select_list.append(data[j])
    
    #정렬
    select_list.sort(key=lambda x:x[sort_index])
    
    
    answer = select_list
    return answer