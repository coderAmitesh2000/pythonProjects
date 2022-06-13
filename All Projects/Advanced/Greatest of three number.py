# Method 1

# def greatest(n1, n2, n3):
#     if n1 > n3:
#         sf = n1
#     else:
#         sf = n3
#
#     if sf > n2:
#         final = sf
#     else:
#         final = n2
#
#     print(f"The greatest of all the three number is: {final}")

# Method 2

def greatest(n1, n2, n3):
    if n1 > n3:
        if n1 > n2:
            print(f"{n1} is the greatest")
        else:
            print(f"{n2} is the greatest")
    else:
        if n3 > n2:
            print(f"{n3} is the greatest")
        else:
            print(f"{n2} is the greatest")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
greatest(num1, num2, num3)
