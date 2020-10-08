import tkinter, tkinter.messagebox

window = tkinter.Tk()
# window.eval('tk::PlaceWindow . center')
window.withdraw()
window2 = tkinter.Tk()
# window2.eval('tk::PlaceWindow . center')

window.geometry("610x480+600+300")
window2.geometry("130x100+600+300")
window.title("Tic Tac Toe .....")


v = tkinter.IntVar()


def closewindow2():
    window.wm_deiconify()
    window2.destroy()



radio2 = tkinter.Radiobutton(window2,text="Two Players",padx = 20, variable=v ,value = 2,anchor="e" ,state= "disabled"  ).grid(column=0,row=1)
radio1 = tkinter.Radiobutton(window2,text="Single Player",padx = 20, variable=v,value = 1,anchor="e"   ).grid(column=0,row=0)

buttonok = tkinter.Button(window2,command = closewindow2 , text = "OK" ).grid(column=0,row=2)


# window2.mainloop()


square = ["nw","no","ne","we","ce","ea","sw","so","se"]

for i in range(len(square)):
    globals()[square[i]] = tkinter.StringVar()

x,y = 0,1
for i in range(9):
    if x == 3: 
        x = 0
        y += 1
    tkinter.Label(  window,font=("Courier", 20),padx = 20,  height = 5, width =10,relief="groove", textvariable=globals()[square[i]]  ).grid(column=x,row=y)
    x += 1




def repeat(winer):
    # buttonrepeat.grid_forget()
    tkinter.messagebox.showinfo("Congratulations", winer.get()+ " Won!!")
    if tkinter.messagebox.askyesno("Play Again","Do you want to play again"):
    
        for i in range(len(square)):
            globals()[square[i]].set("")
    else:
        window.destroy()


playernum = 1

def change_label(num):
    global playernum


    if str(num.get()) == "":
        if playernum == 1 : 
            num.set("X")
            playernum = 2
        else: 
            num.set("O")
            playernum = 1
    
    if nw.get() == no.get() == ne.get() != "" : repeat(nw)#tkinter.messagebox.showinfo("Congratulations", nw.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+nw.get()).grid(column=1,row=0)
    if nw.get() == we.get() == sw.get() != "" : repeat(nw)#tkinter.messagebox.showinfo("Congratulations", nw.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+nw.get()).grid(column=1,row=0)
    if nw.get() == ce.get() == se.get() != "" : repeat(nw)#tkinter.messagebox.showinfo("Congratulations", nw.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+nw.get()).grid(column=1,row=0)
    if we.get() == ce.get() == ea.get() != "" : repeat(ce)#tkinter.messagebox.showinfo("Congratulations", ce.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+ce.get()).grid(column=1,row=0)
    if ne.get() == ce.get() == sw.get() != "" : repeat(ce)#tkinter.messagebox.showinfo("Congratulations", ce.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+ce.get()).grid(column=1,row=0)
    if no.get() == ce.get() == so.get() != "" : repeat(ce)#tkinter.messagebox.showinfo("Congratulations", ce.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+ce.get()).grid(column=1,row=0)
    if sw.get() == so.get() == se.get() != "" : repeat(se)#tkinter.messagebox.showinfo("Congratulations", se.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+se.get()).grid(column=1,row=0)
    if ne.get() == ea.get() == se.get() != "" : repeat(se)#tkinter.messagebox.showinfo("Congratulations", se.get()+ " Won!!")   #labelw =  tkinter.Label(window,fg = "Red", font=("Courier", 20), height = 5, width = 20, text="The Winer is "+se.get()).grid(column=1,row=0)



# buttonrepeat = tkinter.Button(window, command= repeat, text = "Play Again").grid(column=2,row=4)

def callback(event):
    print (str(event.widget))
    if (str(event.widget) == ".!label"): change_label(nw)
    if (str(event.widget )== ".!label2"): change_label(no)
    if (str(event.widget )== ".!label3"): change_label(ne)
    if (str(event.widget )== ".!label4"): change_label(we)
    if (str(event.widget )== ".!label5"): change_label(ce)
    if (str(event.widget )== ".!label6"): change_label(ea)
    if (str(event.widget )== ".!label7"): change_label(sw)
    if (str(event.widget )== ".!label8"): change_label(so)
    if (str(event.widget )== ".!label9"): change_label(se)

def closeapp():
    window.destroy()
    window2.destroy()

### Bind Actions
window.bind("<Button-1>", callback)
window.protocol("WM_DELETE_WINDOW", window.destroy )
window2.protocol("WM_DELETE_WINDOW", closeapp )


window.mainloop()
