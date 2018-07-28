from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from main import main
import math
import sys
from onefile import *

def center_window(win, width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    win.geometry('%dx%d+%d+%d' % (width, height, x, y))

def convertionStart():
    pack = filedialog.askopenfilename(initialdir = "./",title = "Select Pack",filetypes = (("resource pack","*.zip"),("all files","*.*")))
    if(pack):

        root.withdraw()
        '''progress_win = tk.Toplevel(root)
        center_window(progress_win, 270, 60)
        display = tk.Label(progress_win, text="Humm, see a new window !").pack()
        downloaded = tk.IntVar()
        downloaded.set(50)
        mpb = ttk.Progressbar(
            progress_win,
            orient ="horizontal",
            maximum = 100,
            variable = downloaded,
            mode ="determinate").pack(fill=tk.BOTH)'''

        main(pack[:-4], res_r.get())

        root.deiconify()
        #progress_win.withdraw()
        messagebox.showinfo(title='success', message='conversion is done!')
    else:
        print ('select pack to start conversion')

def show_values(value=None):
    slider_label['text'] = text='resolution: '+ str(int(16 * math.pow(2, res_r.get()-1))) + 'X'
    #print (res_r.get())

root = tk.Tk()
root.title("fit to 1.13 tool")
#root.geometry('500x300+500+200')
root.iconbitmap(resource_path('favicon.ico'))
root.resizable(width=False, height=False)
center_window(root, 270, 80)

''' resolution ratio set'''
res_r = tk.IntVar()
res_r.set(1)
slider_res = tk.PanedWindow()
slider_res.pack(fill = tk.BOTH, expand = 1)
slider_label = tk.Label(root, text='resolution: 16X')
slider_scale = tk.Scale(
    root,
    from_=0,
    to=6,
    orient=tk.HORIZONTAL,
    variable = res_r,
    command=show_values
    )
slider_res.add(slider_label)
slider_res.add(slider_scale)

btn_start = tk.Button(
    root,
    text='Select Pack',
    width=60,
    command=convertionStart
    ).pack()

root.mainloop()
