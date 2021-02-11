'''This is a GUI created by Shikhar Kothari, NEOS
to help people by letting them downloading youtube videos fast and easily.'''

try:
    from pytube import YouTube
    from pytube import Playlist
    from tkinter import *
    from tkinter import messagebox as tmsg
    from tkinter.ttk import Progressbar
    import os
except Exception as e:
    tmsg.showinfo(title="Oops!", message="Something went wrong:(")


root = Tk()
root.geometry("320x230")
root.title("Youtube Downloader - NEOS")
root.minsize(320, 230)
root.maxsize(320, 230)

def show_progress_bar(stream, _chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = int((current*200)//1)
    progress['value']=percent
    root.update_idletasks()

#https://youtu.be/I4kVgqRqPsA

def download_vid(*args):
    option_type = var.get()
    url = linkentry.get()
    try:

        if option_type == options[0]:
            yt = YouTube(url)
            yt.register_on_progress_callback(show_progress_bar)
            yt.streams.filter(adaptive=True).first().download()
            tmsg.showinfo(title="Yay!", message="Video has been downloaded!")

        elif option_type == options[1]:
            yt = YouTube(url)
            yt.register_on_progress_callback(show_progress_bar)
            yt.streams.filter(file_extension='mp4').first().download()
            tmsg.showinfo(title="Yay!", message="Video has been downloaded!")

        elif option_type == options[2]:
            yt = YouTube(url)
            yt.register_on_progress_callback(show_progress_bar)
            yt.streams.filter(progressive=True).first().download()
            tmsg.showinfo(title="Yay!", message="Video has been downloaded!")

        elif option_type == options[3]:
            ytd = YouTube(url, on_progress_callback=show_progress_bar).streams.filter(only_audio=True).first().download()
            base = os.path.splitext(ytd)[0]
            os.rename(ytd, base + '.mp3')
            tmsg.showinfo(title="Yay!", message="Audio/song has been downloaded!")

        else:
            tmsg.showinfo(title="Oops", message="Something went wrong.\nYou can contact us at\nneos.company@gmail.com")

    except Exception as e:
        tmsg.showinfo(title="Oops", message="Check your network connection!")


#Heading
Label(root, text="YT Video Downloader", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)



# Video Link  ______________________
ytlink = Label(root, text="Video Link", pady=7, padx=20)
ytlink.grid(row=1, column=2)



#Entry box for link or URL
linkvalue = StringVar()
linkentry = Entry(root, textvariable=linkvalue)
linkentry.grid(row=1, column=3, ipadx=38)




#option label
op_label = Label(text="Options")
op_label.grid(row=2, column=2)



#progress label
pro_label = Label(text="Progress")
pro_label.grid(row=3, column=2)



#Option Menu - To give option to download various streams
# name = Label(root, text="Whatever")
# name.grid(row=2, column=3)
options = ["Best Quality", "Average Quality", "Data Saver", "Audio/Song"]
var = StringVar()
var.set(options[1])
option_menu = OptionMenu(root,var, options[0],options[1],options[2],options[3])
option_menu.grid(row=2, column=3, ipadx=37, pady=8, sticky="ew")




#Progress bar
progress = Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
progress.grid(row=3, column=3)




#Button & packing it and assigning it a command
Button(text="Download", font="comicsansms 13", command=download_vid, width=21, height=2).grid(row=4, column=3, pady=10, sticky="ew")

root.mainloop()