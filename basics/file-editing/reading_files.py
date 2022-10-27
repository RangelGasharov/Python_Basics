employee_file = open("employees.txt", "r")

print("Is the file readable?: " + str(employee_file.readable()))
print("")
print("First line: " + str(employee_file.readline()))
print("")
print("Whole document: \n" + str(employee_file.read()))

employee_file = open("employees.txt", "r")

print("Whole document as a list: " + str(employee_file.readlines()))

employee_file = open("employees.txt", "r")

print("List on the position 2: " + str(employee_file.readlines()[2]))
print("")

employee_file = open("employees.txt", "r")
print("Every employee from the lsit: \n")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
