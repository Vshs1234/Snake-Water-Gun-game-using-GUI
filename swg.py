import turtle
from tkinter import *
import random
ar=Tk()
ar.wm_iconbitmap("favicon.ico")
ar.configure(bg="#CACAFF")
#second page of our GUI
c=0
tc=0
tu=0

def fun1():
    ar.destroy()
    ar1=Tk()
    ar1.title("GAME-Playing...")
    ar1.geometry("600x600")
    ar1.wm_iconbitmap("favicon.ico")
    f2 = Frame(ar1, bg='#9090EE', borderwidth=3, relief=GROOVE, padx=10, pady=20)
    f2.pack(anchor="center", padx=10, pady=20,fill=BOTH)
    l3=Label(f2,text="Hello GAMER!!",bg='black',fg='white',padx=10,pady=20)
    l3.pack(padx=100,pady=20)
    l4 = Label(f2, text="Select any of these options\n s-Snake w-Water g-Gun", bg='black', fg='white', padx=10, pady=20)
    l4.pack(padx=100,pady=20)
    ch1=Label(f2,text="Turn-1")
    ch1.pack(pady=2)
    ch1 = StringVar()
    ch1value = Entry(f2, textvariable=ch1)
    ch1value.pack(pady=10)
    ch2 = Label(f2,text="Turn-2")
    ch2.pack(pady=2)
    ch2=StringVar()
    ch2value = Entry(f2, textvariable=ch2)
    ch2value.pack(pady=10)
    ch3 = Label(f2,text="Turn-3")
    ch3.pack(pady=2)
    ch3=StringVar()
    ch3value = Entry(f2, textvariable=ch3)
    ch3value.pack(pady=10)
    def exits():
        ar1.destroy()
        ar2=Tk()

        def ok():
            ar2.destroy()
            ar3=Tk()
            ar3.wm_iconbitmap("favicon.ico")

            def sr():
                f = open("response.txt", "a")
                f.write(f"Rating given: {rating.get()}\n")
                f.write(f"Feedback given is:{text.get(1.0,END)}\n")
                f.close()
                ar3.destroy()

            ar3.geometry("800x800")
            ar3.configure(bg="#9090EE")
            ar3.title("Rating-SWG")
            Label(ar3, text="Could you Please rate our effort here!!", font="lucida 15 italic").place(x=250, y=50)
            Label(ar3, text="5-Excellent\n4-Pretty well\n3-Average\n2-Good\n1-Worst", font="lucida 15 italic").place(x=350, y=100)
            rating=IntVar()
            rating.set(5)
            x=Entry(ar3,textvariable=rating,font="15").place(x=300,y=250)
            # feedback=StringVar()
            # y=Entry(ar3,textvariable=feedback,font="lucida 15 italic")
            # y.place(x=200,y=300)
            Label(ar3,text="You can give us your feedback here!!", font="lucida 15 italic").place(x=250,y=300)
            text=Text(ar3,font="bold",height=200,width=300)
            text.pack(padx=50,pady=350)
            Button(ar3,text="Submit",command=sr,font="lucida 13 bold",fg="#4A4A70").place(x=375,y=500)
            ar3.mainloop()
        ar2.geometry("500x500")
        ar2.wm_iconbitmap("favicon.ico")
        ar2.title("Overall Score-SWG")
        ar2.configure(bg="#9090EE")
        Label(ar2, text="Thanks for Playing!!", font="lucida 15 italic").place(x=150, y=50)
        Label(ar2,text=f"Hlo Player!!\nLet's see your overall score till {c} rounds",font="lucida 15 italic").place(x=80,y=100)
        Label(ar2,text=f"Your score is {tu} and computer score is {tc}",font="lucida 15 italic").place(x=80,y=225)
        Button(ar2,text="OK",command=ok).place(x=250,y=300)
        ar2.mainloop()


    def getvals():
        global c
        c=c+1
        ar1.title(f"Game-{c}")
        uc1=ch1.get()
        uc2=ch1.get()
        uc3=ch1.get()
        choices = ['s', 'w', 'g']
        cc1 = random.choice(choices)
        cc2 = random.choice(choices)
        cc3 = random.choice(choices)
        win(uc1,cc1,uc2,cc2,uc3,cc3)


    def win(userc1,compc1,userc2,compc2,userc3,compc3):
        global tu
        global tc
        up=0
        cp=0
        l=['s','w','g']
        if (userc1 not in l) or (userc2 not in l) or(userc3 not in l) :
            d=Tk()
            d.wm_iconbitmap("favicon.ico")
            d.geometry("400x400")
            d.title("WARNING!!!")
            k=Label(d,text="Please enter \na valid choice...\nU can enter \neither 's' or 'w' or 'g'",bg="black",fg="red",padx=50,pady=50,font="lucida 25 bold")
            k.pack()
            d.mainloop()
        else:
            if compc1 == 's':
                if userc1 == 'w':
                    cp = cp + 1
                elif userc1 == 'g':
                    up = up + 1
            elif compc1 == 'w':
                if userc1 == 'g':
                    cp = cp + 1
                elif userc1 == 's':
                    up = up + 1
            elif compc1 == 'g':
                if userc1 == 's':
                    cp = cp + 1
                elif userc1 == 'w':
                    up = up + 1
            elif compc1 == userc1:
                pass
            if compc2 == 's':
                if userc2 == 'w':
                    cp = cp + 1
                elif userc2 == 'g':
                    up = up + 1
            elif compc2 == 'w':
                if userc2 == 'g':
                    cp = cp + 1
                elif userc2 == 's':
                    up = up + 1
            elif compc2 == 'g':
                if userc2 == 's':
                    cp = cp + 1
                elif userc2 == 'w':
                    up = up + 1
            elif compc2 == userc2:
                pass
            if compc3 == 's':
                if userc3 == 'w':
                    cp = cp + 1
                elif userc3 == 'g':
                    up = up + 1
            elif compc3 == 'w':
                if userc3 == 'g':
                    cp = cp + 1
                elif userc3 == 's':
                    up = up + 1
            elif compc3 == 'g':
                if userc3 == 's':
                    cp = cp + 1
                elif userc3== 'w':
                    up = up + 1
            elif compc3 == userc3:
                pass
            if up>cp:
                ar2=Tk()
                ar2.geometry("300x300")
                ar2.wm_iconbitmap("favicon.ico")
                f3 = Frame(ar2, bg='#9090EE', borderwidth=3, relief=GROOVE, padx=10, pady=20)
                f3.pack(anchor="center", padx=10, pady=75,fill=BOTH)
                l5=Label(f3,text="Hurray!!You won")
                l5.pack(pady=10)
                tu+=1
                x = Label(f3, text=f"Your score is {up} and Dinku score is {cp}")
                x.pack(pady=10)
                ar2.mainloop()
            elif up==cp:
                ar2 = Tk()
                ar2.geometry("300x300")
                ar2.wm_iconbitmap("favicon.ico")
                f3 = Frame(ar2, bg='#9090EE', borderwidth=3, relief=GROOVE, padx=10, pady=20)
                f3.pack(anchor="center", padx=10, pady=75,fill=BOTH)
                l5 = Label(f3, text="Its a tie")
                l5.pack(pady=10)
                x = Label(f3, text=f"Your score is {up} and Dinku score is {cp}")
                x.pack()
                ar2.mainloop()
            else:
                ar2 = Tk()
                ar2.geometry("300x300")
                ar2.wm_iconbitmap("favicon.ico")
                f3 = Frame(ar2, bg='#9090EE', borderwidth=3, relief=GROOVE, padx=10, pady=20)
                f3.pack(anchor="center", padx=10, pady=75,fill=BOTH)
                l5 = Label(f3, text="Comp won")
                tc+=1
                l5.pack(pady=10)
                x = Label(f3, text=f"Your score is {up} and Dinku score is {cp}")
                x.pack(pady=10)
                ar2.mainloop()
    b3=Button(f2,text="PLAY",font="lucida 15 bold",command=getvals,borderwidth=3,fg="#4A4A70")
    b3.pack()
    b4 = Button(f2, text="EXIT", font="lucida 15 bold", command=exits, borderwidth=3, fg="#4A4A70")
    b4.pack(pady=10)
    ar1.mainloop()
def fun2():
    ar.destroy()


#first page of our GUI
ar.geometry("600x400")
ar.title("SWG-MIE")

f1=Frame(ar,bg='#9090EE',borderwidth=3,relief=GROOVE,padx=10,pady=20)
f1.pack(padx=10,pady=10,fill=BOTH)
l1=Label(f1,text="GAMING SWG-Snake Water Gun!!",bg="black",padx=10,pady=20,fg='white')
l1.pack(side=TOP,anchor='center',padx=100,pady=20)
l2=Label(f1,text="Are You READY GAMER!!",bg='black',fg='white')
l2.pack(padx=100,pady=20)
b1=Button(f1,text="YES",command=fun1,borderwidth=3)
b1.pack(pady=10)
b2=Button(f1,text="NO",command=fun2,borderwidth=3)
b2.pack(pady=10)
ar.mainloop()
