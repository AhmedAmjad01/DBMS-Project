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
        root.geometry("350x616+470+40")
        root.title("pokedex(treeview)")
        trv = ttk.Treeview(root)
        trv.grid(row=1, column=1, padx=10, pady=10, ipady=300)

        trv["columns"] = ("1", "2", "3", "4")

        # Defining
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=80, anchor='c')
        trv.column("2", width=80, anchor='c')
        trv.column("3", width=80, anchor='c')
        trv.column("4", width=80, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="dex")
        trv.heading("2", text="name")
        trv.heading("3", text="type")
        trv.heading("4", text="type2")

        r_set = my_con.execute("select * from testingpoke")

        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(
                dt[0], dt[1], dt[2], dt[3]))

    def update_pokemon():
        connection = cx.connect(
            user='sys', password="admin123", mode=cx.SYSDBA)
        my_con = connection.cursor()
        newname = text_id_uptd_name.get(1.0, "end-1c")
        newdex = text_id_dex.get(1.0, "end-1c")
        my_con.execute("begin updatepoki(:1,:2);end;", [newname, newdex])
        print(newname)

    def import_csv_file():
        connection = cx.connect(
            user='sys', password="admin123", mode=cx.SYSDBA)
        my_con = connection.cursor()

        excel = my_con.execute("select * from pokedex")
        print(x)
        excel = pd.DataFrame(x)
        excel('path to define')

    def moreoptions():
        roo2 = Tk()
        roo2.geometry("350x616+470+40")
        roo2.title("More Options")
        roo2.config(padx=10, pady=10, bg='#2a75bb')
        # framer = Frame(roo2, width=350, height=616)
        # framer.pack()
        # framer.place(anchor='center', relx=0.5, rely=0.5)
        # img = ImageTk.PhotoImage(Image.open(r"cover.png"))
        # label = Label(framer, image=img)
        # label.pack()

        def insert_pokemon():
            connection = cx.connect(
                user='sys', password="admin123", mode=cx.SYSDBA)
            my_con = connection.cursor()
            insertdex = text_dex.get(1.0, "end-1c")
            insertname = text_insertname.get(1.0, "end-1c")
            inserttype = text_inserttype.get(1.0, "end-1c")

            my_con.execute("begin insert_pokemon(:1,:2,:3);end;",
                           [insertdex, insertname, inserttype])

        def delete_pokemon():
            connection = cx.connect(
                user='sys', password="admin123", mode=cx.SYSDBA)

            my_con = connection.cursor()
            deldex = del_dex.get(1.0, "end-1c")
            my_con.execute("begin delete_pokemon(:1);end;",
                           [deldex])

        label_id_name2 = tk.Label(roo2, text="Insert Dex, Name, Type")
        Font_tuple = ("Pokemon GB", 6, "bold")
        label_id_name2.config(font=Font_tuple, bg='#2a75bb', fg='white')
        label_id_name2.place(x=5, y=50)

        text_dex = tk.Text(roo2, height=0.5, width=30)
        text_dex.config(font=("Arial", 10))
        text_dex.place(x=5, y=70)

        text_insertname = tk.Text(roo2, height=0.5, width=30)
        text_insertname.config(font=("Arial", 10))
        text_insertname.place(x=5, y=100)

        text_inserttype = tk.Text(roo2, height=0.5, width=30)
        text_inserttype.config(font=("Arial", 10))
        text_inserttype.place(x=5, y=130)

        btn_load = tk.Button(roo2, text="Insert", command=insert_pokemon)
        btn_load.config(font=("Pocket Monk", 10))
        btn_load.place(x=10, y=170)

        label_id_name2 = tk.Label(roo2, text="Insert Dex To Delete")
        Font_tuple = ("Pokemon GB", 6, "bold")
        label_id_name2.config(font=Font_tuple, bg='#2a75bb', fg='white')
        label_id_name2.place(x=5, y=210)

        del_dex = tk.Text(roo2, height=0.5, width=30)
        del_dex.config(font=("Arial", 10))
        del_dex.place(x=5, y=230)

        btn_load = tk.Button(roo2, text="Delete", command=delete_pokemon)
        btn_load.config(font=("Pocket Monk", 10))
        btn_load.place(x=10, y=270)

    label_id_name = tk.Label(window, text="ID or Name")
    Font_tuple = ("Pokemon GB", 10, "bold")
    label_id_name.config(font=Font_tuple, bg='#2a75bb', fg='white')
    label_id_name.place(x=80, y=340)

    text_id_name = tk.Text(window, height=1, width=30)
    text_id_name.config(font=("Arial", 10))
    text_id_name.place(x=50, y=370)

    btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
    btn_load.config(font=("Pocket Monk", 10))
    btn_load.place(x=110, y=400)

    btn_load = tk.Button(window, text="Load DataBase", command=treeview)
    btn_load.config(font=("Pocket Monk", 10))
    btn_load.place(x=110, y=430)

    label_id_name2 = tk.Label(window, text="Update")
    Font_tuple = ("Pokemon GB", 10, "bold")
    label_id_name2.config(font=Font_tuple, bg='#2a75bb', fg='white')
    label_id_name2.place(x=110, y=470)

    text_id_uptd_name = tk.Text(window, height=1, width=30)
    text_id_uptd_name.config(font=("Arial", 10))
    text_id_uptd_name.place(x=50, y=490)

    label_id_name2 = tk.Label(window, text="To")
    Font_tuple = ("Pokemon GB", 10, "bold")
    label_id_name2.config(font=Font_tuple, bg='#2a75bb', fg='white')
    label_id_name2.place(x=110, y=510)

    text_id_dex = tk.Text(window, height=1, width=30)
    text_id_dex.config(font=("Arial", 10))
    text_id_dex.place(x=50, y=530)

    btn_load = tk.Button(window, text="Update", command=update_pokemon)
    btn_load.config(font=("Pocket Monk", 10))
    btn_load.place(x=133, y=560)

    btn_load = tk.Button(window, text="More Options", command=moreoptions)
    btn_load.config(font=("Pocket Monk", 10))
    btn_load.place(x=250, y=580)


def bar():
    l4 = Label(splash_root, text='Loading...', fg='white', bg=a)
    lst4 = ('Helvetica', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=540)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        splash_root.update_idletasks()
        time.sleep(0.0000003)
        r = r + 1

    splash_root.destroy()

    main_window()


a = '#dbd63b'
b1 = Button(splash_root, width=10, height=2, text='START',
            font=('Pocket Monk', '12'), command=bar, border=4,bg='#2a75bb' ,fg='#ffcb05',  relief=RAISED)
b1.place(x=130, y=470)

progress.place(x=-10, y=575)
mainloop()