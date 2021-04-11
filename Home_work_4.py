# my_list = [10,65,98,101,165,198]
# for f in my_list:
#     if f > 100:
#      print(f)

################

# my_list = [10,65,98,101,165,198]
# my_result = []
# for f in my_list:
#     if f > 100:
#       my_result.append(f)
# for f in my_result:
#     print(my_result)

my_list = [10,65,98,101,165,198]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)