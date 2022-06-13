num = int(input("Enter the number:\t"))

for i in range(1, 11):
    print(str(num) + "X" + str(i) + "=" + str(num * i))

# another method

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
