# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
def create_list():
    list = ['hkgu','kjj', 458 ,'jj', 568 ," yrtg"]
    new_list = [fox for fox in list if type(fox) == str]
    print(new_list)
create_list()

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
def create_my_string():
    my_string = "ffffffffbbbbdldddjdoooooooeeeekeeeepppmmmvmm"
    new_string = []
    for symbol in set(my_string):
        if my_string.count(symbol) == 1:
           new_string.append(symbol)
    print(new_string)
create_my_string()

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
def create_my_list():
    my_str_1 = "ljhlj.jo;jj;df"
    my_str_2 = "kdkmkjhyti"
    res = list(set(my_str_1).intersection(set(my_str_2)))
    print(res)
create_my_list()

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
def create_my_list():
    my_str_1 = "fbbbdsdddookloeeeeppwpm"
    my_str_2 = "kkksjfejjkkklw"
    res = list(set(my_str_1).intersection(set(my_str_2)))
    res_2 = []
    for symbol in res:
     if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_2.append(symbol)
    print(res_2)
create_my_list()

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
import random
def create_email(names, domains):
    name = random.choice(names)
    number = random.randint(100, 999)
    import string
    my_list = ["h","i","l","l","e","l"]
    alphabet = string.ascii_lowercase
    my_list = [random.choice(alphabet) for _ in range(random.randint(5,7))]
    my_list = "".join(my_list)
    domains = random.choice(domains)
    result = f"{name}.{number}@{my_list}.{domains}"
    return  result

names = ["Bob", "Jey", "Tramp"]
domains = ["net", "com", "ua"]
res = create_email(names, domains)
print(res)