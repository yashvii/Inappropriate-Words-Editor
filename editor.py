from os import linesep
from tkinter import *
from tkinter import font

window = Tk()
window['background']='#AEC6CF'

lbl=Label(window, text="Enter your text:", fg='red', bg='#AEC6CF', font=("Times New Roman", 16))
lbl.place(x=30, y=20)
def removal():
     global inp
     inp = T.get(1.0, "end-1c")
     path='C:\\Users\\User\\Desktop\\code\\.vscode\\wor\\words.txt'
     f = open(path,"r",encoding="utf8")
     con=f.read()
     conl=con.split("\n")
     f.close()
     for word in inp.casefold().split():
         if word in conl:
            Tt.insert('1.0'," ")
            dispfont =font.Font(family='Times New Roman', size=10,weight=font.BOLD)
            disp1 = Label(window,text='The entered text has inapproriate word(s) hence they have been removed      ',bg='#AEC6CF',font=dispfont,relief=RAISED)
            disp1.place(x=50,y=450)

          
    # Do Something else if word is not present
         else:
            Tt.insert(END,word+" ")
            dispfont =font.Font(family='Times New Roman', size=10,weight=font.BOLD)
            disp = Label(window,text='The entered text has no inapproriate word(s) hence nothing has been edited',bg='#AEC6CF',font=dispfont,relief=RAISED)
            disp.place(x=50,y=450)
        
            
def clear():
    Tt.delete('1.0',END)

    
#textbox creation
T = Text(window, width = 62,height =7.5)
T.place(x=50,y=75)
#button creation
btnfont =font.Font(family='Times New Roman', size=14)
btn = Button(window, text = "Edit", bd = '5',font= btnfont,command=removal)
btn.configure(activebackground = "#8FBC8F",relief=RAISED)

btn.place(x=150,y=240)
btnfont =font.Font(family='Times New Roman', size=14)
btn1 = Button(window, text = "Clear", bd = '5',font= btnfont,command=clear)
btn1.configure(activebackground = "#8FBC8F",relief=RAISED)
btn1.place(x=350,y=240)

#textbox creation
Tt = Text(window, width = 62,height =7.5)
Tt.place(x=50,y=300)
window.title('Inappropriate Word Editor')
window.geometry("600x500")
window.eval('tk::PlaceWindow . center')
window.mainloop()