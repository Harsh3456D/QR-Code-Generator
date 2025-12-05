import qrcode
import time
import sys
from tkinter import *
from PIL import Image, ImageTk

def generate():
    global name
    global url_entry
    def slow_type(text, speed=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
    
    name = ETname.get()
    url = url_entry.get()
    filePath = f"output\\{name}.png"
    print(f"Your file --> {name} is getting processed")
    
    qr = qrcode.QRCode()
    qr.add_data(url)
    image = qr.make_image()
    image.save(filePath)
    
    print(f"Your QRcode | {name}.png | is now generated \n-- Kindly check the output folder. ")




QRgenerator = Tk()
QRgenerator.geometry("420x420")
QRgenerator.title("QR Code Generator -- Harsh")

photo = Image.open('Harsh_github.png')
resized_img = photo.resize((100,100), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(resized_img)

icon = PhotoImage(file='logo.png')
QRgenerator.iconphoto(True, icon)

QRgenerator.config(background='Black')

TopLabel = Label(QRgenerator, text='QR Code Generator By Harsh',
                 font=('Arial', 16, 'bold'), background="black",
                 fg='White', image=tk_image, compound='bottom')
TopLabel.pack()

ETname= Entry(QRgenerator, font='Arial')
ETname.place(x=125, y=150)
url_entry= Entry(QRgenerator, font='Arial')
url_entry.place(x=125, y=250)

button = Button(QRgenerator, text="Generate",
                font='Arial', fg='white',
                background="grey", activebackground='white',
                activeforeground='grey', command=generate)
button.place(x=175, y=340)

Label = Label(QRgenerator, text='Kindly check the output folder afterwards',
                 font=('Arial', 16, 'bold'), background="black",
                 fg='White', image=tk_image, compound='bottom')
Label.place(x=175, y=280)
QRgenerator.mainloop()

