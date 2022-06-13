class Calculator:

    @staticmethod
    def square(n):
        print(n ** 2)

    @staticmethod
    def cube(n):
        print(n ** 3)

    @staticmethod
    def square_root(n):
        print(n ** 0.5)


operation = input("Type:- (s) for Square, (c) for Cube, (sr) for Square Root > ")
num = int(input("Enter a number: "))
compute = Calculator()

if operation == "s":
    compute.square(num)

if operation == "c":
    compute.cube(num)

if operation == "sr":
    compute.square_root(num)
