import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import socket
import os

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.resizable(False,False)
    window.configure(bg="#f4fdfe")
    
    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("waiting for any connection......")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted!")


    def selectFile():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='select file',
                                            filetypes=(("text files",'.txt'),('all files','*.*')))
    
    icon_image=PhotoImage(file="images/Send.png")
    window.iconphoto(False,icon_image)
    sbackground=PhotoImage(file="images/sender.png")
    Label(window,image=sbackground).place(x=-2,y=0)
    s2background=PhotoImage(file="images/id.png")
    Label(window,image=s2background).place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg="white",fg="black").place(x=140,y=290)
    
    Button(window,text="+Select file",width=10,height=1,font='arail 14 bold',bg="#fff",fg="#000",command=selectFile).place(x=160,y=150)
    Button(window,text="Send",width=8,height=1,font='arail 14 bold',bg="#000",fg="#fff",command=sender).place(x=300,y=150)

    window.mainloop()

def Receive():
    main=Toplevel(root)
    main.title("Recieve")
    main.geometry("450x560+500+200")
    main.resizable(False,False)
    main.configure(bg="#f4fdfe")

    def Receiver():
        try:
            r = socket.socket()
            port = 8080
            ID = senderID.get()
            fileinf = fileData.get()
            r.connect((ID, port))
            file = open(fileinf, 'wb')
            file_data = r.recv(1024)
            file.write(file_data)
            file.close()
            print("File has been received!")
        except socket.gaierror as e:
            messagebox.showerror("Error", f"Failed to connect: {e}")
    
    rbackground=PhotoImage(file="images/receiver.png")
    Label(main,image=rbackground).place(x=-2,y=0)
    rlogo=PhotoImage(file="images/profile.png")
    Label(main,image=rlogo,bg="#f4fdfe").place(x=10,y=250)

    Label(main,text="Receive",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)

    Label(main,text="Input sender id ",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340) 
    senderID=Entry(main,width=25,fg="black",border=2,font=('arial',15),bg='white')
    senderID.place(x=20,y=370)
    senderID.focus()

    Label(main,text="Filename ",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420) 
    fileData=Entry(main,width=25,fg="black",border=2,font=('arial',15),bg='white')
    fileData.place(x=20,y=450)

    rimage=PhotoImage(file="images/arrow.png")
    re_btn = Button(main,text="Receive",image=rimage,bg="#39c790",fg="black",width=130,bd=0,compound=LEFT,font=('arial 14 bold'),command=Receiver)
    re_btn.place(x=20, y=500)    

    icon_image=PhotoImage(file="images/receive.png")
    main.iconphoto(False,icon_image)

    main.mainloop()

root = Tk()
root.title("gocommon")
root.geometry("450x560+500+200")
root.resizable(False, False)
root.configure(bg="#f4fdfe")

# Icon
icon_photo = PhotoImage(file="images/icon.png")
root.iconphoto(True, icon_photo)

# Label
Label(root, text="File transfer", font=("Arial", 15, 'bold'), bg="#f4fdfe").place(x=20, y=30)

# Frame
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

# Buttons
send_image=PhotoImage(file="images/Send.png")
send_btn = Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send_btn.place(x=50, y=100)

receive_image=PhotoImage(file="images/receive.png")
receive_btn = Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive_btn.place(x=300, y=100)

#label
Label(root,text="Send",font=("Arial", 15, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root,text="Recieve",font=("Arial", 15, 'bold'), bg="#f4fdfe").place(x=300, y=200)

background_image=PhotoImage(file="images/background.png")
Label(root,image=background_image).place(x=-2,y=323)
root.mainloop()
