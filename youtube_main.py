import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk, Image  
from tkinter import filedialog
class Youtube1:
    def __init__(self,win):
        self.win=win
        self.win.title("Welcome To Youtube Audio and Video downloader")
        self.win.geometry("450x400+450+100")
        self.win['background']='#8B0000'
        
        self.img = Image.open("./YouTube.jpg")
        self.img1 = self.img.resize((450, 160), Image.ANTIALIAS)
        self.back1=ImageTk.PhotoImage(self.img1)
        self.l1=tk.Label(self.win,image=self.back1)
        self.l1.place(x=0,y=0)
        
        self.l1=tk.Label(self.win,text="Enter link/s:",background='#8B0000',fg="white",font=("Georgia",10))
        self.l1.place(x=10,y=170)
        self.l2=tk.Label(self.win,text="(if you want to",background='#8B0000',fg="white",font=("Georgia",10))
        self.l2.place(x=10,y=190)
        self.l3=tk.Label(self.win,text="multiple youtube audio",background='#8B0000',fg="white",font=("Georgia",10))
        self.l3.place(x=10,y=210)
        self.l4=tk.Label(self.win,text="hit enter and paste the link)",background='#8B0000',fg="white",font=("Georgia",10))
        self.l4.place(x=10,y=230)
        self.link=tk.Text(self.win,height=5,width=30)
        self.link.place(x=185,y=170)
        
        self.which=tk.Label(self.win,text="Select the audio type you want to download audio/music:",background='#8B0000',fg="white",font=("Georgia",10))
        self.which.place(x=10,y=280)

        self.var = IntVar()
        self.r1 = Radiobutton(self.win, text="Download Only Audio", variable=self.var, value=1,\
                  command=self.sel,font=("Georgia",10),fg="#ad6f69",bg='#8B0000')
        self.r1.place(x=10,y=300)

        self.r2 = Radiobutton(self.win, text="Download video", variable=self.var, value=2,\
                  command=self.sel,font=("Georgia",10),fg="#ad6f69",bg='#8B0000')
        self.r2.place(x=180,y=300)


        self.d=tk.Button(self.win,text="Download",command=self.download1,font=("Georgia",10))
        self.d.place(x=160,y=350)

        self.b=tk.Button(self.win,text="Exit",command=self.exit,font=("Georgia",10))
        self.b.place(x=250,y=350)

    def exit(self):
        self.win.destroy()
    def sel(self):
        self.c=self.var.get() 
        if self.c==1:
            self.c=1
        else :
            self.c=2
    def download1(self):  
        if self.c==1:
            self.links=self.link.get("1.0",END)
            self.links_list=self.links.splitlines()

            for link in self.links_list:
                try:
                    self.yt = YouTube(link) 
                    self.video = self.yt.streams.filter(only_audio=True).first()
                    self.dir_name = filedialog.askdirectory()
                    self.out_file = self.video.download(output_path=self.dir_name)
                    self.base, self.ext = os.path.splitext(self.out_file)
                    new_file = self.base +"."+ "mp3"
                    os.rename(self.out_file, new_file)
                    messagebox.showinfo("Success","Audio/Music has been downloaded")
                    self.link.delete('1.0', END)
                    self.var.set(None)
                except: 
                    messagebox.showerror("Error","Connection Error")
                    self.link.delete('1.0', END)
                    self.var.set(None)
        else:
            self.links=self.link.get("1.0",END)
            self.links_list=self.links.splitlines()

            for link in self.links_list:
                try:
                    self.yt = YouTube(link)
                    self.video = self.yt.streams.get_highest_resolution()
                    self.dir_name = filedialog.askdirectory()
                    self.out_file = self.video.download(output_path=self.dir_name)
                    self.base, self.ext = os.path.splitext(self.out_file)
                    new_file = self.base +"."+ "mp4"
                    os.rename(self.out_file, new_file)
                    messagebox.showinfo("Success","video has been downloaded")
                    self.link.delete('1.0', END)
                    self.var.set(None) 
                except: 
                    messagebox.showerror("Error","Connection Error")
                    self.link.delete('1.0', END)
                    self.var.set(None)
            
win=Tk()
app=Youtube1(win)
win.mainloop()