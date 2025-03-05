# Operador and
a = 5
b = 10
c = 15
print(a < b and b < c)  
# True, porque 5 < 10 y 10 < 15

x = True
y = False
print(x and y)  
# False, porque True y False no son ambos verdaderos

# Operador or
x = 7.5
y = 5.8
z = 3.2
print(x > y or y > z)  
# True, porque 7.5 > 5.8 es verdadero


a = False
b = True
print(a or b)  
# True, porque al menos uno de ellos es verdadero

# Operador not
a = 5
b = 3
print(not a < b)  
# True, porque 5 no es menor que 3, entonces not (a < b) es verdadero


x = True
print(not x)  
# False, porque not True es False
