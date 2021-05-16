
# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['hkgu','kjj',458,'jj',568]
new_list = [fox for fox in my_list if type(fox) == str]
print(new_list)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
###### ИСПРАВЛЕНЫЙ БЛОК КОДА
my_str = "ffffffffbbbbdlddddoooooooeeeekeeeepppmmmvmm"
new_str = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        new_str.append(symbol)
print(new_str)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
###### ИСПРАВЛЕНЫЙ БЛОК КОДА
my_str_1 = "ljhlj.jo;jj;df"
my_str_2 = "kkmkjhyti"
res = list(set(my_str_1).intersection(set(my_str_2)))
print(res)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
###### ИСПРАВЛЕНЫЙ БЛОК КОДА
my_str_1 = "fbbbdsdddookloeeeeppwpm"
my_str_2 = "kkksjfejjkkklw"
res = list(set(my_str_1).intersection(set(my_str_2)))
res_2 = []
for symbol in res:
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_2.append(symbol)
print(res_2)

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

