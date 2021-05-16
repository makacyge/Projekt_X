# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

m_s = 'lfdkfjsdkfsdnvnlsdn'
res = []
for symb in set(m_s):
    if m_s.count(symb) == 1:
        res.append(symb)
        print(res)

#### HM8
pers_list = [{"name": "John", "age": 15},{"name": "Jack", "age": 45},{"name": "Bob", "age": 15}]
ages = []
names = []
for person in pers_list:
    ages.append(person["age"])
    names_len.append(len(person["name"]))
