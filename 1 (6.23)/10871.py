import random
random_list=[]
while len(random_list) < 10 :
    a = random.randint(1,10)
    if a not in random_list :
        random_list.append(a)
print(random_list)
b = random.randint(1,10)

small_than_b=[]

for i in random_list:
    if i < b:
        small_than_b.append(i)
print(small_than_b)
