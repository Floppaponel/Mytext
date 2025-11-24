import tkinter as tk
from tkinter import NW, font
from tkinter import filedialog,END 
from tkinter.filedialog import asksaveasfilename
from tkinter.scrolledtext import ScrolledText
from tkinter import colorchooser
from PIL import Image, ImageTk
my_w = tk.Tk()
my_w.title("MyText")
my_w.geometry("500x350")
init_dir='D:\\testing\\file-menu\\'
global file_name
custom_font = font.Font(family="Arial", size=12, weight="bold")
tt1 = font.Font(family="Arial", size=48, weight="bold")
t2 = font.Font(family="Arial", size=16, weight="bold")
t3 = font.Font(family="Arial", size=8, weight="bold")
ScrolledText_font = font.Font(family="Arial", size=35, weight="bold")
Vers = "0.0.0.1a"
new_file_img = Image.open("new_file.png")
img = ImageTk.PhotoImage(Image.open("favicon.png"))
my_w.iconphoto(False, img)
EditText_HelloWorld = "Hello World!"
labelVer = tk.Label(my_w, text=f"My Text - {Vers}", font=t2).pack(anchor=NW, padx=10, pady=10)
panel = tk.Label(my_w, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
t1 = ScrolledText(my_w, font=ScrolledText_font)
t1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

def windowC():
    window = tk.Tk()
    window.title("My Text - Edit Text")
    window.geometry("250x200")
    window.iconphoto(False, img)
    label = tk.Label(window, text=f"{EditText_HelloWorld}")
    label.pack(anchor=NW, padx=10, pady=10)
    def font_changed(font):
        label["font"] = font
        t1["font"] = font
 
    def select_font():
        window.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", window.register(font_changed))
        window.tk.call("tk", "fontchooser", "show")

    def select_color():
        result = colorchooser.askcolor(initialcolor="black")
        label["foreground"] = result[1]
        t1["foreground"] = result[1]
 
    open_button1 = tk.Button(window, text="Выбрать цвет", command=lambda:select_color())
    open_button1.pack(anchor=NW, padx=10, pady=11)

    open_button = tk.Button(window, text="Выбрать шрифт", command=lambda:select_font())
    open_button.pack(anchor=NW, padx=10, pady=10)

def new_file():
    global file_name     
    file_name='untitled.txt'
    my_w.title(file_name)

def open_file():
    file = filedialog.askopenfilename(filetypes=[("txt file", ".txt")],defaultextension=".txt",initialdir=init_dir)
    global file_name     
    file_name=file
    my_w.title(file_name)
    fob=open(file,'r')
    my_str1=fob.read()
    t1.delete('1.0',END)
    t1.insert(tk.END, my_str1)
    fob.close()

def save_file():
    global file_name
    if(file_name=='untitled.txt'):
        save_as_file()
    else:
        fob=open(file_name,'w')
        my_str1=t1.get("1.0",END)
        fob.write(my_str1)

def save_as_file():
    file = filedialog.asksaveasfilename(
        filetypes=[("txt file", ".txt")],
        defaultextension=".txt",initialdir=init_dir)
    if file:
        fob=open(file,'w')
        my_str1=t1.get("1.0",END)
        fob.write(my_str1) 
        my_w.title(file)
        fob.close()
    else:
        print("No file chosen")

def close_file():
    save_file()
    t1.delete('1.0',END)
    my_w.title('')


menubar = tk.Menu(my_w)

menu_f = tk.Menu(menubar,title='my title',tearoff=0)
menu_d = tk.Menu(menubar,title='my title',tearoff=0)
menu_g = tk.Menu(menubar,title='my title',tearoff=0)
settings_menu = tk.Menu()

menubar.add_cascade(label="View", menu=menu_d)
menubar.add_cascade(label="File", menu=menu_f)
# menubar.add_cascade(label="App", menu=menu_g)

menu_d.add_command(label="Text", command=lambda:windowC())
# menu_d.add_cascade(label="Language", menu=settings_menu)
# settings_menu.add_command(label="Ru")
# settings_menu.add_command(label="Eng")
# menu_g.add_command(label="Credits", command=lambda:windowD())
menu_f.add_command(label="New", command=lambda:new_file(), foreground="#28580B", font=custom_font)
menu_f.add_command(label="Open...", command=lambda:open_file())  
menu_f.add_command(label="Save", command=lambda:save_file())
menu_f.add_command(label="Save As...", command=lambda:save_as_file())
menu_f.add_command(label="Close", command=lambda:close_file(), foreground="#981616")
menu_f.add_command(label="Exit", command=my_w.quit, foreground="#981616")
my_w.config(menu=menubar)
my_w.mainloop()