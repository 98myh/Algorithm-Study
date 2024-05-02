def solution(numbers):
    answer = [-1]*len(numbers)
#     시간초과 발생
#     answer=[]
#     for i in range(len(numbers)):
#         check=False
#         for j in range(i+1,len(numbers)):
#             if numbers[i]<numbers[j]:
#                 answer.append(numbers[j])
#                 check=True
#                 break
            
#         if check==False:
#             answer.append(-1)
    
    stack=[]
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]]<numbers[i]:
             answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer