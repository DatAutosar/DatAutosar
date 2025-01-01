import os
import csv
import time
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import filedialog
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from tkinter import messagebox
from tkinter import *

ser = serial.Serial('COM10', 115200) 

data_list1 = []
data_list2 = []
data_list3 = []
data_list4 = []
data_list5 = []
data_list6 = []
data_list7 = []
data_list8 = []
def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to exit the program?"):
        win.destroy()
def show_car_brands():
    car_brands = [
        "Toyota",
        "Honda",
        "Ford",
        "Mazda CX-5",
         "Hyundai",
        "Mercedes",
        "BMW",
        "Volvo",
        "Peugeot",
    ]
    def select_car_brand(event):
        selected_index = listbox.curselection()
        if selected_index:
            selected_car_brand = listbox.get(selected_index)
            label.config(text=f"Select: {selected_car_brand}")
    window = Toplevel(win)
    window.title("Car brand list")
    scroll =Scrollbar(window)
    scroll.pack(side=RIGHT, fill=Y)
    listbox = Listbox(window, yscrollcommand=scroll.set) 
    for car_brand in car_brands:
        listbox.insert(END, car_brand)
    listbox.pack(side=LEFT, fill=BOTH)
    scroll.config(command=listbox.yview) 
    listbox.bind("<<ListboxSelect>>", select_car_brand)

def update_data():
    if ser.in_waiting > 0:
        data1 = ser.readline().decode().strip()
        value = int(data1)
        if 600 <= value <= 6000 :
          label1.config(text="Engine speed [rpm]: " + str(value))
          data_list1.append(value)
    if ser.in_waiting > 0:
        data2 = ser.readline().decode().strip()
        value = int(data2)
        if 0 <= value <= 18 :
          label2.config(text="Vehicle speed [km/h]: " + str(value))
          data_list2.append(value)
    if ser.in_waiting > 0: 
        data3 = ser.readline().decode().strip()  
        value = int(data3)
        if (-500 <= value <= 0) or (10 <= value <= 500) :
            label3.config(text="Steer angle [deg]: " + str(value))
            data_list3.append(value)
    if ser.in_waiting > 0: 
        data4 = ser.readline().decode().strip()  
        value = int(data4)
        if 0 <= value <= 70 :
            label4.config(text='Pedal gas [%]:' + str(value))
        data_list4.append(value)
    if ser.in_waiting > 0: 
        data5 = ser.readline().decode().strip()  
        value = int(data5)
        if 0 <= value <= 18 :
            label5.config(text=" Front left wheel speed[km/h]:" + str(value))
        data_list5.append(value)
    if ser.in_waiting > 0: 
        data6 = ser.readline().decode().strip()  
        value = int(data6)
        if 0 <= value <= 18 :
            label6.config(text=" Front right wheel speed[km/h]:" + str(value))
        data_list6.append(value)
    if ser.in_waiting > 0: 
        data7 = ser.readline().decode().strip()  
        value = int(data7)
        if 0 <= value <= 18 :
            label7.config(text=" Rear left wheel speed[km/h]:" + str(value))
        data_list7.append(value)     
    if ser.in_waiting > 0: 
        data8 = ser.readline().decode().strip()  
        value = int(data8)
        if 0 <= value <= 18 :
            label8.config(text=" Rear right wheel speed[km/h]:" + str(value))
        data_list8.append(value)
    if button_stop["state"] == "normal":
       button_start.after(100,update_data) 

def start_reading():
    button_start.config(state="disabled")
    button_stop.config(state="normal")
    update_data()
def stop_reading():
    button_start.config(state="normal")
    button_stop.config(state="disabled")

def save_data1():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]', 'Engine speed [rpm]'])  
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list1:  
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1) 
                current_time = round(time.time() - start_time)

def save_data2():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Vehicle speed [km/h]'])  
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list2:  
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1) 
                current_time = round(time.time() - start_time)

def save_data3():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Steer angle [deg]'])  
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list3:  
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1)  
                current_time = round(time.time() - start_time)

def save_data4():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Pedal gas [%]']) 
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list4: 
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1) 
                current_time = round(time.time() - start_time)     

def save_data5():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Front left wheel speed [km/h]']) 
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list5: 
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1) 
                current_time = round(time.time() - start_time)

def save_data6():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Front right wheel speed [km/h]'])  
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list6:  
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1) 
                current_time = round(time.time() - start_time)

def save_data7():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Rear left wheel speed [km/h]'])  
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list7:  
                writer.writerow([current_time, value])  
                data_file.flush() 
                time.sleep(1)  
                current_time = round(time.time() - start_time)

