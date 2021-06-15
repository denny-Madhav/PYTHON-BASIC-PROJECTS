import tkinter

window = tkinter.Tk()
window.title("My first GUI program with python")
window.minsize(width = 600, height = 400)


#lable
ml = tkinter.Label(text="HMM",font=("lato",16,"bold"))
ml.pack(side = "left")

#update lable
ml["text"] = "New Text"
ml.config(text = "New Text")

#button
def button_clicked():
    print("i got clicked")
    it=input.get()
    ml.config(text = it)


button = tkinter.Button(text = "Click Me",command = button_clicked)
button.pack()

#Entry

input = tkinter.Entry(width="20")
input.pack()


window.mainloop()