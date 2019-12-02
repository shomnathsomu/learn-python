employee_file = open("employees.txt", "r")
# returns all texts
# print(employee_file.read())

# every line can be read on by one
# print(employee_file.readline())
# print(employee_file.readline())

# a specific index value of a file
# print(employee_file.readlines()[1])

# show as a list
# print(employee_file.readlines())

# returns a boolean
# print(employee_file.readable())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
