def recur_sum(n):
    if n <= 0:
        pass
    elif n <= 1:
        return n
    else:
        return n + recur_sum(n-1)


num = int(input("Enter a natural number: "))
result = recur_sum(num)
print(f"Sum of first {num} natural numbers is {result}")
