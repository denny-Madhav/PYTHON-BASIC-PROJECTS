from tkinter import *

window = Tk()
window.title("M TO KM")
window.config(padx=10, pady=10)

def miles_to_kilo():
    miles = float(mi.get())
    kmm = miles * 1.609
    km.config(text=f"{int(kmm)}")

mi = Entry()
mi.grid(column=2,row=0)
ml = Label(text="Miles")
ml.grid(column=1,row=0)

eq = Label(text="is equal to")
eq.grid(column=1,row=1)
km = Label(text = "0")
km.grid(column=2,row=1)
kml = Label(text=" KM")
kml.grid(column=3,row=1)
cb = Button(text="CALCULATE",command=miles_to_kilo)
cb.grid(column=2,row=2)








window.mainloop()