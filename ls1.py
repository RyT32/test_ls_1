# # input -> aaabb   
# # output -> a - 3  b -2 

# # # N**2
# # def strcounter(data):   # abcd 
# #     for sym in data: #len(data) 5 
# #         count = 0
# #         for sym_2 in data:#len(data) 5 
# #             if sym == sym_2:
# #                 count += 1 
# #         print(sym, count)


# # strcounter("aabcd")


# # N*M
# # N - длина строки    M - колво уникальных символов
# def strcounter(data):   # aabcd 
#     for sym in set(data): # 4 
#         count = 0
#         for sym_2 in data:#len(data) 5 
#             if sym == sym_2:
#                 count += 1 
#         print(sym, count)


# strcounter("aabcd")








# N
# N - длина строки    
# def strcounter(data):   # aabcd 
#     sym_count = {}
#     for sym in data: # 5 
#         sym_count[sym] = sym_count.get(sym,0) + 1
    
#     # print(sym_count.items())
#     for s, c in sym_count.items(): # преобразую словарь в кортеж  dict_items([('a', 2), ('b', 1), ('c', 1), ('d', 1)])
#         print(s,c)
        
        


# strcounter("aabcd")





# зарегистрироваться на гитхабе 
# https://github.com/
# https://gitforwindows.org/
# https://desktop.github.com/

# 1 способ
# создать репозиторий удаленный
# создать репозиторий локальный
# в терминале выполнить команды:
# git init


# 2 способ
# сделать все через github desktop

#3 способ
# сделать все через плагин vscode






# u = {}
# u['papa'] = 1
# print(u)
# u['child'] = 1
# print(u)
# u['child'] =  u.get('child',0)  + 1
# print(u)








#  set - множество,неупорядоченный тип данных состоящий только из уникальных элементов 


# x = {1,1,2,3}
# print(x)

# y = set('aabcd')
# print(y)

# l = [1,2,2,3,3,4,5,6,6]
# l_set = set(l)
# print(l_set)
# l = list(l_set)
# print(l)




