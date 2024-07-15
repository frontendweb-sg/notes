# number
num = 10
Num = 30
value = 10/6
valueInt = 10//6
valueRem = 10 % 6
try:
    infinite = 10/0
    print(num, value, valueInt, valueRem, infinite)
except ZeroDivisionError:
    print("Error")

print(num, Num)


name = "Pradeep Kumar"
text = """Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
Velit exercitationem pariatur iure iusto temporibus sunt delectus quis saepe ex repellendus. 
Labore, nesciunt. Sapiente animi,fugiat dicta culpa alias nisi vero."""

print(name.split(' '))
print(text.split(' '))

# Many value to multiple variables
x, y, z = 10, 'Hello world', 34.6
print(x, y, z)


a, b = 10, 40
print(a, b, a+b)

# one value to multiple variables
m = n = o = 90
print(m, n, o, id(m), id(n), id(o))

# unpack collection
users = ['pk', 'ak', 'sk', 'dk', 'ra', 'aa']
[a, b, c, *r] = users
print(a, b, c, r)
