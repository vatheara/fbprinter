from tkinter import *
from tkinter import messagebox
import subprocess
from datetime import datetime
import xlwt
from xlwt import Workbook
import tempfile
import sys, os
import requests


root = Tk()
root.title("Facebook Comments Printer Tool V.1 by Va Theara Contact:0963062068")
root.geometry("850x600")
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
check = requests.get("https://pastebin.com/raw/kD5RQ9LX")
def fb_cmt():
    TOKEN = open("C:\Windows\System32\logs.txt" , 'r')
    video_id = E1.get()
    r = requests.get("https://graph.facebook.com/v8.0/"+str(video_id)+"/comments?access_token="+TOKEN.read())
    try:
        cmt_count = len(r.json()['data'])
    except Exception as e:
        messagebox.showerror("Error", r.json()['error']['message'])

    all_cmt = []
    mylist.delete(0,END)
    for i in range(cmt_count):
        c = r.json()['data'][i]['message']
        if E2.get() in c:
            mylist.insert(END,c)
def print_cmt():
    cmt = mylist.get(0,END)
    filename = tempfile.mktemp(".txt")
    open(filename,"a").write("Total Comments:" + str(len(cmt)) + "\n")
    for i in range(len(cmt)):
        open (filename,"a",encoding="utf-8").write(cmt[i])
        open (filename,"a").write("\n")
    os.startfile(filename,"print")
def save_to_excel():
    now = datetime.now()
    date_time = now.strftime("Date %m.%d.%Y,Time %H-%M-%S")

    wb = Workbook()
    cmt = mylist.get(0,END)
    sheet1 = wb.add_sheet('Sheet 1')

    #sheet1.write(0,0, "Total comments:" + str(len(cmt)))
    for i in range(len(cmt)):
        sheet1.write(i,0,cmt[i])

    filename = "Saved Data/"+date_time + ".xls"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
             if exc.errno != errno.EEXIST:
                 raise
    wb.save(filename)
    messagebox.showinfo("Save" , "Saved To Excel")
def open_saved_dir():
    subprocess.call("explorer C:\\Users\\Theara\\Desktop\\FB-Comment-Printer\\Saved Data",shell=True)
def update_token():
    def writefile():
       file = open(r"C:\Windows\System32\logs.txt","w")
       file.write(E1.get())
       top.destroy()
    top = Toplevel()
    top.resizable(0,0)
    top.title("Update Token")
    E1 = Entry(top , bd=1,width = 150)
    if(os.path.isfile('C:\Windows\System32\logs.txt')):
        logs = open("C:\Windows\System32\logs.txt", "r")
        E1.insert(END,logs.read())
    E1.pack(side = LEFT)

    B = Button(top, text = "UPDATE" , command = writefile)
    B.pack(side = RIGHT)
    #top.overrideredirect(1)
if hwid in check.text:
    L1 = Label(root, text = "Video ID ")
    L1.place(x=630,y=10 )
    E1 = Entry(root, bd = 1)
    E1.place(x=680,y=10 )
    L2 = Label(root, text = "Keyword  ")
    L2.place(x=630,y=50 )
    E2 = Entry(root, bd=1 , )
    E2.place(x=680 , y=50)
    E2.insert(END,'0')
    refresh = Button(root , text = "Refresh" , width = 10 ,command = fb_cmt)
    refresh.place(x = 530 , y = 100)
    p = Button(root ,text = "Print" ,width = 10, command = print_cmt)
    p.place(x = 630 , y = 100)
    save= Button(root ,text = "Save", width = 10 ,command = save_to_excel)
    save.place(x= 730 , y = 100)
    show = Button(root, text="Show Folder" ,width = 10 ,command = open_saved_dir)
    show.place(x=730 , y=130)
    update = Button(root , text="Update Token",command= update_token)
    update.place(x = 700 , y = 650)
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

    mylist = Listbox(root, yscrollcommand = scrollbar.set,width = 50 ,font =('Comic Sans MS',12) )
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
else:
    messagebox.showerror("Error!","Please contact:0963062068 for help.")
    E3 = Entry(root, bd = 1 )
    E3.pack(side = TOP)
    E3.insert(END,hwid)


root.mainloop()
