#Dictionary comprehension
#https://www.youtube.com/watch?v=khCzymLy_QE&t=199s

# ---------- loop implementation -------------------------

#Dict from 2 Lists (key,value) pair, for loop implementation w/ zip()
names = ['Maria', 'Mike', 'Peter']
profs = ['programmer', 'farmer', 'wizard']

#with zip()
my_dict_zip = {}        #create an empty dictionary

for (key, value) in zip(names, profs):
    my_dict_zip[key] = value

print('for loop zip \n', my_dict_zip)

#with range()
my_dict_iter = {}

for i in range(len(names)):
    my_dict_iter[names[i]] = profs[i]

print('for loop range \n', my_dict_iter)

# ---------- dict comprehension, make dict from 2 lists ---------------------

my_dict_comp_zip = {        #comprehension creates a new dict for you, don't have to make an empty dict
    key : value for (key, value) in zip(names, profs)
    }
print('dict comprehension zip \n', my_dict_comp_zip)

my_dict_comp_range = {
    names[i] : profs[i] for i in range(len(names))}
print('dict comprehension range \n', my_dict_comp_range)

# ---------------- dictionary manipulation, change keys / values --------------

#this example is not quite useful b/c requires intimate knowledge of the dict content
my_dict = {     
    "Spider": "photographer", 
    "Bat": "philanthropist", 
    "Wonder Wo": "nurse"
}

my_dict = {
    (key+"man" if key != "Spider" else "Superman"):
    (val if val != "photographer" else "journalist") 
    for (key, val) in my_dict.items()}  #my_dict will only fetch keys; .items() fetch key:value pair 

print(my_dict)

# --------------- random DNA pairing example (dict of lists) -------------

import random

dna_bases = ["A", "T", "C", "G"]

# for random.choices() see https://www.w3schools.com/python/ref_random_choices.asp
dna_st1 = random.choices(dna_bases, k=10)   #.choice() returns a k sized List
print(dna_st1)

# loop implementation
# dna = {}
# for i, b in enumerate(dna_st1):   #enumerate returns 2 values, index and value
#     if b == 'A':
#         b2 = 'T'
#     elif b == 'T':
#         b2 = 'A'
#     elif b == 'C':
#         b2 = 'G'
#     else:
#         b2 = 'A'
#     dna[i] = [b, b2]    #key is index, value is base pair
# print(dna)
    

dna = {i: [b, ('T' if b =='A' 
                else 'A' if b =='T' 
                else 'C' if b =='G' 
                else 'G')] 
            for (i, b) in enumerate(dna_st1)}
print(dna)      #dna is a dictionary of lists


# ---------------- assemble a list of dictionaries, example ------------------
# - user information is stored in a special dictionary
# - the keys of this dictionary are pre-determined in keys
# - the id is a unique identifier, must be automatically generated
# - the usernames are pre-determined in users
# - the password must be randomly and automatically generated

import random
import string

keys = ["id", "username", "password"]
users = ["mariyasha888", "KnotABot", "SpongiBOBO", "IAMBATMAN"]

#string.printable is a string constant of all ASCII chars. See https://docs.python.org/3/library/string.html
data = [{key:               #create each dict specification
         (i if key == "id" 
            else users[i] if key == "username" 
            else "".join(random.choices(string.printable, k=8)))    #random.choice() returns a list, use"".join to make a string
        for key in keys
        }   
        for i in range(len(users))]     #make len(users) number of dict
print(data)

# -----------------panda dataframe ------------------------------------

#zip implementation
my_pd_comp_zip = {        
    key : value for (key, value) in zip(names[0], profs[0])
    }

#range implementation
my_pd_comp_range = {
    names[0][i] : profs[0][i] for i in range(len(names))}