def func():
    print("Hello world!")
    print("First function!")


def add(a, b, c):
    return a+b+c


def introduction(name, age):
    print("Hey, I am " + name + ". I am " + age + " years old.")


# works as top down parser
func()
print(add(9, 999, 0.9))
introduction("Lincoln", '25')
introduction("Crimson", str(33))
