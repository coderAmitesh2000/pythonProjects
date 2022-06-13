sub1 = int(input("Enter marks in subject 1:\t"))
sub2 = int(input("Enter marks in subject 2:\t"))
sub3 = int(input("Enter marks in subject 3:\t"))
print("Marks of all the subjects:", "\nsubject1:", sub1, "\nsubject2:", sub2, "\nsubject3:", sub3)

Total = int(sub1 + sub2 + sub3)
TotalPercent = int((Total / 300) * 100)

if sub1 >= 33:
    pass
else:
    print("Fail")

if sub2 >= 33:
    pass
else:
    print("Fail")

if sub3 >= 33:
    pass
else:
    print("Fail")

if TotalPercent >= 40:
    print("You have successfully passed this exam")
else:
    print("Fail")
