from tkinter import *
from tkinter import ttk as tk
from tkinter import filedialog
from pytube import YouTube

# --------------------------------- Code -------------------------------
Folder_name = ""


def openlocation():

    global Folder_name
    Folder_name = filedialog.askdirectory()
    if len(Folder_name) > 1:
        p_error.config(text=Folder_name, fg="grey")

    else:
        p_error.config(text="Please choose Folder.!!", fg="red")


def DownloadVideo():
    choice = res_choice.get()
    url = entry.get()

    if len(Folder_name) > 1:
        s_error.config(text=" ")
        yt = YouTube(url)
        if choice == resolutions[0]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == resolutions[1]:
            select = yt.streams.filter(progressive=True).last()

        elif choice == resolutions[2]:
            select = yt.streams.filter(only_audio=True).first()

        else:
            s_error.config(text="please enter a valid link.!!",fg='red',font=20)

    select.download(Folder_name)
    done_txt.config(text=" --- Download has been completed --- ",fg="grey")


# --------------------------------- UI -------------------------------

window = Tk()
window.title('YouTube video downloader')
window.geometry("420x420")
window.config(bg='black')
window.columnconfigure(0, weight=1)


# Space
space_0 = Label(window, text=" ", bg='black')
space_0.grid()

# Title
search = Label(window, text="YouTube Video Downloader",font=35)
search.grid()


# Space
space_01 = Label(window, text=" ", bg='black')
space_01.grid()

# Search label
search = Label(window, text="Enter the URL of the video", bg='black', fg='white')
search.grid()

# Search box
entry = StringVar()
entry = Entry(window, width=60, textvariable=entry)
entry.grid()

# Error message
s_error = Label(window, text=".............", bg='black')
s_error.grid()

# Space
space_1 = Label(window, text=" ", bg='black')
space_1.grid()


# save file path
save_p = Button(window, width=25, height=2, bg="red", fg="white", text="Choose path to save file", command=openlocation)
save_p.grid()

# Error message
p_error = Label(window, text=".............",bg='black')
p_error.grid()

# Space 2
space_2 = Label(window, text=" ", bg='black')
space_2.grid()


# Quality label
quality = Label(window, text="Select Quality", bg='black', fg='white')
quality.grid()

# selection drop box.
resolutions = ['High', 'Low', 'Only Audio']
res_choice = tk.Combobox(window, values=resolutions)
res_choice.grid()

# Space 3
space_3 = Label(window, text=" ", bg='black')
space_3.grid()

# download button.
download = Button(window, width=25, height=3, bg="blue", fg="white", text="Download", font=30, command=DownloadVideo)
download.grid()

# download done
done_txt = Label(window, text=" ", font=25, bg='black')
done_txt.grid()


window.mainloop()

