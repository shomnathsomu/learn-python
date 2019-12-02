# employee_file = open("employees.txt", "a")

# create file or totally overlap the previous texts
employee_file = open("employees.txt", "w")

# create a html file
# file = open("index.html", "w")
# file.write("<p>This the first text</p>")

employee_file.write("\nSoftware company")

employee_file.close()
