def solution(phone_book):
    answer = True
    l = len(phone_book)
    
    phone_book.sort()
    for i in range(l-1):
        if len(phone_book[i]) < len(phone_book[i+1]) and phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
#     for i in range(l):
#         for j in range(i+1,l):
#             if len(phone_book[i]) < len(phone_book[j]) and phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                     return False
        
    
    return answer