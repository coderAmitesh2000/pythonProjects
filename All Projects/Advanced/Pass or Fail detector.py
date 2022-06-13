sub1 = int(input("Enter marks in subject 1:\t"))
sub2 = int(input("Enter marks in subject 2:\t"))
sub3 = int(input("Enter marks in subject 3:\t"))
print("Marks of all the subjects:", "\nsubject1:", sub1, "\nsubject2:", sub2, "\nsubject3:", sub3)

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    pass
else:
    print("Sorry to inform you that you have failed in this examination")

if (sub1 + sub2 + sub3) / 3 >= 40:
    print("Congratulations you have successfully passed in this examination")
else:
    print("Sorry to inform you that you have failed in this examination")
