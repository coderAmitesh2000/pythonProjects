with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as g:
    content2 = g.read()

if content1 == content2:
    print("These two files are identical.")
else:
    print("These two files are not identical.")
