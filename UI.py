class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
    
  def get_age(self):
    return self.age
    
a = Person('Dave', 27)
b = Person('Tom', 32)
 
print(f'{a.get_name()} is {a.get_age()} years old')
print(f'{b.get_name()} is {b.get_age()} years old')