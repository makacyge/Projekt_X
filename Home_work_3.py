value = 101
new_value = value / 2 if value < 100 else - value
print(new_value)

#################

value =102
new_value = 1 if value < 100 else 0  ### ИСПРАВЛЕНАЯ СТРОКА
print(new_value)

#################

value = 102
new_value = True if value < 100 else False   ### ИСПРАВЛЕНАЯ СТРОКА
print(new_value)

#################

my_str = "Hamster"
print(my_str[::2])

#################

my_str = "Hamster"
print(my_str[1::2])

#################

my_str = "Hams"
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)

#################

my_str = "Hamster"
new_str = my_str + my_str [::-1] if len(my_str) < 5 else my_str
print(new_str)