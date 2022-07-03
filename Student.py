from ClassAndObjects import Student

student1 = Student("Fred", "Architecture", 3.3, False)
student2 = Student("Julia", "Business", 2.8, True)
student3 = Student("Marc", "Business", 3.9, False)

print("Names: ")
print(student1.name)
print(student2.name)
print(student3.name)
print("")
print("Gpa over 3.5?: ")
print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())