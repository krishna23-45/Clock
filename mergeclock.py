from tkinter import *

from PIL import ImageTk,Image,ImageDraw
from datetime import *
import time
from math import *


class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()
        self.minsize(1350,700)
        self.wm_iconbitmap("favicon.ico")
        self.title("\t\t\t\t\thello")
       
        self.import_images()
        self.label12 = Label(self,bg='#000d1a',bd=10,relief=RAISED)
        self.label12.place(x=100,y=100,height=400,width=400)
        self.clockin()
        self.label_min()
        
        
        
    def import_images(self):
        self.phone_images = ImageTk.PhotoImage(file='images/L1.png')
        self.lbl_phone_images = Label(self,image=self.phone_images).place(x=-3,y=-3)

    def clock_label(self,h1,m1,s1):
        self.clock_l = Image.new('RGB',(400,400),(255,255,255))
        self.draw = ImageDraw.Draw(self.clock_l)
        self.bg = Image.open('images/s.jpg')
        k = self.bg.resize((300,300),Image.ANTIALIAS)
        self.clock_l.paste(k,(50,50))


        self.origin = 200,200
        #h
        self.draw.line((self.origin,200+50*sin(radians(h1)),200-50*cos(radians(h1))),fill='black',width=3)
        #m
        self.draw.line((self.origin,200+80*sin(radians(m1)),200-80*cos(radians(m1))),fill='blue',width=4)

        self.draw.line((self.origin,200+100*sin(radians(s1)),200-100*cos(radians(s1))),fill='green',width=3)
        self.draw.ellipse((195,195,210,210),fill='green',width=3)
        self.clock_l.save("12.png")


    def clockin(self):
        self.raw = datetime.now()
        self.h = self.raw.hour
        self.m = self.raw.minute
        self.s = self.raw.second
        self.hr = (self.h/12)*360
        self.mi = (self.m/60)*360
        self.se = (self.s/60)*360
        self.clock_label(self.hr,self.mi,self.se)
        self.img1 = ImageTk.PhotoImage(file="12.png")
        self.label12.config(image=self.img1)
        self.label12.after(200,self.clockin)

    def label_min(self):
    
        self.lbl_hour = Label(text="12",bg="#0875B7",fg="white",font=('times new roman',50,"bold"))
        self.lbl_hour.place(x=570,y=150,width=150,height=180)
        self.lbl_hour2 = Label(text="Hour",bg="#0875B7",fg="white",font=('',20,"bold"))
        self.lbl_hour2.place(x=570,y=340,width=150,height=60)


        self.lbl_min = Label(text="12",bg="#008EA4",fg="white",font=('times new roman',50,"bold"))
        self.lbl_min.place(x=750,y=150,width=150,height=180)
        self.lbl_min2 = Label(text="Minute",bg="#008EA4",fg="white",font=('',20,"bold"))
        self.lbl_min2.place(x=750,y=340,width=150,height=60)



        self.lbl_sec = Label(text="12",bg="#DF002A",fg="white",font=('times new roman',50,"bold"))
        self.lbl_sec.place(x=920,y=150,width=150,height=180)
        self.lbl_sec2 = Label(text="Second",bg="#DF002A",fg="white",font=('',20,"bold"))
        self.lbl_sec2.place(x=920,y=340,width=150,height=60)

        self.lbl_noon = Label(text="df",bg="green",fg="white",font=('times new roman',50,"bold"))
        self.lbl_noon.place(x=1090,y=150,width=155,height=180)
        self.lbl_noon2 = Label(text="AM",bg="green",fg="white",font=('',14,"bold"))
        self.lbl_noon2.place(x=1090,y=340,width=155,height=60)


        self.clock12()



    def clock12(self):
        self.raw = datetime.now()
        self.h = self.raw.hour
        self.m = self.raw.minute
        self.s = self.raw.second

        
        self.lbl_min.config(text=self.m)
        self.lbl_sec.config(text=self.s)


            
        if self.h>=0 and self.h<12:
            self.lbl_noon2.config(text="Good Morning")

        elif self.h>=12 and self.h<18:
            self.lbl_noon2.config(text="Good Afternoon") 

        elif self.h > 18 and self.h > 20:
            self.lbl_noon2.config(text="Good Evening")   

        if self.h > 12:
            self.times = str(self.h - 12 )
            self.lbl_hour.config(text=self.times)
            self.lbl_noon.config(text="PM")
        elif self.h < 12:
            self.he  = str(self.h)
            self.lbl_hour.config(text=self.he)
            self.lbl_noon.config(text="AM")

        self.lbl_sec.after(200,self.clock12)
        
        
window = Window()
window.mainloop()