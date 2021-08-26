from tkinter import*
from tkinter import filedialog
import png
import pyqrcode
from pyqrcode import QRCode
from PIL import Image ,ImageTk


window = Tk()
window.config(bg='#F25252')
window.title("qrcode generator")
window.minsize(width=900, height=800)
window.maxsize(width=900, height=800)




def generate_qr(name= ".//display.png"):
    global image
    global canvas
    canvas = Canvas(width=300, height=300)
    canvas.grid(row=2,column=2)
    stringIN = textArea.get(1.0,END+"-1c")
    qr = pyqrcode.create(stringIN)
    qr.png(name,scale=strng_var.get())
    qrimage = Image.open(".//display.png")
    new_image = qrimage.resize((300,300))
    new_image.save('.//display.png')
    image = ImageTk.PhotoImage(Image.open(".//display.png"))
    canvas.create_image(152,152,image=image)


def save_qr():
    try:
        filename = filedialog.asksaveasfilename(initialdir='/',title="File save",filetypes=(('PNG FILE','.png'),('all files','*.*')))
        generate_qr(name=str(filename+".png"))
    except:
        pass


textArea = Text(window,height=20,width=65,bd = '4')
textArea.grid(row = 2,column = 1,padx = 20,pady=10)


generatBUtton = Button(window,text="Generat",width=30,height=1,bd = '4',command=generate_qr)
generatBUtton.grid(row=4,column=1)


saveButton = Button(window,text="Save",width=30,height=1,bd = '4',command=save_qr)
saveButton.grid(row=4,column=2)

strng_var = StringVar(window)
choices = { 1,2,3,4,5,6,7,8,9,10}
strng_var.set(5)

window.mainloop()