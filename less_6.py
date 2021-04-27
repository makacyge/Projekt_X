
# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['hkgu','kjj',458,'jj',568]
new_list = [fox for fox in my_list if type(fox) == str]
print(new_list)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = set ("ffffffffbbbbdddddoooooooeeeeeeeepppmmmmm")
n_str = []
n_str.extend(my_str)
print(n_str)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = ("fffbbbddddoooeeeepppm")
my_str_1 = ("kkkssjjjkkklll")
n_str = []
n_str.extend(set(my_str_1))
n_str.extend(set(my_str))
print(n_str)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = ("fbbbdsssdddookloeeeepppm")
my_str_1 = ("kkkssjfejjkkkl")
my_str_set = set(my_str)
my_str_1_set = set(my_str_1)
n_str = my_str_1_set.intersection_update(my_str_set)
print(n_str)

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):

person = {"lastname": "Rybakov",
          "name": "Vlad",
          "age": 23,
          "address": {"country": "Ukraine",
                      "city": "Dnepr",
                      "strit": "Lizy Chaikinoy"},
          "work": {"fact": "yes",
                   "position": "manager"}}

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):

рецепт = {"Коржи": {"Мука": 100,
                    "Молоко": 200,
                    "Масло": 30,
                    "Яйцо": 2},
          "Крем": {"Сахар": 150,
                   "Масло": 100,
                   "Ваниль": 5,
                   "Сметана": 50},
          "Глазурь": {"Какао": 80,
                      "Сахар": 500,
                      "Масло": 18}}

