from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from plyer import notification
import time


t = Tk()
t.title("notifier-app")
t.geometry("500x300")
img = Image.open("image1.jpg")
img = img.resize((500, 350))

tkimage =ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are compulsory!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set ", "set notification?")

        time.sleep(min_to_sec)

        notification.notify(title=get_title, message=get_msg, app_name="Notifier", app_icon="ico.ico", timeout=10)




img_labels = Label(t, image=tkimage).grid()

# label1
t_label = Label(t, text = "Title to Notify", font=("poppins",10))
t_label.place(x=12, y=70)

# entry1
title = Entry(t, width="25", font=("poppins", 13))
title.place(x=123, y=70)

# label2
m_label = Label(t, text = "Message", font=("poppins",10))
m_label.place(x=12, y=120)

# entry2
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123, y=120, height=30)

# label3
time_label = Label(t, text = "Set Time", font=("poppins",10))
time_label.place(x=12, y=175)

# entry3
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# label4
time_min_label = Label(t, text = "Min", font=("poppins",10))
time_min_label.place(x=185, y=180)

# button
but = Button(t, text = "SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#7d7e80", width=20, relief="raised", command=get_details)
but.place(x=170,y=230)


t.resizable(0,0)
t.mainloop()
