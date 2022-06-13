Text = input("Please enter your text:\t")

if "make a lot of money" in Text:
    spam = True
elif "buy now" in Text:
    spam = True
elif "subscribe this" in Text:
    spam = True
elif "click this" in Text:
    spam = True
else:
    spam = False

if spam:
    print("Spam detected")
else:
    print("No spam detected")
