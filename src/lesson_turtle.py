import turtle  # Inside_Out

wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")


def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5
        if i == 3:
            size = size + 20
            sqrfunc(size)

sqrfunc(6)
