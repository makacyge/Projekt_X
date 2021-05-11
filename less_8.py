import random
# from random import randint, choice


# rand_value = random.randint(1, 10)
# print(rand_value)
#
# triangle ={'A':(random.randint(-10, 10), random.randint(-10, 10)),
#            'B':(random.randint(-10, 10), random.randint(-10, 10)),
#            'C':(random.randint(-10, 10), random.randint(-10, 10)),}
# print(triangle)

# import string
# alf = string.ascii_letters
# print(alf)
def create_triangle():
    

triangle_1 = {'A':(random.randint(-10, 10), random.randint(-10, 10)),
           'B':(random.randint(-10, 10), random.randint(-10, 10)),
           'C':(random.randint(-10, 10), random.randint(-10, 10)),}
triangle_2 = {'A':(random.randint(-10, 10), random.randint(-10, 10)),
           'B':(random.randint(-10, 10), random.randint(-10, 10)),
           'C':(random.randint(-10, 10), random.randint(-10, 10)),}
triangle_3 = {'A':(random.randint(-10, 10), random.randint(-10, 10)),
           'B':(random.randint(-10, 10), random.randint(-10, 10)),
           'C':(random.randint(-10, 10), random.randint(-10, 10)),}
triangles = [triangle_1, triangle_2, triangle_3]
for triangle in triangles:
 print(triangle)