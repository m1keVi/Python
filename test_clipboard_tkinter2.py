import tkinter
from tkinter import *
from tkinter.constants import PIESLICE
from PIL import Image, ImageDraw,ImageFont
import qrcode
from tkinter import filedialog


root = tkinter.Tk()
root.title('Generator kodów QR v0.4')
# root.iconbitmap('C:/Users/michal.wolczyk/OneDrive/Python/allegro_favicon.ico')
root.geometry('400x400')


qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,
border=2,
)

lista = []
# save2 = "/Test/"
# root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))


#etykiety
lab = tkinter.Label(root, text = 'Allegro - generator kodów QR')
lab.pack()
lab1 = tkinter.Label(root, text = 'Podaj rozmiar czcionki:')
lab1.place(x=20,y=60)


#fieldy
entry_1 = tkinter.Entry(root, bd = 1, width = 10)
entry_1.place(x=310,y=60)

# # radio button
# var = tkinter.StringVar()


# Rbutton1 = Radiobutton(root, text="Tekst",variable = var, value = "i").pack(side="left")
# Rbutton2 = Radiobutton(root, text="Licznik", variable = var, value = "n").pack(side="right")



with open("test.txt", 'r') as plik:
    for line in plik:
        lista.append(line[:-1])
        continue



def generuj_naklejki_tekst():
    for i in lista:
        n = 0
        n += 1
        qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=11,
        border=2,
        )
        qr.add_data(i)
        qr.make(fit=True)

        image = Image.new( "RGBA", ( 400, 640 ) ,"white")
        img = qr.make_image()
        image.paste(img, (1,2), img.convert("RGBA"))
        print (img.size)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r'c:\windows\fonts\verdana.ttf', int(entry_1.get()))
        # font = ImageFont.load_default()
        txt = i
        draw.multiline_text((80, 480), txt,(0,0,0),font = font, align='center')

        image.save(str(i) + ".png")
    root.destroy()



def generuj_naklejki_liczba():
    n = 0
    for i in lista:
        n += 1
        qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=11,
        border=2,
        )
        qr.add_data(i)
        qr.make(fit=True)

        image = Image.new( "RGBA", ( 400, 640 ) ,"white")
        img = qr.make_image()
        image.paste(img, (1,2), img.convert("RGBA"))
        print (img.size)

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r'c:\windows\fonts\verdana.ttf', int(entry_1.get()))
        # font = ImageFont.load_default()
        txt = i
        draw.multiline_text((80, 480), txt,(0,0,0),font = font, align='center')

        image.save(str(n) + ".png")
    root.destroy()




# #przyciski
b_text = tkinter.Button(root, text = 'WYGENERUJ PLIKI Z NAZWĄ', width = 50, height = 5, command = generuj_naklejki_tekst)
b_text.place(x = 20, y = 210)
b_num = tkinter.Button(root, text = 'WYGENERUJ PLIKI Z LICZNIKIEM', width = 50, height = 5, command = generuj_naklejki_liczba)
b_num.place(x = 20, y = 305)





root.mainloop()
