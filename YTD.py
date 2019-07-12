from tkinter import  *
from tkinter import filedialog
import os
import youtube_dl

window = Tk()

window.title('Yourube Video Downloader ')
window.configure(background = 'cyan')
window.geometry('1280x720')
window.iconbitmap('youtube_icon.ico')
window.state('zoomed')
folder_path = StringVar()

def clear():
    url.delete(first =0, last=100)

def browse_Button():
    global folder_path
    global file_name
    file_name=filedialog.askdirectory()
    folder_path.set(file_name)

def downloading():
    # try:
        URL = url.get()
        PATH = path.get()
        ydl_opt = {}
        os.chdir(PATH)
        with youtube_dl.YoutubeDL(ydl_opt) as ydl:
            window.title('Dowbloading...'+ URL)
            ydl.download([URL])
        print(ydl_opt)
        noty = 'Your video downloded'
        window.title(noty)
        Notification.configure(text=noty, fg='black', bg="SpringGreen3", width=50, font=('times', 17, 'bold', 'italic'))
        Notification.place(x=350, y=500)
    # except Exception as e:
    #     print(e)

eYLH = Label(window, text='Enter Youtube Link here', width=30, fg='Black', bg='yellow', height=2, font=('times', 15, 'bold '))
eYLH.place(x=150, y=100)

url = Entry(window,width = 35,fg = 'red', bg = 'yellow',font=('times', 25, 'bold '))
url.place(x = 410 , y =100)

Clbutton = Button(window,text = 'Clear', command=clear, width =28, fg = 'red',font=('times', 25, 'bold '))
Clbutton.place(x = 900, y= 105)


eSP = Label(window, text='Enter Save Path', width=30, fg='Black', bg='yellow', height=2, font=('times', 15, 'bold '))
eSP.place(x=150, y=200)

path = Entry(window,width = 35,fg = 'red', textvariable=folder_path, bg = 'yellow',font=('times', 25, 'bold '))
path.place(x = 410 , y =200)

saveButton = Button(window,text = 'Save', command=browse_Button, width =28, fg = 'red',font=('times', 25, 'bold '))
saveButton.place(x = 900, y= 205)

dYtube = Button(window,text = 'Download', command=downloading, width =28, fg = 'red',font=('times', 25, 'bold ') )
dYtube.place(x = 490,y = 280)

Notification = Label(window, text="Video downloaded", bg="Green", fg="white", width=35, height=3, font=('times', 17, 'bold'))

window.mainloop()
