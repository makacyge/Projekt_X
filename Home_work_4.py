my_list = [10,65,98,101,165,198]
for f in my_list:
if f > 100:
print(f)

################

my_list = [10,65,98,101,165,198]
my_result = []
for f in my_list:
if f > 100:
my_result.append(f)
print(my_result)

################
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

ИСПРАВЛЕНЫЙ БЛОК КОДА
my_list = [4,5,6,7]
if len(my_list) < 2:
 my_list.append(0)
else:
 my_list = my_list[-1] + my_list [-2]
print(my_list)
###############

my_string = '0123456789'
r =[]
for f_1 in my_string:
for f_2 in my_string:
r.append(int(f_1 + f_2))
print(r)
######
