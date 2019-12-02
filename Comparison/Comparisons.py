def max_find(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(str(num1) + " is maximum.")
    elif num2 >= num3:
        print(str(num2) + " is maximum.")
    else:
        print(str(num3) + " is maximum.")


max_find(55, 456, 76)
max_find(35, 3465, 6757)
max_find(32, 4, 6)
