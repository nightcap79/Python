import tkinter as tk
import webbrowser



window = tk.Tk()


greeting = tk.Label(text="CHESS GAME لعبة شطرنج",activeforeground="red", cursor="pencil")
#greeting.pack()

greeting.bind("<Button-1>", lambda e: webbrowser.open_new("http://www.google.com"))

c=0
vvvv = 0
for x  in range (0,64):
    
    r = int(x/8)

    if (vvvv%2) == 0: 
        color="black" 
    else:
        color="white"
    labZ = tk.Label( bg=color, width=5, height=2).grid(row=r,column=c)

    c += 1   #    c = c  + 1 
    if c == 8 :  # يتحقق هذا الشرط فقط عند كل سطر جديد
        c =0
        vvvv +=1

    vvvv += 1





window.mainloop()
