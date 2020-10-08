import tkinter

#a,b=0,0


w = tkinter.Tk()

$(cmd)

x,y = 0,0



v=  tkinter.StringVar()

v.set(0)

def change_label(x):
    global v
    if v.get() == "0" :
        v.set(str(x))
        return 
    v.set(v.get()+str(x))

def add():
    global v,a
    a = int(v.get())
    v.set("0")

def equ():
    global v,a
    cccc = a + int(  v.get() )
    v.set( str(       int(a) + int(  v.get()    )   )  )



def callback(event):
    print (str(event.widget))
    if (str(event.widget) == ".!button"): change_label(0)
    if (str(event.widget )== ".!button2"): change_label(1)
    if (str(event.widget )== ".!button3"): change_label(2)
    if (str(event.widget )== ".!button4"): change_label(3)
    if (str(event.widget )== ".!button5"): change_label(4)
    if (str(event.widget )== ".!button6"): change_label(5)
    if (str(event.widget )== ".!button7"): change_label(6)
    if (str(event.widget )== ".!button8"): change_label(7)
    if (str(event.widget )== ".!button9"): change_label(8)
    if (str(event.widget )== ".!button10"): change_label(9)

label = tkinter.Label(w, textvariable = v).grid(row=4,column=1)

for i in range(10):
    button = tkinter.Button ( w, text=i , width =  10).grid(row=y,column=x)

    x += 1
    if i % 3 == 0 :
        y += 1
        x = 0
    

button = tkinter.Button ( w,text="+" , width =  10, command=add).grid(row=0,column=2)
button = tkinter.Button ( w,text="=" , width =  10, command=equ).grid(row=0,column=1)


w.bind("<Button-1>", callback)


w.mainloop()