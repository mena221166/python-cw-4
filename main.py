def my_name (name):
     print(f"My name is {name}")
my_name("mina")

def my_meal (food,drink):
     print(f"i like to eat {food} and while drinking {drink}")
food = input("enter your favorit food:")
drink = input("enter your favorit drink:")
my_meal (food,drink)
def cube(number):
     return number**3

def by_three(number):
     if number%3==0:
          return cube(number)
     else:
          return False
     
print(by_three(3))




