

from tkinter import *
from tkinter.messagebox import showerror, askyesno
from PyDictionary import PyDictionary




window =Tk()
window.title("English Dictionary")

window.minsize(700,300)

window.iconbitmap("dict1.ico")

def close_window():
    if askyesno(title="Close Dictionary ",message="Are you sure close the dictionary ?"):
        window.destroy()

def kelimeyi_ara():
    kelime=kelime_girisi.get()
    if kelime=="":
        showerror(title="Error Message ",message="Please enter word you want to find!!")
    else:
        try:
            sozluk=PyDictionary()
                
            kelime_anlami=sozluk.meaning(kelime)
            #print(kelime_anlami)
            kelime_aciklama.delete(1.0,END)
            kelime_aciklama.insert('1.0',kelime_anlami)
            kelime_etiketi2=Label()
            kelime_etiketi2.grid(row=2,column=4)
            kelime_etiketi2.config(text=kelime)
        except:
            showerror(title="error message",message="error occur, please control your arguments!! ")


kelime_etiketi=Label(text="Enter Your Word  :")
kelime_etiketi.grid(row=1,column=1,padx=10,pady=10)
kelime_girisi=Entry()
kelime_girisi.grid(row=1,column=4)

aciklama_etiketi=Label(text="Meaning of word  :")
aciklama_etiketi.grid(row=3,column=1)

baslik_eiketi=Label(text="English Dictionary ",font=("Times",18))  
baslik_eiketi.grid(row=0,column=4)

kelime_aciklama=Text(width=50,height=5)
kelime_aciklama.grid(row=3,column=4)

kelime_ara_button=Button(text="Search",command=kelimeyi_ara)
kelime_ara_button.grid(row=5,column=3)


window.protocol("WM_DELETE_WINDOW",close_window)

window.mainloop()