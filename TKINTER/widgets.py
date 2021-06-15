import tkinter

window = tkinter.Tk()
window.title("Widgets")
window.minsize(width= 600, height= 400)
#lable
ml = tkinter.Label(text="This is new text")
ml.pack()
#button
bt = tkinter.Button(text="Click me")
bt.pack()
#input
ip = tkinter.Entry(width=30)
ip.insert(index=0, string="some Text To Begin With")
print(ip.get())
ip.pack()
#text area
ta= tkinter.Text(height=5, width=30)
ta.focus()
ta.insert(index="END",chars="Example of multiline text entry.")
print(ta.get())
ta.pack()
















window.mainloop()