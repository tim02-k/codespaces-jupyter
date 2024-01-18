from tkinter import *
from time import sleep
from PIL import Image, ImageTk

H = 500
B = 500
window = Tk()
window.title("Snake")
c = Canvas(window, width=B, height = H)
c.pack()
grid_length= 23

body_img = Image.open("snake_body.png")
body_img = body_img.resize((grid_length, grid_length), Image.ANTIALIAS)
body_img = ImageTk.PhotoImage(body_img)
richtung = (1,0)
head_pos = [B/2, H/2]