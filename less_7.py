# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
my_dict_1 = {6:12,8:59,7:78,5:45}
my_dict_2 = {6:89,1:12,3:15,7:77}
result = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
print(result)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре
my_dict_1 = {6:12,8:59,7:78,5:45}
my_dict_2 = {6:89,1:12,3:15,7:77}
result = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
print(result)

# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
pers_list = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 15}]
min_value_list = []
for age in pers_list:
    min_value_list.append(list(age.values())[1])
min_value = min(min_value_list)
for name in pers_list:
    if list(name.values())[1] == min_value:
     print(list(name.values())[0])

# в) Посчитать среднее количество лет всех людей из списка.
pers_list = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 15}]
mid_value_list = []
for age in pers_list:
    mid_value_list.append(list(age.values())[1])
min_value = sum(mid_value_list)
res = sum(mid_value_list) / 3
print(res)

