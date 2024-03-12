import tkinter as tk
from tkinter import *
import qrcode

window = tk.Tk()

window.title("QR code generator")

label = tk.Label(
    text="Type your link")
label.pack()

entry = tk.Entry()
entry.pack()

label2 = tk.Label(
    text="Save as")
label2.pack()

entry2 = tk.Entry()
entry2.pack()


def generate_qr():
    content = entry.get()
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(content)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    filename = entry2.get() + '.png'
    img.save(filename)


button = tk.Button(
    text="Generate QR",
    width=10,
    height=3,
    command=generate_qr
)
button.pack()

canvas = Canvas(window, width=300, height=300)
canvas.pack()

photo = tk.PhotoImage(file='')
image = tk.Label(window, image=photo)
image.pack()

window.mainloop()
