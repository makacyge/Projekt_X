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

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
#######ДОБАВЛЕННЫЙ БЛОК КОДА
my_dict_1 = {6:12,8:59,7:78,6:12}
my_dict_2 = {6:89,1:12,3:15,5:77}
new_keys = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
new_dict = {key: value for key, value in my_dict_1.items() if key in new_keys}
print(new_dict)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#######ДОБАВЛЕННЫЙ БЛОК КОДА
new_dict_88 = {**my_dict_1, **my_dict_2}
print(new_dict_88)

# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#######ДОБАВЛЕННЫЙ БЛОК КОДА
my_dict_1 = {6:12,8:59,7:78,5:45}
my_dict_2 = {6:89,1:12,3:15,7:77}
result = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
res_dict = {**my_dict_1, **my_dict_2}
for key in result:
    res_dict[key] = [my_dict_1[key], my_dict_2[key]]
print(res_dict)

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

# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
#######ДОБАВЛЕННЫЙ БЛОК КОДА
pers_list = [{"name": "JohnJohn", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 15}]
names_len = []
for person in pers_list:
    names_len.append(len(person["name"]))
    long_name_len = max(names_len)
for person in pers_list:
    if len(person["name"]) == long_name_len:
     print(person["name"])

# в) Посчитать среднее количество лет всех людей из списка.
pers_list = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 15}]
mid_value_list = []
for age in pers_list:
    mid_value_list.append(list(age.values())[1])
min_value = sum(mid_value_list)
res = sum(mid_value_list) / 3
print(res)

