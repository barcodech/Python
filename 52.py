


# # lambda parameters:expression

def double(x):
    return x*2

print(double(2))

double = lambda x:x*2
print(double(2))

multiply = lambda x,y:x*y
print(multiply(2,3))

add=lambda x,y,z: x+y+z
print(add(1,2,3))

full_name = lambda first_name,last_name: first_name+last_name
print(full_name("Meta","Verse"))