def save_data8():
    documents_folder = os.path.expanduser("~/Documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
    file_path = filedialog.asksaveasfilename(initialdir=documents_folder, defaultextension='.csv')
    if file_path:
        with open(file_path, 'w', newline='') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(['Time [sec]','Rear right wheel speed [km/h]']) 
            start_time = time.time()
            current_time = round(time.time() - start_time)
            for value in data_list8:  
                writer.writerow([current_time, value])  
                data_file.flush()  
                time.sleep(1)  
                current_time = round(time.time() - start_time)

def update_plot1(i):
    time = list(range(len(data_list1)))
    ax1.clear()
    ax1.plot(time, data_list1)
    ax1.set_xlabel('Time [sec]')
    ax1.set_ylabel('Engine speed [rpm]')
    ax1.set_xticks(time[::10])  
    ax1.legend()
def show_plot1():
    global plot_window1, fig1, ax1, ani1
    if not plot_window1:
        plot_window1 = Toplevel(win)
        plot_window1.title("Engine speed [rpm]")
        fig1 = Figure(figsize=(5,4 ), dpi = 100)
        ax1 = fig1.add_subplot(1, 1, 1)
        canvas1 = FigureCanvasTkAgg(fig1, master=plot_window1)
        canvas1_widget = canvas1.get_tk_widget()
        canvas1_widget.pack()
        ani1 = FuncAnimation(fig1, update_plot1,cache_frame_data=False, interval=2000)
    
def update_plot2(i):
    time = list(range(len(data_list2)))
    ax2.clear()
    ax2.plot(time, data_list2)
    ax2.set_xlabel('Time [sec]')
    ax2.set_ylabel('Vehicle speed [km/h]')
    ax2.set_xticks(time[::10])  
    ax2.legend()
def show_plot2():
    global plot_window2, fig2, ax2, ani2
    if not plot_window2:
        plot_window2 = Toplevel(win)
        plot_window2.title("Vehicle speed [km/h]")
        fig2 = Figure(figsize=(5, 4), dpi=100)
        ax2 = fig2.add_subplot(1, 1, 1)
        canvas2 = FigureCanvasTkAgg(fig2, master=plot_window2)
        canvas2_widget = canvas2.get_tk_widget()
        canvas2_widget.pack()
        ani2 = FuncAnimation(fig2, update_plot2, interval=2000)

def update_plot3(i):
    time = list(range(len(data_list3)))
    ax3.clear()
    ax3.plot(time, data_list3) 
    ax3.axhline(0, color='black', linewidth=0.5)  
    ax3.set_xlabel('Time [sec]')
    ax3.set_ylabel('Steer angle [deg]')
    ax3.set_xticks(time[::10])  
    ax3.legend()
def show_plot3():
    global plot_window3, fig3, ax3, ani3
    if not plot_window3:
        plot_window3 = Toplevel(win)
        plot_window3.title("Steer angle [deg]")
        fig3 = Figure(figsize=(5, 4), dpi=100)
        ax3 = fig3.add_subplot(1, 1, 1)
        canvas3 = FigureCanvasTkAgg(fig3, master=plot_window3)
        canvas3_widget = canvas3.get_tk_widget()
        canvas3_widget.pack()
        ani3 = FuncAnimation(fig3, update_plot3, interval=2000)

def update_plot4(i):
    time = list(range(len(data_list4)))
    ax4.clear()
    ax4.plot(time, data_list4) 
    ax4.set_xlabel('Time [sec]')
    ax4.set_ylabel('Pedal gas [%]')
    ax4.set_xticks(time[::10]) 
    ax4.legend()
def show_plot4():
    global plot_window4, fig4, ax4, ani4
    if not plot_window4:
        plot_window4 = Toplevel(win)
        plot_window4.title("Pedal gas [%]")
        fig4 = Figure(figsize=(5, 4), dpi=100)
        ax4 = fig4.add_subplot(1, 1, 1)
        canvas4 = FigureCanvasTkAgg(fig4, master=plot_window4)
        canvas4_widget = canvas4.get_tk_widget()
        canvas4_widget.pack()
        ani4 = FuncAnimation(fig4, update_plot4, interval=2000)

def update_plot5(i):
    time = list(range(len(data_list5)))
    ax5.clear()
    ax5.plot(time, data_list5)
    ax5.set_xlabel('Time [sec]')
    ax5.set_ylabel('Front left wheel speed [km/h]')
    ax5.set_xticks(time[::10])  
def show_plot5():
    global plot_window5, fig5, ax5, ani5
    if not plot_window5:
        plot_window5 = Toplevel(win)
        plot_window5.title("Front left wheel speed [km/h]")
        fig5 = Figure(figsize=(5, 4), dpi=100)
        ax5 = fig5.add_subplot(1, 1, 1)
        canvas5 = FigureCanvasTkAgg(fig5, master=plot_window5)
        canvas5_widget = canvas5.get_tk_widget()
        canvas5_widget.pack()
        ani5 = FuncAnimation(fig5, update_plot5, interval=2000)

def update_plot6(i):
    time = list(range(len(data_list6)))
    ax6.clear()
    ax6.plot(time, data_list6, label='Front right wheel speed [km/h]')
    ax6.set_xlabel('Time [sec]')
    ax6.set_ylabel('Front right wheel speed [km/h]')
    ax6.set_xticks(time[::10]) 
    ax6.legend()
def show_plot6():
    global plot_window6, fig6, ax6, ani6
    if not plot_window6:
        plot_window6 = Toplevel(win)
        plot_window6.title("Front right wheel speed [km/h]")
        fig6 = Figure(figsize=(5, 4), dpi=100)
        ax6 = fig6.add_subplot(1, 1, 1)
        canvas6= FigureCanvasTkAgg(fig6, master=plot_window6)
        canvas6_widget = canvas6.get_tk_widget()
        canvas6_widget.pack()
        ani6 = FuncAnimation(fig6, update_plot6, interval=2000)

def update_plot7(i):
    time = list(range(len(data_list7)))
    ax7.clear()
    ax7.plot(time, data_list7)
    ax7.set_xlabel('Time [sec]')
    ax7.set_ylabel('Rear left wheel speed [km/h]')
    ax7.set_xticks(time[::10])  
    ax7.legend()
def show_plot7():
    global plot_window7, fig7, ax7, ani7
    if not plot_window7:
        plot_window7 = Toplevel(win)
        plot_window7.title("Rear left wheel speed [km/h]")
        fig7 = Figure(figsize=(5, 4), dpi=100)
        ax7 = fig7.add_subplot(1, 1, 1)
        canvas7= FigureCanvasTkAgg(fig7, master=plot_window7)
        canvas7_widget = canvas7.get_tk_widget()
        canvas7_widget.pack()
        ani7 = FuncAnimation(fig7, update_plot7, interval=2000)

def update_plot8(i):
    time = list(range(len(data_list8)))
    ax8.clear()
    ax8.plot(time, data_list8)
    ax8.set_xlabel('Time [sec]')
    ax8.set_ylabel('Rear right wheel speed [km/h]')
    ax8.set_xticks(time[::10])  
    ax8.legend()
def show_plot8():
    global plot_window8, fig8, ax8, ani8
    if not plot_window8:
        plot_window8 = Toplevel(win)
        plot_window8.title("Rear right wheel speed [km/h]")
        fig8 = Figure(figsize=(5, 4), dpi=100)
        ax8 = fig8.add_subplot(1, 1, 1)
        canvas8= FigureCanvasTkAgg(fig8, master=plot_window8)
        canvas8_widget = canvas8.get_tk_widget()
        canvas8_widget.pack()
        ani8 = FuncAnimation(fig8, update_plot8, interval=2000)

win=Tk()
win.geometry('1600x770')
win.attributes('-fullscreen', True)
win.title('Engine index')
def exit_fullscreen(event):
     win.attributes('-fullscreen', False)
win.bind("<Escape>", exit_fullscreen)

photo_image = PhotoImage(file="C:\image\hcmute.png")
hcmute = Label(win, image=photo_image)
hcmute.place(x=15, y=15)
lbl = Label(win, text=" ENGINE INDEX ", font=('Arial 37 bold'), fg='blue')
lbl.place ( x= 630, y=18)
BangDK0 = Canvas(win, bg="lightgreen", height=280, width=260)
BangDK0.place(x=5, y=257)
Label9 = Label(win, text="CONTROL TABLE", font=('Arial 22 bold'),  fg = "blue",bg = 'white')
Label9.place(x=12, y=278)
BangDK1 = Canvas(win, bg="lightblue", height=595, width=530)
BangDK1.place(x=275, y=110)
BangDK2 = Canvas(win, bg="lightblue", height=595, width=530)
BangDK2.place(x=820, y=110)
BangDK3 = Canvas(win, bg="lightblue", height=155, width=260)
BangDK3.place(x=5, y=550)
label =Label(win, text="", font = "Arial 19 bold", bg ="lightblue")
label.place(x=15, y=645)

label1 = Label(win, text="Engine speed [rpm]:", font=('Arial 22 bold'),bg= "lightblue" ,fg='black')
label1.place(x=279, y= 118)
label2 = Label(win, text="Vehicle speed [km/h]:", font=('Arial 22 bold'),bg='lightblue', fg='black')
label2.place(x=278, y=270)
label3 = Label(win, text="Steer angle [deg]:", font=('Arial 21 bold '),bg='lightblue', fg='black')
label3.place(x=280, y=422)
label4 = Label(win, text="Pedal gas [%]:", font=('Arial 22 bold '),bg='lightblue', fg='black')
label4.place(x=278, y=569)
label5 = Label(win, text="Front left wheel speed [km/h]:", font=('Arial 22 bold'),bg='lightblue', fg='black')
label5.place(x=825, y=118)
label6 = Label(win, text="Front right wheel speed [km/h]:", font=('Arial 22 bold '),bg='lightblue', fg='black')
label6.place(x=825, y=270)
label7 = Label(win, text="Rear left wheel speed [km/h]:", font=('Arial 22 bold '),bg='lightblue', fg='black')
label7.place(x=825, y=422)
label8 = Label(win, text="Rear right wheel speed [km/h]:", font=('Arial 22 bold '),bg='lightblue', fg='black')
label8.place(x=825, y= 569)

lineTieuDe = Canvas(win, bg="lightblue", height=5, width = 1070)
lineTieuDe.place(x=276, y=80)
lineTieuDe2 = Canvas(win, bg="black", height=1, width = 260)
lineTieuDe2.place(x=5, y=330)
lineTieuDe3 = Canvas(win, bg="black", height=1, width = 260)
lineTieuDe3.place(x=5, y=257)
lineTieuDe4 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe4.place(x=275, y=110)
lineTieuDe5 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe5.place(x=275, y=260)
lineTieuDe6 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe6.place(x=275, y=412)
lineTieuDe7 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe7.place(x=275, y=562)
lineTieuDe8 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe8.place(x=275, y=704)
lineTieuDe9 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe9.place(x=820, y=110)
lineTieuDe10 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe10.place(x=820, y=260)
lineTieuDe11 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe11.place(x=820, y=412)
lineTieuDe12 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe12.place(x=820, y= 562)
lineTieuDe13 = Canvas(win, bg="black", height=1, width = 530)
lineTieuDe13.place(x=820, y= 704)
lineTieuDe14 = Canvas(win, bg="black", height=1, width = 260)
lineTieuDe14.place(x=5, y= 535)
lineTieuDe14 = Canvas(win, bg="black", height=1, width = 260)
lineTieuDe14.place(x=5, y= 551)
lineTieuDe15 = Canvas(win, bg="black", height=1, width = 260)
lineTieuDe15.place(x=5, y= 704)

button_car_brand =Button(win, text="CAR BRAND", font=('Arial 22 bold'),  fg = "blue",bg = 'white', command=show_car_brands)
button_car_brand.place(x=37, y=570)
button_exit = Button(win, text="EXIT", font = "Arial 21 bold" , fg = "brown" , bg = "white" ,command=exit_program)
button_exit.place(x= 90,y=470)
button_start = Button(win, text="START", font=('Arial 20 bold '), bg='white', fg='brown', command=start_reading)
button_start.place(x=75, y=346)
button_stop = Button(win, text="STOP", font=('Arial 20 bold '),bg='white', fg='brown', command=stop_reading)
button_stop.place(x=85, y=408)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data1)
button_save.place(x=280, y=190)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data2)
button_save.place(x=280, y=342)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data3)
button_save.place(x=280, y=492)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data4)
button_save.place(x=280, y=630)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data5)
button_save.place(x=830, y=190)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data6)
button_save.place(x=828, y=342)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data7)
button_save.place(x=828, y=492)
button_save = Button(win, text="Save", font=('arial 22 bold'), fg='brown', bg='white', command=save_data8)
button_save.place(x=828, y=630)

