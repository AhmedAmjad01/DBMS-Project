import pypokedex
from tkinter import *
from tkinter import ttk
import tkinter as tk
import urllib3
from io import BytesIO
import image
from PIL import ImageTk, Image
import PIL.Image
import PIL.ImageTk
from tkinter.ttk import Progressbar
#import cx_Oracle as cx
#from cx_Oracle import *
import os
import time


#Splash SCREEEN
splash_root = Tk()
splash_root.geometry("350x616+470+40")
frame = Frame(splash_root, width=350, height=616)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open(r"cover.png"))
label = Label(frame, image=img)
label.pack()
splash_root.overrideredirect(True)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar",
            foreground='red', background='#4f4f4f')
progress = Progressbar(splash_root, style="red.Horizontal.TProgressbar",
                       orient=HORIZONTAL, length=500, mode='determinate', )


def main_window():
    # connectstring = os.getenv('con_connect')
    # connection = cx.connect(user='sys', password="admin123", mode=cx.SYSDBA)
    window = tk.Tk()
    window.geometry("350x616+470+40")
    window.title("Pokedex")
    window.config(padx=10, pady=10, bg='#2a75bb')

    title_label = tk.Label(window, text="Pokedex", bg='#2a75bb')
    Font_tuple = ("Pocket Monk", 40)
    title_label.config(font=Font_tuple, foreground='#ffcb05')
    title_label.place(x=70, y=0)

    pokemon_image = tk.Label(window)
    pokemon_image.pack(padx=10, pady=10)
    pokemon_information = tk.Label(window)
    pokemon_information.config(font=("Arial", 20))
    pokemon_information.pack(padx=10, pady=10)

    pokemon_types = tk.Label(window)
    pokemon_types.config(font=("Arial", 20))
    pokemon_types.pack(padx=10, pady=10)

    # FUNCTION

    def load_pokemon():
        # connection = cx.connect(
        #     user='sys', password="admin123", mode=cx.SYSDBA)
        # my_con = connection.cursor()
        pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
        http = urllib3.PoolManager()
        response = http.request('GET', pokemon.sprites.front.get('default'))
        image = PIL.Image.open(BytesIO(response.data))

        img = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image=img, bg='#2a75bb')
        pokemon_image.image = img
        pokemon_image.place(x=110, y=80)

        Font_tuple = ("Pokemon GB", 12, "bold")

        # namee = text_id_name.get(1.0, "end-1c")
        # poke_mon=my_con.execute("select name from pokedex where dex = (%s)",(namee))

        pokemon_information.config(
            text=f"{pokemon.dex} - {pokemon.name}", font=Font_tuple, bg='#2a75bb', fg='white')
        pokemon_information.place(x=60, y=200)
        pokemon_types.config(
            text=" - ".join([t for t in pokemon.types]), font=Font_tuple, bg='#2a75bb', fg='white')
        pokemon_types.place(x=50, y=260)

    def treeview():
        connection = cx.connect(
            user='sys', password="admin123", mode=cx.SYSDBA)
        my_con = connection.cursor()
        root = Tk()