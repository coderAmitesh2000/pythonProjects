def game():
    return 99


score = game()
with open("Highscore.txt", "r") as f:
    if int(f.read()) < 99:
        with open("Highscore.txt", "w") as g:
            g.write(str(score))
    else:
        pass
