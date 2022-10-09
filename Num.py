import random

randlist3 = []
for _ in range(10):
    randlist3.append(random.randint(0,99))
    
print (randlist3)

#Error to be debugged]
my_list=[1,2,3,3,3,4,5,6,6,7]
my_set = [set(my_list)]
my_set
my_set.sort(reverse = True)
print(my_set)