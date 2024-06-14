import random

highscore = 0
noHighscore = False
num = random.randrange(1, 100)


print(num)


def guessnumb(num):
    gues = input("Welche Nummer ist es: ")
    if not gues.isdigit():
        print("falsche Eingabe, nur ganze Zahlen")
        pass
    elif int(gues) == num:
        print("you won!")
        return True
    elif int(gues) > num:
        print("zu Hoch geraten")

    elif int(gues) < num:
        print("zu niedrig geraten")


def lesen():
    datei = open("highcore.txt", "r")
    alltimehigh = datei.read().lstrip("[").strip("]").lstrip("'.'")
    alltimehigh = alltimehigh.split(",")
    datei.close()
    return alltimehigh


def schreiben(alltimehigh):
    datei = open("highcore.txt", "w")
    datei.write(str(alltimehigh))
    datei.close()


alltimehigh = lesen()

while True:

    highscore = 1 + highscore
    gewonnen = guessnumb(num)
    if gewonnen == True:
        print(f"Danke fürs spielen, dein Highscore ist {highscore}!")
        break
try:
    if int(alltimehigh[1].strip()) == 1:
        punkt = "Punkt"
    else:
        punkt = "Punkten"
except:
        noHighscore = True
if int(alltimehigh[1]) <= int(highscore):
    if int(alltimehigh[1]) == int(highscore):
        print(f"Du hast den selben Highscore wie {alltimehigh[0].strip("'")} geschafft, probiers nochmal")

    else:
        print(f"Leider hast du nicht den Highscore von {alltimehigh[0]} mit{alltimehigh[1]} {punkt} geknackt ")


else:
    if noHighscore == False:
        print(f"Herzlichen Glückwunsch du hast den Besten Highcore von {alltimehigh[0]} mit  {int(alltimehigh[1]) - highscore} {punkt} übertroffen.")
        newhighName = input("Bitte geb deinen Namen ein:")
        alltimehigh[0] = newhighName
        alltimehigh[1] = highscore
        schreiben(alltimehigh)
    else:
        print(
        f"Herzlichen Glückwunsch du hast den ersten Highcore geschafft")
        newhighName = input("Bitte geb deinen Namen ein:")
        alltimehigh[0] = newhighName
        alltimehigh[1] = highscore
        schreiben(alltimehigh)

print("Bis zu nächsten mal")

