a = 2
print('id(a) =', id(a))     # id(a) = 1901846227280

a = a + 1
print('id(a) =', id(a))     # id(a) = 1901846227312

print('id(3) =', id(3))     # id(3) = 1901846227312

b = 2
print('id(b) =', id(b))     # id(b) = 1901846227280
print('id(2) =', id(2))     # id(2) = 1901846227280

# test object identity with "is" operator
# "is" operator tests if identifier points to same memory address, return True / False
print(3 is a)               # True


# ------------------------------------------------------------------------

# Since functions are object too, a name can refer to them as well
def printHello():
    print("Hello")

a = printHello      # 'a' now refers to printHello function, i.e. different name for the same thing
a()
#Hello


# --------------------------------------------------------------------------

# in inner() we can read + write new values to c, but can only read a and b
def outer():
    b = 20              # b = local namespace; nonlocal scope
    def inner():
        c = 30          # c = nested local namespace, local scope

a = 10                  # a = global namespace, global scope
