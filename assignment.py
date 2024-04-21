#we recently began on object oriented programming with Python where i learned that it is a paradigm that advocates for developing software based on real-world objects
#i also learned that OOP has 4 principles which are polymorphism, abstraction, encapsulation and inheritance
#polymorphism is the ability to take on different attributes of a class
#abstraction is the ability to ignore other details and you concentrate on the highest level of representation
#encapsulation is the abilty to have what to share and what not to share
#inheritance is the concept of parent and child relationships where classes can have subclasses and objects
#i also learned that a class is the blueprint of an object for instance a class Person has objects ssuch as name, gender,age, etc
#i learned that a class gives existence to the objects
#i learned that a class begins with a capital letter and is always singular
#i also learned about objects where i learned that it is an instance of a class
#i learned that a full set of attributes/features/characteristics are what form an object
#i also learned that objects take on all attributes and features of a class but each object is different
#i learned that we can identify the class of an object using the phrase 'is a' for instance man is a Person therefore Person is a class and man is an object in class Person
#yesterday i learned that when defining an object we use a keyword class followed by the name of the class identified then a full colon
#i also learned that a function defined within a class is called a method and the individual statements within the method are known as behaviours
#i also learned that a plus sign is a polymorphic operator
#below is an example of creating objects of a class Person
class Person:
    color = ""
    size = ""
    gender = ""
    name = ""
    sound = ""
    age = "" 

man = Person()
man.name = "wilson"
man.color = "darkskinned"
man.size = "medium"
man.gender = "male"
man.sound = "talks"
man.age = "18"    

print(f"{man.name} is {man.age} years old")
print(man.name +  man.sound )
print(man.name + " is " + man.size)
print(man.name + " is " + man.gender)
print(man.name + " is " + man.color + " and " + man.size)