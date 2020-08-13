from tkinter import *
kg=Tk()
kg.title("CONVERTION")
A=Label(kg,text="KG")
A.grid(row=0,column=0)
entryval=StringVar()
entry=Entry(kg,textvariable=entryval,width=20)
entry.grid(row=0,column=1)

#functions

def convertions():
    grams = float(entry.get()) / 1000
    pounds = float(entry.get()) * 2.2046
    ounces = float(entry.get()) / 0.02834952
    box1.insert(END,grams)
    box2.insert(END,pounds)
    box3.insert(END,ounces)
    
convert=Button(kg,text="Convert",command=convertions)
convert.grid(row=0,column=2)

box1=Text(width=20,height=1)
box1.grid(row=1,column=0)
box2=Text(width=20,height=1)
box2.grid(row=1,column=1)
box3=Text(width=20,height=1)
box3.grid(row=1,column=2)



    


