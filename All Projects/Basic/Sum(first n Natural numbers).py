num = int(input("Enter the number:\t"))
# Using while loop
sum_total = 0  # supposing sum as 0
num1 = num  # storing variable num in num1
while num > 0:  # taking a condition, until this condition is false this loop will run
    sum_total = sum_total + num  # (0+n, 0+n-1, 0+n-2, ...., 0+1)
    num = num - 1  # this is to iterate num to 0

print(f"Sum of consecutive natural numbers from 1 to {num1} is {sum_total}")

# Using for loop
numNew = int(input("Enter a number: "))
sumTotal = 0
for i in range(1, numNew+1):
    sumTotal = sumTotal + i
print(f"Sum of consecutive natural numbers from 1 to {numNew} is {sumTotal}")
