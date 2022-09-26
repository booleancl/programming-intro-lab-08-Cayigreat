# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 

class Student:
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills

    def say_name(self):
        print("Hola mi nombre es", self.name, "me desempeño como", self.position, "y mis habilidades son", self.skills, show_skills())   

    def show_skills(self):
        skills
        for skill in self.skills:
            print(skill)
        rtu

Alice = Student("Alice", "Fullstack Developer", ["Python", "Git", "HTML","CSS","Javascript"])  
Bob= Student("Bob", "Chef", ["comida peruana", "comida mexicana", "comida asiática","comida árabe"])
  
Alice.say_name()
Bob.say_name()