# Hasta ahora todos los elementos primitivos que hemos manejado
# Listas, Diccionarios, Strings, Numbers, etc tienen un cierto tipo
# que vemos con el método especial type()
# 
print(type(1))
print(type(['a','b','c']))
print(type(True)) 
print(type("Hello World"))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("Mi nombre es", self.name, "y tengo", self.age, "años")        

firulais = Dog("Firulais", 4)    
lulú = Dog("Lulú", 2)
león = Dog("León", 3)
print(type(firulais))

firulais.say_name()
lulú.say_name()
león.say_name()