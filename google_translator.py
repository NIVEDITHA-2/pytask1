from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg=Sor_txt.get(1.0,END)
    text_get=change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,text_get)

root=Tk()
root.title("Translator")
root.geometry("500x700")

lab_txt=Label(root,text="Translator",font=("Times New Roman",20,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)
#SOURCE TEXTBOX
lab_txt=Label(root,text="Source Text",font=("Times New Roman",20,"bold"))
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

#combo box for source
list_text=list(LANGUAGES.values())
comb_sor=ttk.Combobox(frame,value=list_text)
#placement of combobox
comb_sor.place(x=30,y=300,height=40,width=100)
#SET VALUE IN COMBO LIST
comb_sor.set("English")
#to change language
button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)
#for destination
comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=350,y=300,height=40,width=100)
comb_dest.set("English")

lab_txt=Label(root,text="Destination Text",font=("Times New Roman",20,"bold"))
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)






root.mainloop()