from tkinter import *
from pytube import YouTube
# importing YouTube module from pytube Umport YouTube # initlalizing tkinter 
root = Tk ()  
root.geometry ("450x380") 
# title of the GUI App
root.title (" YouTube Downloder") 
root.configure(bg="skyblue")
# defining download function 
def download (): 
# using try and except to execute program without errors 
    try: 
        myVar, set (" Downloading ... ") 
        root. update () 
        YouTube (link.get () ) .streams.first (). download () 
        link. set ("Video downloaded successfully") 
    except Exception as e:
        myVar, set ("Mistake") 
        root.update () 
        link. set ("Enter correct link") 
# created the Label widget to wetcome user 
Label (root,text = "Welcome to youtube Downloader Application", font = "Consolas 15 bold",bg="yellow"). pack () 
# declaring StringVar type 
myVar = StringVar () 
# setting the default text to myvar 
myVar.set ("Enter the link below") 
# created the Entry widget to ask user to enter the url 
Entry (root, textvariable = myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link,width=40).pack(pady=10)
Button(root, text="Download video", command=download).pack()
root.mainloop()