button_plot = Button(win, text="Plot",font =('arial 22 bold'), fg='brown', bg='white' ,command=show_plot1)
plot_window1 = None
button_plot.place (x=380, y=190)
button_plot = Button(win, text="Plot",font =('arial 22 bold'),fg='brown', bg='white' ,command=show_plot2)
button_plot.place (x=380, y=342)
plot_window2 = None
button_plot = Button(win, text="Plot",font =('arial 22 bold'), fg='brown', bg='white' ,command=show_plot3)
button_plot.place (x=380, y=492)
plot_window3 = None
button_plot = Button(win, text="Plot",font =('arial 22 bold'),fg='brown', bg='white' ,command=show_plot4)
button_plot.place (x=380, y=630)
plot_window4 = None
button_plot = Button(win, text="Plot",font =('arial 22 bold'),fg='brown', bg='white' ,command=show_plot5)
plot_window5 = None
button_plot.place (x=930, y=190)
button_plot = Button(win, text="Plot",font =('arial 22 bold'), fg='brown', bg='white' ,command=show_plot6)
button_plot.place (x=930, y=342)
plot_window6 = None
button_plot = Button(win, text="Plot",font =('arial 22 bold'), fg='brown', bg='white' ,command=show_plot7)
button_plot.place (x=930, y=492)
plot_window7 = None
button_plot = Button(win, text="Plot",font =('arial 22 bold'), fg='brown', bg='white' ,command=show_plot8)
plot_window8 = None
button_plot.place (x=930, y=630)
win.mainloop()