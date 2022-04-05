from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='Lucida 20 ').place(x= 85,y= 40)


link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Lucida 15 ').place(x= 160 , y = 100)
link_enter = Entry(root, width = 60,textvariable = link).place(x = 75, y = 150



def Downloader():     
    url1 =YouTube(str(link.get()))
    video = url1.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'Lucida 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'Lucida 15 ' ,bg = 'light green', padx = 2, command = Downloader).place(x=180 ,y = 190)

root.mainloop()