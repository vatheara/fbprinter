from tkinter import *
import tempfile
import os
import requests

root = Tk()
root.geometry("900x600")
def fb_cmt():
    TOKEN = "EAAEDHsLYgpUBAOoOargWFsAFKTmcs3AgvZAE8axX2Qr2ZArCC8HK2yxc2ZBZCqVHFP8p1vKqLZCIAp3aGLKsfcj6TNAWCGCxRMc6wxJbTphOF0ZAHfoaUuLrXmPzyVwY8ieQGPcPr0RV5kwE7nR0VUuGtbH8BfljJqnpkGt2VSxwZDZD"
    video_id = E1.get()
    r = requests.get("https://graph.facebook.com/v8.0/"+str(video_id)+"/comments?access_token="+TOKEN)
    cmt_count = len(r.json()['data'])
    all_cmt = []
    mylist.delete(0,END)
    for i in range(cmt_count):
        c = r.json()['data'][i]['message']
        mylist.insert(END,c)
def print_cmt():
    cmt = mylist.get(0,END)
    filename = tempfile.mktemp(".txt")
    for i in range(len(cmt)):
        open (filename,"a",encoding="utf-8").write(cmt[i])
        open (filename,"a").write("\n")
    os.startfile(filename,"print")


L1 = Label(root, text = "Video ID ")
L1.place(x=650,y=10 )
E1 = Entry(root, bd = 5)
E1.place(x=700,y=10 )
refresh = Button(root , text = "Refresh" , command = fb_cmt)
refresh.place(x = 700 , y = 50)
p = Button(root ,text = "Print" , command = print_cmt)
p.place(x = 800 , y = 50)

m = Menu(root, tearoff=0)
m.add_command(label = "Paste")
def do_popup(event):
    e_widget = event.widget
    try:
        m.entryconfigure("Paste",command=lambda: e_widget.event_generate("<<Paste>>"))
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

E1.bind_class("Entry","<Button-3><ButtonRelease-3>", do_popup)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set,width = 90 )
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
