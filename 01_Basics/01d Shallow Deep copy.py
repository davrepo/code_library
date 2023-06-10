#shallow copy: one level deep, only references of nested child objects
#deep copy: full independent copy

# shallow copy: only 1 level deep (i.e. not work on nested list)
import copy

org = [0, 1, 2, 3]
# 4 options
cpy = copy.copy(org)    #use copy module
cpy = org.copy()        #list has a copy option
cpy = list(org)         #make new list
cpy = org[:]              #slicing trick

cpy[0] = 100
print(org)
print(cpy)
# [0, 1, 2, 3]
# [100, 1, 2, 3]


#deep copy: 
import copy

org = [[0, 1, 2, 3], [4, 5, 6, 7]]
cpy = copy.deepcopy(org)
cpy[0][1] = 100
print(org)
print(cpy) 
# [[0, 1, 2, 3], [4, 5, 6, 7]]
# [[0, 100, 2, 3], [4, 5, 6, 7]]


# level of copy layers also apply to custome classes
import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, emp):
        self.boss = boss
        self.emp = emp

p1 = Person('Alex', 55)
p2 = Person('Joe', 25)
company = Company(p1, 2)
company_clone = copy.deepcopy(company)  #deepcopy bc class is 2 layers deep
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
# 56
# 55
