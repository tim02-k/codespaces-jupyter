import time


def muster():
    space = range(1, 10)
    for i in space:
        x = 2 * i -1
        y = len(space) - i
        print(' ' * y + '*' * x)

muster()

def muster2():
    height = int(input("Für die Höhe, geben sie eine ungerade Zahl ein: "))
    X = 1
    O = 1
    spitze = int((height/2))
    for i in range(height + 1):
        if i <= spitze:
            print("X"*X + (" "*(((height*2)-(O)-i)) + "O"*O))
            X += 1
            O += 1
            time.sleep(0.1)
        if i >= spitze:
            print("X"*X + (" "*(((height)-(O)+i)) + "O"*O))
            X -= 1
            O -= 1
            time.sleep(0.1)

muster2()