import tkinter, PyPDF2
from tkinter import filedialog 
















root = tkinter.Tk()
root.title("PDF Text Extractor")


filename_label = tkinter.Label(root, text="No File Selected")
outputfile_text = tkinter.Text(root)


filename_label.pack()
outputfile_text.pack()


root.mainloop()