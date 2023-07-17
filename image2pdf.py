#a modified pain in the ass img2pdf from geeks4geeks
#import pdf2image
import tkinter
import tkinter as tk
from tkinter import filedialog as fd
import img2pdf
window = tkinter.Tk()
window.geometry('500x400')

def select_file():
    global file_names
    file_names = fd.askopenfilenames(initialdir = "/",
                                     title = "Select Files")
#IMAGE TO PDF
def image_to_pdf():
    for index, file_name in enumerate(file_names):
        with open(f"file {index}.pdf", "wb") as f:
            f.write(img2pdf.convert(file_name))

#IMAGES TO PDF
def images_to_pdf():
    with open(f"file.pdf", "wb") as f:
        f.write(img2pdf.convert(file_names))

tk.Label(window, text = "Image Conversion",
         font = "italic 15 bold").pack(pady=10)

tk.Button(window, text = "Select Images",
          command=select_file, font=14).pack(pady=10)

frame = tkinter.Frame()
frame.pack(pady=20)

tk.Button(frame, text = "Image to PDF",
          command=image_to_pdf,
          relief="solid",
          bg="white",font=15).pack(padx=10)

tk.Button(frame, text = "Images to PDF",
          command=images_to_pdf,
          relief="solid",
          bg="white",font=15).pack(padx=10)

window.mainloop()
