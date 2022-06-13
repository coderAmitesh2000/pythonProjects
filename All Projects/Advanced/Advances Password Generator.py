# Password generator

import random

alpLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]
alpLowerSelect_1 = random.randint(0, 25)
alpLowerSelect_2 = random.randint(0, 25)
alpLowerSelect_3 = random.randint(0, 25)
alpLowerSelect_4 = random.randint(0, 25)

alpUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]
alpUpperSelect_1 = random.randint(0, 25)
alpUpperSelect_2 = random.randint(0, 25)
alpUpperSelect_3 = random.randint(0, 25)
alpUpperSelect_4 = random.randint(0, 25)

signs = ["!", "@", "#", "$", "%", "^", "&", "*", "<", ">", "/", "?", "-", "_", "+", "=", "|"]
signsSelect_1 = random.randint(0, 16)
signsSelect_2 = random.randint(0, 16)
signsSelect_3 = random.randint(0, 16)
signsSelect_4 = random.randint(0, 16)
signsSelect_5 = random.randint(0, 16)


num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)
num5 = random.randint(0, 9)

password_08 = f"{signs[signsSelect_1]}{alpUpper[alpUpperSelect_1]}{num1}{signs[signsSelect_2]}" \
              f"{alpLower[alpLowerSelect_1]}{alpUpper[alpUpperSelect_2]}{num2}{alpLower[alpLowerSelect_2]}"

password_09 = f"{alpLower[alpLowerSelect_1]}{signs[signsSelect_1]}{alpUpper[alpUpperSelect_1]}" \
              f"{alpLower[alpLowerSelect_2]}{num1}{signs[signsSelect_2]}{signs[signsSelect_3]}" \
              f"{alpLower[alpLowerSelect_3]}{num2}"

password_10 = f"{num1}{alpUpper[alpUpperSelect_1]}{alpLower[alpLowerSelect_1]}{alpLower[alpLowerSelect_2]}" \
              f"{signs[signsSelect_1]}{alpUpper[alpUpperSelect_2]}{signs[signsSelect_2]}{num2}" \
              f"{alpLower[alpLowerSelect_3]}{alpUpper[alpUpperSelect_3]}"

password_11 = f"{signs[signsSelect_1]}{alpLower[alpLowerSelect_1]}{alpLower[alpLowerSelect_2]}{num1}" \
              f"{alpUpper[alpUpperSelect_1]}{signs[signsSelect_2]}{num2}{num3}{alpUpper[alpUpperSelect_2]}" \
              f"{alpLower[alpLowerSelect_3]}{signs[signsSelect_3]}"

password_12 = f"{alpUpper[alpUpperSelect_1]}{alpLower[alpLowerSelect_1]}{alpLower[alpLowerSelect_2]}" \
              f"{signs[signsSelect_1]}{alpUpper[alpUpperSelect_2]}{num1}{alpUpper[alpUpperSelect_3]}" \
              f"{signs[signsSelect_2]}{num2}{num3}{alpUpper[alpUpperSelect_4]}{signs[signsSelect_3]}"

password_13 = f"{num1}{signs[signsSelect_1]}{signs[signsSelect_2]}{alpLower[alpLowerSelect_1]}{num2}" \
              f"{alpUpper[alpUpperSelect_1]}{alpUpper[alpUpperSelect_2]}{signs[signsSelect_3]}" \
              f"{alpLower[alpLowerSelect_2]}{alpUpper[alpUpperSelect_3]}{num3}{num4}{signs[signsSelect_4]}"

password_14 = f"{alpLower[alpLowerSelect_1]}{num1}{num2}{signs[signsSelect_1]}{alpUpper[alpUpperSelect_1]}" \
              f"{alpLower[alpLowerSelect_2]}{alpLower[alpLowerSelect_3]}{signs[signsSelect_2]}{num3}" \
              f"{alpUpper[alpUpperSelect_2]}{alpUpper[alpUpperSelect_3]}{num4}{signs[signsSelect_3]}" \
              f"{alpLower[alpLowerSelect_4]}"

password_15 = f"{signs[signsSelect_1]}{alpLower[alpLowerSelect_1]}{alpLower[alpLowerSelect_2]}{num1}" \
              f"{alpUpper[alpUpperSelect_1]}{num2}{num3}{signs[signsSelect_2]}{alpLower[alpLowerSelect_3]}" \
              f"{signs[signsSelect_3]}{signs[signsSelect_4]}{alpUpper[alpUpperSelect_2]}{num4}" \
              f"{alpLower[alpLowerSelect_4]}{signs[signsSelect_5]}"

password_16 = f"{alpUpper[alpUpperSelect_1]}{signs[signsSelect_1]}{signs[signsSelect_2]}{num1}" \
              f"{alpLower[alpLowerSelect_1]}{num2}{num3}{alpUpper[alpUpperSelect_2]}{num4}{signs[signsSelect_3]}" \
              f"{alpLower[alpLowerSelect_2]}{alpUpper[alpUpperSelect_3]}{alpUpper[alpUpperSelect_4]}" \
              f"{signs[signsSelect_4]}{alpLower[alpLowerSelect_3]}{num5}"

print("PASSWORD OPTIONS:-")

print(f"08 digit password is :- {password_08}")
print(f"09 digit password is :- {password_09}")
print(f"10 digit password is :- {password_10}")
print(f"11 digit password is :- {password_11}")
print(f"12 digit password is :- {password_12}")
print(f"13 digit password is :- {password_13}")
print(f"14 digit password is :- {password_14}")
print(f"15 digit password is :- {password_15}")
print(f"16 digit password is :- {password_16}")
