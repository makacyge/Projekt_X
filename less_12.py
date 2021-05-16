# def sort_dict(pers_dict):   ### Сортировка по возрасту
#     age = pers_dict["age"]
#     return age
# persons = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 16}]
# n_p = sorted(persons, key=sort_dict)
# print(n_p)
#

# def sort_dict(pers_dict):  ### Сортировка по алфавитному порядку имен
#     name = pers_dict["name"]
#     return name
# persons = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 16}]
# n_p = sorted(persons, key=sort_dict)
# print(n_p)
#

# def sort_by_name_len(pers_dict):  ### Сортировка по длинне имени
#     name_len = len(pers_dict["name"])
#     return name_len
# persons = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 16}]
# n_p = sorted(persons, key=sort_by_name_len)
# print(n_p)
#
my_str_1 = "fbbbdsdddooklloeeeeppwpm"
my_str_2 = "kkksjfejjkkklw"
res = list(set(my_str_1).intersection(set(my_str_2)))
res_2 = []
for symbol in res:
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_2.append(symbol)
print(res_2)