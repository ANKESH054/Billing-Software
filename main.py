import os
import random
from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu
from tkinter import messagebox
# from PIL import ImageTk,Image

#welcome window
root = Tk()
#main window and functions
def main():
    root = Tk()

    #generate bill no
    def bill_no():
        try:
           z=open("bill_no","x")
           z.close()
           z = open("bill_no", "w")
           z.write("1")
           z.close()
        except:
            z=open("bill_no","r")
            e=int(z.readline())
            e3.delete(0,END)
            z.close()
            e3.insert(0,"{}".format(e))
            e+=1
            z=open("bill_no","w")
            z.write("{}".format(e))
            z.close()
    #clear billing area
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        e12.delete(0,END)
        e13.delete(0,END)
        e14.delete(0,END)
        e15.delete(0,END)
        e16.delete(0,END)
        e17.delete(0,END)
        e18.delete(0,END)
        e19.delete(0,END)
        e20.delete(0,END)
        e21.delete(0,END)
        e22.delete(0,END)
        e23.delete(0,END)
        e24.delete(0,END)
        e25.delete(0,END)
        e26.delete(0,END)
        e27.delete(0,END)
        t1.delete(1.0,END)
        bill_no()
    #Generate bill in billing area and store it in a diffrent file with a unique bill no.
    def gen_bill():
        t1.insert(END, "                   BS\n     "
                       "            Billing Software\n")
        b = os.getcwd()
        os.chdir("{}/bill".format(b))
        z = open("{}".format(e3.get()),"r")
        for i in range(20):
            k = z.readline()
            t1.insert(END, "{}".format(k))
        t1.insert(END, "\n \n Total :      {0}".format(float(e4.get()[3:])+float(e6.get()[3:])+float(e8.get()[3:])))
        z.close()
        z = open("{}".format(e3.get()), "a")
        z.write("Total :      {0}".format(float(e4.get()[3:])+float(e6.get()[3:])+float(e8.get()[3:])))
        z.close()
        os.chdir("{}".format(b))
    #search bill using a unique bill no. and display on bill area.
    def sea():
        t1.delete(1.0, END)
        try:
            b=os.getcwd()
            os.chdir("{}/bill".format(b))
            z=open("{}".format(e3.get()),"r")
            for i in range(20):
                k=z.readline()
                t1.insert(END,"{}".format(k))
            os.chdir("{}".format(b))
        except:
            messagebox.showinfo("error","Specified Bill no Not available.")
    #generate total of bill
    def total():
            global d, e
            e = d = f = w = 0
            e1.get()
            e2.get()
            e3.get()
            co1 = [e10.get(), e11.get(), e12.get(), e13.get(), e14.get(), e15.get()]
            g1 = [e16.get(), e17.get(), e18.get(), e19.get(), e20.get(), e21.get()]
            col1 = [e22.get(), e23.get(), e24.get(), e25.get(), e26.get(), e27.get()]
            col2 = [e22, e23, e24, e25, e26, e27]
            g2 = [e16, e17, e18, e19, e20, e21]
            co2 = [e10, e11, e12, e13, e14, e15]
            g = ["rc", "fo", "da", "wh", "su", "te"]
            c = ["ba", "fc", "fw", "hs", "hg", "bl"]
            co = ["mz", "coc", "fru", "thum", "lim", "spr"]
            r = ["grot", "cost", "colt"]
            l = 0
            for i in g:
                z = open(i, "r")
                e = int(z.readline())
                z.close()
                n = e * int(g1[l])
                l += 1
                d += n
            z = open(r[0], "r")
            u = float(z.readline())
            e7.insert(1, "{}".format(u))
            z.close()
            p = d * (u / 100)
            s = p + d
            e6.insert(1, "Rs.{}".format(s))
            l = 0
            for i in g:
                z = open(i, "r")
                e = int(z.readline())
                z.close()
                n = e * int(co1[l])
                l += 1
                w += n
            z = open(r[1], "r")
            u = float(z.readline())
            e5.insert(1, "{}".format(u))
            z.close()
            s = w * (u / 100)
            q = s + w
            e4.insert(1, "Rs.{}".format(q))
            l = 0
            for i in co:
                z = open(i, "r")
                e = int(z.readline())
                z.close()
                n = e * int(col1[l])
                l += 1
                f += n
            z = open(r[2], "r")
            u = float(z.readline())
            e9.insert(1, "{}".format(u))
            z.close()
            o = f * (u / 100)
            e = o + f
            e8.insert(1, "Rs.{}".format(e))
            z = open("bill_no", "r")
            s = z.readline()
            z.close()
            try:
                b = os.getcwd()
                os.mkdir("{}/bill".format(b))
                os.chdir("{}/bill".format(b))
                z = open("{}".format(e3.get()), "w")
                n = [e10.get(), e11.get(), e12.get(), e13.get(), e14.get(), e15.get(),
                     e16.get(), e17.get(), e18.get(), e19.get(), e20.get(), e21.get(), e22.get(), e23.get(), e24.get(),
                     e25.get(), e26.get(), e27.get()]
                m = ["Bath soap", "Face cream", "Face Wash", "Hair Spray"
                    , "Hair Gel", "Body Lotion", "Rice", "Food Oil", "Daal", "Wheat", "Sugar", "Tea"
                    , "Maza", "Coke", "Fruti", "Thumbs up", "Sprite"]
                z.write("Name :{0} \nContact :{1}\nBill no.{2}\n\n".format(e1.get(), e2.get(), s))
                z.write("Items\t\tQuantity\n")
                l = 0
                for i in m:
                    z.write("{0}\t\t{1}\n".format(i, n[l]))
                    l += 1
                z.close()
                os.chdir("{}".format(b))
            except:
                os.chdir("{}/bill".format(b))
                z = open("{}".format(e3.get()), "w")
                n = [e10.get(), e11.get(), e12.get(), e13.get(), e14.get(), e15.get(),
                     e16.get(), e17.get(), e18.get(), e19.get(), e20.get(), e21.get(), e22.get(), e23.get(), e24.get(),
                     e25.get(), e26.get(), e27.get()]
                m = ["Bath soap", "Face cream", "Face Wash", "Hair Spray"
                    , "Hair Gel", "Body Lotion", "Rice", "Food Oil", "Daal", "Wheat", "Sugar", "Tea"
                    , "Maza", "Coke", "Fruti", "Thumbs up", "Sprite"]
                z.write("Name :{0} \nContact :{1}\nBill no.{2}\n\n".format(e1.get(), e2.get(), s))
                z.write("Items\t\tQuantity\n")
                l = 0
                for i in m:
                    z.write("{0}\t\t{1}\n".format(i, n[l]))
                    l += 1
                z.close()
                os.chdir("{}".format(b))
            l = 0
            for i in co:
                col2[l].delete(0, END)
                z = open(i, "r")
                e = z.readline()
                col2[l].insert(1, "Rs.{}".format(e))
                z.close()
                l += 1
            l = 0
            for i in g:
                g2[l].delete(0, END)
                z = open(i, "r")
                e = z.readline()
                g2[l].insert(1, "Rs.{}".format(e))
                z.close()
                l += 1
            l = 0
            for i in c:
                co2[l].delete(0, END)
                z = open(i, "r")
                e = z.readline()
                co2[l].insert(1, "Rs.{}".format(e))
                z.close()
                l += 1

    root.geometry("1280x720")
    root.minsize(960, 540)
    root.configure(bg="black")
    root.title("BILLING APPLICATION")
    # top frame
    topframe = LabelFrame(root, text="Customer Details", bg="grey", font=("comicsansms", 12, "bold"), fg="yellow",
                          height="60", relief=SUNKEN, borderwidth=5)

    l2 = Label(topframe, text="Customer Name", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=10, y=5)
    e1 = Entry(topframe, relief=SUNKEN, borderwidth=5)
    e1.place(x=125, y=-1)
    l3 = Label(topframe, text="Contact No.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=429, y=5)
    e2 = Entry(topframe, relief=SUNKEN, borderwidth=5)
    e2.place(x=515, y=-1)
    l4 = Label(topframe, text="Bill No.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(
        x=860, y=5)
    e3 = Entry(topframe, relief=SUNKEN, borderwidth=5)
    e3.place(x=923, y=-1)
    try:
        z = open("bill_no", "x")
        z.close()
        z = open("bill_no", "w")
        z.write("1")
        z.close()
    except:
        z = open("bill_no", "r")
        e = int(z.readline())
        z.close()
        e3.insert(0, "{}".format(e))
        e += 1
        z = open("bill_no", "w")
        z.write("{}".format(e))
        z.close()
    btn1 = Button(topframe, activebackground="black", activeforeground="white", text="Search",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3,command=sea).place(x=1115, y=-3)
    topframe.pack(side=TOP, fill=X, padx=10, pady=10)

    bottomframe = LabelFrame(root, text="Billing Menu", bg="grey", fg="yellow", font=("comicsansms", 12, "bold"),
                             height="150", relief=SUNKEN, borderwidth=5)

    l6 = Label(bottomframe, text="Total Cosmetic Price", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=10, y=15)
    e4 = Entry(bottomframe, relief=SUNKEN, borderwidth=5)
    e4.place(x=150, y=3)
    l7 = Label(bottomframe, text="Cosmetic Tax.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=418, y=15)
    e5 = Entry(bottomframe, relief=SUNKEN, borderwidth=5)
    e5.place(x=535, y=3)
    l8 = Label(bottomframe, text="Total Grocery", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=10, y=51)
    e6 = Entry(bottomframe, relief=SUNKEN, borderwidth=5)
    e6.place(x=150, y=40)
    l9 = Label(bottomframe, text="Grocery Tax.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=418, y=51)
    e7 = Entry(bottomframe, relief=SUNKEN, borderwidth=5)
    e7.place(x=535, y=40)
    l10 = Label(bottomframe, text="Total Cold Drinks", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=80)
    e8 = Entry(bottomframe, relief=SUNKEN, borderwidth=5)
    e8.place(x=150, y=80)
    l11 = Label(bottomframe, text="Cold Drinks Tax.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=418, y=80)
    e9 = Entry(bottomframe, relief=SUNKEN, borderwidth=5)
    e9.place(x=535, y=80)
    btn2 = Button(bottomframe, activebackground="black", activeforeground="white", text="Total",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, height=2, width=6, borderwidth=9,command=total).place(x=820,
                                                                                                           y=30)
    btn3 = Button(bottomframe, activebackground="black", activeforeground="white", text="Generate Bill",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, height=2, width=12, borderwidth=9,command=gen_bill).place(x=940,
                                                                                                            y=30)
    btn4 = Button(bottomframe, activebackground="black", activeforeground="white", text="Clear",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, height=2, width=6, borderwidth=9,command=clear).place(x=1110,
                                                                                                           y=30)
    btn5 = Button(bottomframe, activebackground="black", activeforeground="white", text="Exit",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, height=2, width=5, borderwidth=9,
                  command=root.destroy).place(x=1220,
                                              y=30)
    bottomframe.pack(side=BOTTOM, fill=X, padx=10, pady=10)

    cntrframe1 = LabelFrame(root, text="Cosmetic", bg="grey", fg="yellow", font=("comicsansms", 12, "bold"),
                            height="70", width="325", relief=SUNKEN, borderwidth=5)

    l13 = Label(cntrframe1, text="Bath Soap", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=15)
    e10 = Entry(cntrframe1, relief=SUNKEN, borderwidth=5)
    e10.place(x=125, y=11)
    l14 = Label(cntrframe1, text="Face Cream", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=80)
    e11 = Entry(cntrframe1, relief=SUNKEN, borderwidth=5)
    e11.place(x=125, y=80)
    l15 = Label(cntrframe1, text="Face Wash", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=145)
    e12 = Entry(cntrframe1, relief=SUNKEN, borderwidth=5)
    e12.place(x=125, y=145)
    l16 = Label(cntrframe1, text="Hair Spray", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=210)
    e13 = Entry(cntrframe1, relief=SUNKEN, borderwidth=5)
    e13.place(x=125, y=210)
    l17 = Label(cntrframe1, text="Hair Gel", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=275)
    e14 = Entry(cntrframe1, relief=SUNKEN, borderwidth=5)
    e14.place(x=125, y=275)
    l18 = Label(cntrframe1, text="Body Lotion", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=340)
    e15 = Entry(cntrframe1, relief=SUNKEN, borderwidth=5)
    e15.place(x=125, y=340)
    cntrframe1.pack(side=LEFT, fill=Y, padx=10, pady=10)

    cntrframe2 = LabelFrame(root, text="Grocery", bg="grey", fg="yellow", font=("comicsansms", 12, "bold"), height="70",
                            width="325", relief=SUNKEN, borderwidth=5)

    l20 = Label(cntrframe2, text="Rice", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=15)
    e16 = Entry(cntrframe2, relief=SUNKEN, borderwidth=5)
    e16.place(x=125, y=11)
    l21 = Label(cntrframe2, text="Food Oil", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=80)
    e17 = Entry(cntrframe2, relief=SUNKEN, borderwidth=5)
    e17.place(x=125, y=80)
    l22 = Label(cntrframe2, text="Daal", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=145)
    e18 = Entry(cntrframe2, relief=SUNKEN, borderwidth=5)
    e18.place(x=125, y=145)
    l23 = Label(cntrframe2, text="Wheat", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=210)
    e19 = Entry(cntrframe2, relief=SUNKEN, borderwidth=5)
    e19.place(x=125, y=210)
    l24 = Label(cntrframe2, text="Sugar", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=275)
    e20 = Entry(cntrframe2, relief=SUNKEN, borderwidth=5)
    e20.place(x=125, y=275)
    l25 = Label(cntrframe2, text="Tea", bg="grey", fg="black", font=("comicsansms", 12, "bold"), relief=FLAT).place(
        x=10, y=340)
    e21 = Entry(cntrframe2, relief=SUNKEN, borderwidth=5)
    e21.place(x=125, y=340)
    cntrframe2.pack(side=LEFT, fill=Y, padx=10, pady=10)

    cntrframe3 = LabelFrame(root, text="Billing Area", height="70", width="325", bg="white", fg="BLACK",
                            font=("comicsansms", 20, "bold"), relief=SUNKEN, borderwidth=5)
    sb1 = Scrollbar(cntrframe3)
    sb1.pack(side=RIGHT, fill=Y)
    t1 = Text(cntrframe3, height=700, width=35, yscrollcommand=sb1.set)


    t1.pack(fill=Y, padx=6, pady=6)
    sb1.config(command=t1.yview)
    cntrframe3.pack(side=RIGHT, fill=Y, padx=10, pady=10)

    cntrframe4 = LabelFrame(root, text="Cold Drinks", bg="grey", fg="yellow", font=("comicsansms", 12, "bold"),
                            height="70", width="325", relief=SUNKEN, borderwidth=5)
    l28 = Label(cntrframe4, text="Maza", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=15)
    e22 = Entry(cntrframe4, relief=SUNKEN, borderwidth=5)
    e22.place(x=125, y=11)
    l29 = Label(cntrframe4, text="Cock", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=80)
    e23 = Entry(cntrframe4, relief=SUNKEN, borderwidth=5)
    e23.place(x=125, y=86)
    l30 = Label(cntrframe4, text="Frooti", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(
        x=10, y=145)
    e24 = Entry(cntrframe4, relief=SUNKEN, borderwidth=5)
    e24.place(x=125, y=145)
    l31 = Label(cntrframe4, text="Thumbs Up", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=210)
    e25 = Entry(cntrframe4, relief=SUNKEN, borderwidth=5)
    e25.place(x=125, y=210)
    l32 = Label(cntrframe4, text="Limca", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=275)
    e26 = Entry(cntrframe4, relief=SUNKEN, borderwidth=5)
    e26.place(x=125, y=275)
    l33 = Label(cntrframe4, text="Sprite", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                relief=FLAT).place(x=10, y=340)
    e27 = Entry(cntrframe4, relief=SUNKEN, borderwidth=5)
    e27.place(x=125, y=340)
    cntrframe4.pack(side=RIGHT, fill=Y, padx=10, pady=10)

    root.mainloop()

#Signup window
def sgnup():
    global oge, cpe, cpe2, nme
    root2 = Tk()
    #window of changing the value of items
    def item_values():
        root5 = Tk()
        #write changes in a file.So, that we can pick value in billing window at the time of totaling
        def changed():
            a = e16.get()  # rice
            b = e17.get()  # food oil
            c = e18.get()  # daal
            d = e19.get()  # wheat
            e = e20.get()  # sugar
            f = e21.get()  # tea
            g = e22.get()  # groc tax
            h = e23.get()  # cosc tax
            i = e24.get()  # bath
            j = e25.get()  # face cream
            k = e26.get()  # face wash
            l = e27.get()  # hair spray
            m = e28.get()  # hair gel
            n = e29.get()  # body lotion
            o = e30.get()  # cold tax
            p = e31.get()  # maza
            q = e32.get()  # cocl
            r = e33.get()  # fruti
            s = e34.get()  # thumbs up
            t = e35.get()  # limca
            u = e36.get()  # sprite
            z = open("rc", "w")
            z.write("{}".format(a))
            z.close()
            v = open("fo", "w")
            v.write("{}".format(b))
            v.close()
            w = open("da", "w")
            w.write("{}".format(c))
            w.close()
            x = open("wh", "w")
            x.write("{}".format(d))
            x.close()
            y = open("su", "w")
            y.write("{}".format(e))
            y.close()
            aa = open("te", "w")
            aa.write("{}".format(f))
            aa.close()
            bb = open("grot", "w")
            bb.write("{}".format(g))
            bb.close()
            cc = open("cost", "w")
            cc.write("{}".format(h))
            cc.close()
            dd = open("ba", "w")
            dd.write("{}".format(i))
            dd.close()
            ee = open("fc", "w")
            ee.write("{}".format(j))
            ee.close()
            ff = open("fw", "w")
            ff.write("{}".format(k))
            ff.close()
            gg = open("hs", "w")
            gg.write("{}".format(l))
            gg.close()
            hh = open("hg", "w")
            hh.write("{}".format(m))
            hh.close()
            ii = open("bl", "w")
            ii.write("{}".format(n))
            ii.close()
            jj = open("colt", "w")
            jj.write("{}".format(o))
            jj.close()
            kk = open("mz", "w")
            kk.write("{}".format(p))
            kk.close()
            tt = open("coc", "w")
            tt.write("{}".format(q))
            tt.close()
            ll = open("fru", "w")
            ll.write("{}".format(r))
            ll.close()
            pp = open("thum", "w")
            pp.write("{}".format(s))
            pp.close()
            ww = open("lim", "w")
            ww.write("{}".format(t))
            ww.close()
            qq2 = open("spr", "w")
            qq2.write("{}".format(u))
            qq2.close()
        root5.geometry("1280x720")
        root5.minsize(965, 460)
        root5.title("CHANGE ITEM'S RATE")
        root5.configure(bg="black")
        f12 = LabelFrame(root5, text="Grocery Taxs.", height="251", width="325", bg="grey", fg="yellow",
                         font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
        l43 = Label(f12, text="Taxs.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=80)
        e22 = Entry(f12, relief=SUNKEN, borderwidth=5)
        e22.place(x=125, y=80)
        f12.place(x=10, y=440)
        f9 = LabelFrame(root5, text="Grocery", height="420", width="325", bg="grey", fg="yellow",
                        font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)

        l20 = Label(f9, text="Rice", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=15)
        e16 = Entry(f9, relief=SUNKEN, borderwidth=5)
        e16.place(x=125, y=11)
        l21 = Label(f9, text="Food Oil", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=80)
        e17 = Entry(f9, relief=SUNKEN, borderwidth=5)
        e17.place(x=125, y=80)
        l22 = Label(f9, text="Daal", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=145)
        e18 = Entry(f9, relief=SUNKEN, borderwidth=5)
        e18.place(x=125, y=145)
        l23 = Label(f9, text="Wheat", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=210)
        e19 = Entry(f9, relief=SUNKEN, borderwidth=5)
        e19.place(x=125, y=210)
        l24 = Label(f9, text="Sugar", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=275)
        e20 = Entry(f9, relief=SUNKEN, borderwidth=5)
        e20.place(x=125, y=275)
        l25 = Label(f9, text="Tea", bg="grey", fg="black", font=("comicsansms", 12, "bold"), relief=FLAT).place(
            x=10, y=340)
        e21 = Entry(f9, relief=SUNKEN, borderwidth=5)
        e21.place(x=125, y=340)
        f9.place(x=10, y=10)
        f13 = LabelFrame(root5, text="Cosmetics Taxs.", height="251", width="325", bg="grey", fg="yellow",
                         font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
        l44 = Label(f13, text="Taxs.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=80)
        e23 = Entry(f13, relief=SUNKEN, borderwidth=5)
        e23.place(x=125, y=80)
        f13.place(x=356, y=440)
        f10 = LabelFrame(root5, text="Cosmetics", height="420", width="325", bg="grey", fg="yellow",
                         font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
        l13 = Label(f10, text="Bath Soap", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=15)
        e24 = Entry(f10, relief=SUNKEN, borderwidth=5)
        e24.place(x=125, y=11)
        l14 = Label(f10, text="Face Cream", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=80)
        e25 = Entry(f10, relief=SUNKEN, borderwidth=5)
        e25.place(x=125, y=80)
        l15 = Label(f10, text="Face Wash", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=145)
        e26 = Entry(f10, relief=SUNKEN, borderwidth=5)
        e26.place(x=125, y=145)
        l16 = Label(f10, text="Hair Spray", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=210)
        e27 = Entry(f10, relief=SUNKEN, borderwidth=5)
        e27.place(x=125, y=210)
        l17 = Label(f10, text="Hair Gel", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=275)
        e28 = Entry(f10, relief=SUNKEN, borderwidth=5)
        e28.place(x=125, y=275)
        l18 = Label(f10, text="Body Lotion", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=340)
        e29 = Entry(f10, relief=SUNKEN, borderwidth=5)
        e29.place(x=125, y=340)
        f10.place(x=356, y=10)
        f14 = LabelFrame(root5, text="Cold Drinks Taxs.", height="251", width="325", bg="grey", fg="yellow",
                         font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
        l45 = Label(f14, text="Taxs.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=80)
        e30 = Entry(f14, relief=SUNKEN, borderwidth=5)
        e30.place(x=125, y=80)
        f14.place(x=702, y=440)
        f11 = LabelFrame(root5, text="Cold Drinks", height="420", width="325", bg="grey", fg="yellow",
                         font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
        l28 = Label(f11, text="Maza", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=15)
        e31 = Entry(f11, relief=SUNKEN, borderwidth=5)
        e31.place(x=125, y=11)
        l29 = Label(f11, text="Cock", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=80)
        e32 = Entry(f11, relief=SUNKEN, borderwidth=5)
        e32.place(x=125, y=86)
        l30 = Label(f11, text="Frooti", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(
            x=10, y=145)
        e33 = Entry(f11, relief=SUNKEN, borderwidth=5)
        e33.place(x=125, y=145)
        l31 = Label(f11, text="Thumbs Up", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=210)
        e34 = Entry(f11, relief=SUNKEN, borderwidth=5)
        e34.place(x=125, y=210)
        l32 = Label(f11, text="Limca", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=275)
        e35 = Entry(f11, relief=SUNKEN, borderwidth=5)
        e35.place(x=125, y=275)
        l33 = Label(f11, text="Sprite", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=10, y=340)
        e36 = Entry(f11, relief=SUNKEN, borderwidth=5)
        e36.place(x=125, y=340)
        f11.place(x=702, y=10)
        btn10 = Button(root5, activebackground="black", activeforeground="white", text="Change",
                      font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3, command=changed).place(x=1140, y=600)
        btn9 = Button(root5, activebackground="black", activeforeground="white", text="Back",
                      font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3, command=root5.destroy).place(x=1220, y=600)
        root5.mainloop()
    #About window
    def about():
        root7 = Tk()
        root7.geometry("1280x720")
        root7.minsize(965, 460)
        root7.title("ABOUT")
        root7.configure(bg="black")
        photo = PhotoImage(file="2.png")
        x_lable = Label(image=photo)
        Label.pack(self=x_lable)
        l47 = Label(root7, text="BS", bg="black", fg="Grey", font=("comicsansms", 30, "bold"),
                    relief=FLAT).place(x=650, y=10)
        l46 = Label(root7, text="Billing Software", bg="black", fg="Grey", font=("comicsansms", 30, "bold"),
                    relief=FLAT).place(x=560, y=60)
        l45 = Label(root7, text="Safe Surffing Over Internet, Be Like Anonymous", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=490, y=110)
        l44 = Label(root7, text="Billing Software, Inc. is an American IT Company  based in Menaleo Park,"
                                " Hokaido. It was founded by -------", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=210, y=160)
        l43 = Label(root7, text="along with his fellow roommates and "
                                "students at ------- College,who were Eduardo Saverin, Andrew ",
                    bg="black", fg="Grey", font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=230, y=210)
        l48 = Label(root7, text="McCollum,Dustin Moskovitz  and Chris Hughes, originally as"
                                " BS.com—today's Billing, a ", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=250, y=260)
        l49 = Label(root7, text="popular global IT sollution website. Billing Software is one of the "
                                "world's most valuable companies.", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=230, y=310)
        l50 = Label(root7, text="It is considered one of the Big Five technology companies "
                                "along with", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=320, y=360)
        l50 = Label(root7, text=" -------, A----, Ap----, and G----.", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=450, y=410)
        l51 = Label(root7, text="For Technical Support : ", bg="black", fg="Grey",
                    font=("comicsansms", 18, "bold"),
                    relief=FLAT).place(x=60, y=470)
        l52 = Label(root7, text="Visit : www.companyname.domain/companyname/contact", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=320, y=470)
        l53 = Label(root7, text="Email :  **********@bg.com ", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=320, y=510)
        l54 = Label(root7, text="Call : 1800 200 0047 or 3030 6363", bg="black", fg="Grey",
                    font=("comicsansms", 15, "bold"),
                    relief=FLAT).place(x=320, y=550)
        btn45 = Button(root7, text="Back", bg="black", fg="grey", command=root7.destroy).place(x=1100, y=620)
        root7.mainloop()
    #Admin window
    def Admin():
        if oge.get() != "" and nme.get() != "" and cpe.get() != "":
            if cpe.get() == cpe2.get():
                root = Tk()
                root2.destroy()
                root.geometry("1280x720")
                root.minsize(965, 460)
                root.title("ADMIN CONSOLE")
                root.configure(bg="black")
                #Add Access code window
                def Add_access_code():
                    root5 = Tk()
                    root5.maxsize(400, 400)
                    root5.minsize(400, 400)
                    root5.title("ACCESS CODE")
                    root5.configure(bg="black")
                    global a, b, c, d, x
                    a, b, c, d, x = [], [], [], [], ""
                    def Add(x):
                        list1.insert(END, "{}: {}".format(nme.get(), x))
                        try:
                            f = open("assigned_name", "x")
                            t = open("access_code", "x")
                            if f:
                                if t:
                                    f.close()
                                    f = open("assigned_name", "a")
                                    f.write("{}\n".format(nme.get()))
                                    f.close()
                                    t = open("access_code", "a")
                                    t.write("{}\n".format(x))
                                    t.close()
                                    listbox2.insert(END, x)
                                    listbox.insert(END, nme.get())

                        except:
                            print("already created")
                            f = open("assigned_name", "a")
                            f.write("{}\n".format(nme.get()))
                            f.close()
                            t = open("access_code", "a")
                            t.write("{}\n".format(x))
                            t.close()
                            listbox2.insert(END, x)
                            listbox.insert(END, nme.get())
                    #for generating the random Access code for user login
                    def generate():
                        global a, b, c, d, x
                        a, b, c, d, x = [], [], [], [], ""
                        o = 65
                        for i in range(o, o + 26):
                            p = o + 33
                            for j in range(p - 1, p):
                                if o < 75:
                                    for g in range(o - 64):
                                        c.append(g)
                                l = chr(j)
                                d.append(l)
                            k = chr(i)
                            a.append(k)
                            o += 1
                            if o == 92:
                                break
                        for i in range(2):
                            n = random.choice(a)
                            h = random.choice(c)
                            f = random.choice(d)
                            b.append(h)
                            b.append(f)
                            b.append(n)
                        for i in range(len(b)):
                            x = str(x + "{}".format(b[i]))
                        e1.insert(1, x)
                        Add(x=x)

                    f5 = Frame(root5, width="200", bg="grey", borderwidth=2)
                    l99 = Label(f5, text="Name:").place(x=10, y=1)
                    nme = Entry(f5, borderwidth=2)
                    nme.place(x=20, y=30)
                    e1 = Entry(f5, borderwidth=2)
                    e1.place(x=20, y=79)
                    btn9 = Button(f5, text="Generate", command=generate).place(x=20, y=109)
                    f5.pack(side=RIGHT, fill=Y)
                    f6 = Frame(root5, width="200", relief=SUNKEN, bg="grey", borderwidth=2)
                    list1 = Listbox(f6, height="90", width="200")

                    list1.pack(fill=Y, padx=6, pady=6)
                    f6.pack(side=LEFT, fill=Y)
                    root5.mainloop()

                def dec():
                    root.destroy()
                    main()

                menubar = Menu(root, bg="grey", font=("comicsansms", 12, "bold"))
                Set = Menu(menubar, tearoff=0)
                Set.add_command(label="Access Code", font=("comicsansms", 12, "bold"), command=Add_access_code)
                Set.add_command(label="Item Values and Taxs.", font=("comicsansms", 12, "bold"),
                                command=item_values)
                Set.add_separator()
                Set.add_command(label="Exit", font=("comicsansms", 12, "bold"), command=root.destroy)
                menubar.add_cascade(label="Set", menu=Set)
                Bill = Menu(menubar, tearoff=0)
                Bill.add_command(label="New Billing Window", font=("comicsansms", 12, "bold"), command=dec)
                menubar.add_cascade(label="Bill", menu=Bill)
                Bill.add_separator()
                help = Menu(menubar, tearoff=0)
                help.add_command(label="About", font=("comicsansms", 12, "bold"), command=about)
                menubar.add_cascade(label="Help", menu=help)
                root.config(menu=menubar)
                f10 = Frame(root, height="10", bg="grey", relief=SUNKEN, borderwidth=5)
                l33 = Label(f10, text="List of Access Code", bg="grey", fg="black",
                            font=("comicsansms", 12, "bold"),
                            relief=FLAT).pack()
                f10.pack(side=TOP, fill=X, padx=10, pady=10)
                f12 = Frame(root, height="30", bg="grey")
                l34 = Label(f12, text="Assigned To", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                            relief=FLAT).place(x=50, y=10)
                l35 = Label(f12, text="Access Code", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                            relief=FLAT).place(x=900, y=10)
                f12.pack(side=TOP, fill=X, padx=10)
                f11 = Frame(root, height="800", bg="grey", borderwidth=5)

                listbox = Listbox(f11, height=900, width=100)
                listbox.pack(side=LEFT, fill=Y, padx=6, pady=0)

                listbox2 = Listbox(f11, height=900, width=100)
                try:
                    f = open("assigned_name", "r")
                    z = f.readlines()
                    for i in z:
                        k = i
                        listbox.insert(1, k)
                        f.close()
                    t = open("access_code", "r")
                    j = t.readlines()
                    for i in j:
                        k = i
                        listbox2.insert(1, k)
                except:
                    messagebox.showinfo("information", "no Access code")

                listbox2.pack(side=RIGHT, fill=Y, padx=6, pady=0)

                f11.pack(side=TOP, fill=X, padx=10)
                btn = Button(f12, text="Delete Name",relief=FLAT, command=lambda listbox=listbox: listbox.delete(ANCHOR))
                btn.place(x=450, y=1)
                btn90 = Button(f12, text="Delete Access code",relief=FLAT,
                               command=lambda listbox2=listbox2: listbox2.delete(ANCHOR))
                btn90.place(x=1150, y=1)

                root.mainloop()
            else:
                messagebox.showinfo("Warning", "Conform Password ")

        else:
            messagebox.showinfo("warning", "Fill the details:")
    #for creation of admin account
    def create_ac():
        try:
            f = open("admn", "x").close()
            t = open("pa", "x").close()
            y = open("or", "x").close()
            og = oge.get()
            nam = nme.get()
            pas = cpe.get()
            pa2 = cpe2.get()
            t = open("or", "r")
            g = t.readline()
            f = open("admn", "r")
            d = f.readline()
            if nam != d and og != g:
                f.close()
                t.close()
                if pas == pa2:
                    y = open("or", "w")
                    f = open("admn", "w")
                    t = open("pa", "w")
                    f.write(nam)
                    t.write(pas)
                    y.write(og)
                    f.close()
                    t.close()
                    y.close()
                    messagebox.showinfo("Information", "Created Admin Account")
                    Admin()
                else:
                    messagebox.showinfo("Error", "Confirm Your Password")
            else:
                f.close()
                t.close()
                messagebox.showinfo("Error", "Account Already Exist")
        except:
            og = oge.get()
            nam = nme.get()
            pas = cpe.get()
            pa2 = cpe2.get()
            t = open("or", "r")
            g = t.readline()
            f = open("admn", "r")
            d = f.readline()
            if nam != d and og != g:
                f.close()
                t.close()
                if pas == pa2:
                    y = open("or", "w")
                    f = open("admn", "w")
                    t = open("pa", "w")
                    f.write(nam)
                    t.write(pas)
                    y.write(og)
                    f.close()
                    t.close()
                    y.close()
                    messagebox.showinfo("Information", "Created Admin Account")
                    Admin()
                else:
                    messagebox.showinfo("Error", "Confirm Your Password")
            else:
                f.close()
                t.close()
                messagebox.showinfo("Error", "Account Already Exist")

    root2.title("")
    # root1.minsize(965, 460)
    # root1.maxsize(965, 460)
    f2 = Frame(root2, bg="black", height=460, width=965).pack()
    # root1.configure(bg="black")
    l38 = Label(f2, text="Creating Admin Account.", bg="black", fg="grey",
                font=("comicsansms", 30, "bold")).place(x=250, y=80)
    l39 = Label(f2, text="Organization Name:", bg="black", fg="grey", font=("comicsansms", 20, "bold"),
                relief=FLAT).place(
        x=250, y=170)
    oge = Entry(f2, relief=SUNKEN, borderwidth=5)
    oge.place(x=520, y=170)
    l42 = Label(f2, text="Name:", bg="black", fg="grey", font=("comicsansms", 20, "bold"),
                relief=FLAT).place(
        x=250, y=220)
    nme = Entry(f2, relief=SUNKEN, borderwidth=5)
    nme.place(x=520, y=220)

    l40 = Label(f2, text="Create Password:", bg="black", fg="grey", font=("comicsansms", 20, "bold"),
                relief=FLAT).place(
        x=250, y=270)
    cpe = Entry(f2, show="*", relief=SUNKEN, borderwidth=5)
    cpe.place(x=520, y=270)
    l41 = Label(f2, text="Conform Password:", bg="black", fg="grey", font=("comicsansms", 20, "bold"),
                relief=FLAT).place(x=250, y=320)
    cpe2 = Entry(f2, show="*", relief=SUNKEN, borderwidth=5)
    cpe2.place(x=520, y=320)
    btn8 = Button(f2, text="Create Account", bg="Grey", fg="Black", font=("comicsansms", 20, "bold"),
                  command=create_ac).place(x=620, y=370)
    root2.mainloop()

#Signin window
def sgnin():
    root1 = Tk()
    #destroying root1 and call signup window
    def dis():
        root1.destroy()
        sgnup()
    #call Admin login window from signin screen and destroy root1
    def dis3():
        messagebox.showinfo("Information", "Adminstrator Login Success.")
        root = Tk()
        root1.destroy()
        root.geometry("1280x720")
        root.minsize(965, 460)
        root.title("ADMIN CONSOLE")
        root.configure(bg="black")

        #For making change in value of items
        def item_values():
            root5 = Tk()
            # write changes in a file.So, that we can pick value in billing window at the time of totaling
            def changed():
                a = e16.get()  # rice
                b = e17.get()  # food oil
                c = e18.get()  # daal
                d = e19.get()  # wheat
                e = e20.get()  # sugar
                f = e21.get()  # tea
                g = e22.get()  # groc tax
                h = e23.get()  # cosc tax
                i = e24.get()  # bath
                j = e25.get()  # face cream
                k = e26.get()  # face wash
                l = e27.get()  # hair spray
                m = e28.get()  # hair gel
                n = e29.get()  # body lotion
                o = e30.get()  # cold tax
                p = e31.get()  # maza
                q = e32.get()  # cocl
                r = e33.get()  # fruti
                s = e34.get()  # thumbs up
                t = e35.get()  # limca
                u = e36.get()  # sprite
                z = open("rc", "w")
                z.write("{}".format(a))
                z.close()
                v = open("fo", "w")
                v.write("{}".format(b))
                v.close()
                w = open("da", "w")
                w.write("{}".format(c))
                w.close()
                x = open("wh", "w")
                x.write("{}".format(d))
                x.close()
                y = open("su", "w")
                y.write("{}".format(e))
                y.close()
                aa = open("te", "w")
                aa.write("{}".format(f))
                aa.close()
                bb = open("grot", "w")
                bb.write("{}".format(g))
                bb.close()
                cc = open("cost", "w")
                cc.write("{}".format(h))
                cc.close()
                dd = open("ba", "w")
                dd.write("{}".format(i))
                dd.close()
                ee = open("fc", "w")
                ee.write("{}".format(j))
                ee.close()
                ff = open("fw", "w")
                ff.write("{}".format(k))
                ff.close()
                gg = open("hs", "w")
                gg.write("{}".format(l))
                gg.close()
                hh = open("hg", "w")
                hh.write("{}".format(m))
                hh.close()
                ii = open("bl", "w")
                ii.write("{}".format(n))
                ii.close()
                jj = open("colt", "w")
                jj.write("{}".format(o))
                jj.close()
                kk = open("mz", "w")
                kk.write("{}".format(p))
                kk.close()
                tt = open("coc", "w")
                tt.write("{}".format(q))
                tt.close()
                ll = open("fru", "w")
                ll.write("{}".format(r))
                ll.close()
                pp = open("thum", "w")
                pp.write("{}".format(s))
                pp.close()
                ww = open("lim", "w")
                ww.write("{}".format(t))
                ww.close()
                qq2=open("spr","w")
                qq2.write("{}".format(u))
                qq2.close()
            root5.geometry("1280x720")
            root5.minsize(965, 460)
            root5.title("CHANGE ITEM'S RATE")
            root5.configure(bg="black")
            f12 = LabelFrame(root5, text="Grocery Taxs.", height="251", width="325", bg="grey", fg="yellow",
                             font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
            l43 = Label(f12, text="Taxs.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=80)
            e22 = Entry(f12, relief=SUNKEN, borderwidth=5)
            e22.place(x=125, y=80)
            f12.place(x=10, y=440)
            f9 = LabelFrame(root5, text="Grocery", height="420", width="325", bg="grey", fg="yellow",
                            font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)

            l20 = Label(f9, text="Rice", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=15)
            e16 = Entry(f9, relief=SUNKEN, borderwidth=5)
            e16.place(x=125, y=11)
            l21 = Label(f9, text="Food Oil", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=80)
            e17 = Entry(f9, relief=SUNKEN, borderwidth=5)
            e17.place(x=125, y=80)
            l22 = Label(f9, text="Daal", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=145)
            e18 = Entry(f9, relief=SUNKEN, borderwidth=5)
            e18.place(x=125, y=145)
            l23 = Label(f9, text="Wheat", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=210)
            e19 = Entry(f9, relief=SUNKEN, borderwidth=5)
            e19.place(x=125, y=210)
            l24 = Label(f9, text="Sugar", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=275)
            e20 = Entry(f9, relief=SUNKEN, borderwidth=5)
            e20.place(x=125, y=275)
            l25 = Label(f9, text="Tea", bg="grey", fg="black", font=("comicsansms", 12, "bold"), relief=FLAT).place(
                x=10, y=340)
            e21 = Entry(f9, relief=SUNKEN, borderwidth=5)
            e21.place(x=125, y=340)
            f9.place(x=10, y=10)
            f13 = LabelFrame(root5, text="Cosmetics Taxs.", height="251", width="325", bg="grey", fg="yellow",
                             font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
            l44 = Label(f13, text="Taxs.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=80)
            e23 = Entry(f13, relief=SUNKEN, borderwidth=5)
            e23.place(x=125, y=80)
            f13.place(x=356, y=440)
            f10 = LabelFrame(root5, text="Cosmetics", height="420", width="325", bg="grey", fg="yellow",
                             font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
            l13 = Label(f10, text="Bath Soap", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=15)
            e24 = Entry(f10, relief=SUNKEN, borderwidth=5)
            e24.place(x=125, y=11)
            l14 = Label(f10, text="Face Cream", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=80)
            e25 = Entry(f10, relief=SUNKEN, borderwidth=5)
            e25.place(x=125, y=80)
            l15 = Label(f10, text="Face Wash", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=145)
            e26 = Entry(f10, relief=SUNKEN, borderwidth=5)
            e26.place(x=125, y=145)
            l16 = Label(f10, text="Hair Spray", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=210)
            e27 = Entry(f10, relief=SUNKEN, borderwidth=5)
            e27.place(x=125, y=210)
            l17 = Label(f10, text="Hair Gel", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=275)
            e28 = Entry(f10, relief=SUNKEN, borderwidth=5)
            e28.place(x=125, y=275)
            l18 = Label(f10, text="Body Lotion", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=340)
            e29 = Entry(f10, relief=SUNKEN, borderwidth=5)
            e29.place(x=125, y=340)
            f10.place(x=356, y=10)
            f14 = LabelFrame(root5, text="Cold Drinks Taxs.", height="251", width="325", bg="grey", fg="yellow",
                             font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
            l45 = Label(f14, text="Taxs.", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=80)
            e30 = Entry(f14, relief=SUNKEN, borderwidth=5)
            e30.place(x=125, y=80)
            f14.place(x=702, y=440)
            f11 = LabelFrame(root5, text="Cold Drinks", height="420", width="325", bg="grey", fg="yellow",
                             font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=5)
            l28 = Label(f11, text="Maza", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=15)
            e31 = Entry(f11, relief=SUNKEN, borderwidth=5)
            e31.place(x=125, y=11)
            l29 = Label(f11, text="Cock", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=80)
            e32 = Entry(f11, relief=SUNKEN, borderwidth=5)
            e32.place(x=125, y=86)
            l30 = Label(f11, text="Frooti", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(
                x=10, y=145)
            e33 = Entry(f11, relief=SUNKEN, borderwidth=5)
            e33.place(x=125, y=145)
            l31 = Label(f11, text="Thumbs Up", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=210)
            e34 = Entry(f11, relief=SUNKEN, borderwidth=5)
            e34.place(x=125, y=210)
            l32 = Label(f11, text="Limca", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=275)
            e35 = Entry(f11, relief=SUNKEN, borderwidth=5)
            e35.place(x=125, y=275)
            l33 = Label(f11, text="Sprite", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                        relief=FLAT).place(x=10, y=340)
            e36 = Entry(f11, relief=SUNKEN, borderwidth=5)
            e36.place(x=125, y=340)
            f11.place(x=702, y=10)
            btn10 = Button(root5, activebackground="black", activeforeground="white", text="Change",
                      font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3, command=changed).place(x=1140, y=600)
            btn9 = Button(root5, activebackground="black", activeforeground="white", text="Back",
                          font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3, command=root5.destroy).place(
                x=1220, y=600)
            root5.mainloop()
        #this is just About page
        def about():
            root7 = Tk()
            root7.geometry("1280x720")
            root7.minsize(965, 460)
            root7.title("ABOUT")
            root7.configure(bg="black")
            photo = PhotoImage(file="2.png")
            x_lable = Label(image=photo)
            Label.pack(self=x_lable)
            l47 = Label(root7, text="BS", bg="black", fg="Grey", font=("comicsansms", 30, "bold"),
                        relief=FLAT).place(x=650, y=10)
            l46 = Label(root7, text="Billing Software", bg="black", fg="Grey", font=("comicsansms", 30, "bold"),
                        relief=FLAT).place(x=560, y=60)
            l45 = Label(root7, text="Safe Surffing Over Internet, Be Like Anonymous", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=490, y=110)
            l44 = Label(root7, text="Billing Software, Inc. is an American IT Company  based in Menaleo Park,"
                                    " Hokaido. It was founded by -------", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=210, y=160)
            l43 = Label(root7, text="along with his fellow roommates and "
                                    "students at ------- College,who were Eduardo Saverin, Andrew ",
                        bg="black", fg="Grey", font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=230, y=210)
            l48 = Label(root7, text="McCollum,Dustin Moskovitz  and Chris Hughes, originally as"
                                    " BS.com—today's Billing, a ", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=250, y=260)
            l49 = Label(root7, text="popular global IT sollution website. Billing Software is one of the "
                                    "world's most valuable companies.", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=230, y=310)
            l50 = Label(root7, text="It is considered one of the Big Five technology companies "
                                    "along with", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=320, y=360)
            l50 = Label(root7, text=" -------, A----, Ap----, and G----.", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=450, y=410)
            l51 = Label(root7, text="For Technical Support : ", bg="black", fg="Grey",
                        font=("comicsansms", 18, "bold"),
                        relief=FLAT).place(x=60, y=470)
            l52 = Label(root7, text="Visit : www.companyname.domain/companyname/contact", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=320, y=470)
            l53 = Label(root7, text="Email :  **********@bg.com ", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=320, y=510)
            l54 = Label(root7, text="Call : 1800 200 0047 or 3030 6363", bg="black", fg="Grey",
                        font=("comicsansms", 15, "bold"),
                        relief=FLAT).place(x=320, y=550)
            btn45 = Button(root7, text="Back", bg="black", fg="grey", command=root7.destroy).place(x=1100, y=620)
            root7.mainloop()
        #Trigger Add access code window
        def Add_access_code():
            root5 = Tk()
            root5.maxsize(400, 400)
            root5.minsize(400, 400)
            root5.title("ACCESS CODE")
            root5.configure(bg="black")
            global a, b, c, d, x
            a, b, c, d, x = [], [], [], [], ""
            def Add(x):
                list1.insert(END, "{}: {}".format(nme.get(), x))
                try:
                    f = open("assigned_name", "x")
                    t = open("access_code", "x")
                    if f:
                        if t:
                            f.close()
                            f = open("assigned_name", "a")
                            f.write("{}\n".format(nme.get()))
                            f.close()
                            t = open("access_code", "a")
                            t.write("{}\n".format(x))
                            t.close()
                            listbox2.insert(END, x)
                            listbox.insert(END, nme.get())

                except:
                    print("already created")
                    f = open("assigned_name", "a")
                    f.write("{}\n".format(nme.get()))
                    f.close()
                    t = open("access_code", "a")
                    t.write("{}\n".format(x))
                    t.close()
                    listbox2.insert(END, x)
                    listbox.insert(END, nme.get())
            #generating random Access Code For user Login
            def generate():
                global a, b, c, d, x
                a, b, c, d, x = [], [], [], [], ""
                o = 65
                for i in range(o, o + 26):
                    p = o + 33
                    for j in range(p - 1, p):
                        if o < 75:
                            for g in range(o - 64):
                                c.append(g)
                        l = chr(j)
                        d.append(l)
                    k = chr(i)
                    a.append(k)
                    o += 1
                    if o == 92:
                        break
                for i in range(2):
                    n = random.choice(a)
                    h = random.choice(c)
                    f = random.choice(d)
                    b.append(h)
                    b.append(f)
                    b.append(n)
                for i in range(len(b)):
                    x = str(x + "{}".format(b[i]))
                e1.insert(1, x)
                Add(x=x)

            f5 = Frame(root5, width="200", bg="grey", borderwidth=2)
            l99 = Label(f5, text="Name:").place(x=10, y=1)
            nme = Entry(f5, borderwidth=2)
            nme.place(x=20, y=30)
            e1 = Entry(f5, borderwidth=2)
            e1.place(x=20, y=79)
            btn9 = Button(f5, text="Generate", command=generate).place(x=20, y=109)
            f5.pack(side=RIGHT, fill=Y)
            f6 = Frame(root5, width="200", relief=SUNKEN, bg="grey", borderwidth=2)
            list1 = Listbox(f6, height="90", width="200")

            list1.pack(fill=Y, padx=6, pady=6)
            f6.pack(side=LEFT, fill=Y)
            root5.mainloop()
        #destroying root and calling main
        def dec():
            root.destroy()
            main()

        menubar = Menu(root, bg="grey", font=("comicsansms", 12, "bold"))
        Set = Menu(menubar, tearoff=0)
        Set.add_command(label="Access Code", font=("comicsansms", 12, "bold"), command=Add_access_code)
        Set.add_command(label="Item Values and Taxs.", font=("comicsansms", 12, "bold"), command=item_values)
        Set.add_separator()
        Set.add_command(label="Exit", font=("comicsansms", 12, "bold"), command=root.destroy)
        menubar.add_cascade(label="Set", menu=Set)
        Bill = Menu(menubar, tearoff=0)
        Bill.add_command(label="New Billing Window", font=("comicsansms", 12, "bold"), command=dec)
        menubar.add_cascade(label="Bill", menu=Bill)
        Bill.add_separator()
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About", font=("comicsansms", 12, "bold"), command=about)
        menubar.add_cascade(label="Help", menu=help)
        root.config(menu=menubar)
        f10 = Frame(root, height="10", bg="grey", relief=SUNKEN, borderwidth=5)
        l33 = Label(f10, text="List of Access Code", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).pack()
        f10.pack(side=TOP, fill=X, padx=10, pady=10)
        f12 = Frame(root, height="30", bg="grey")
        l34 = Label(f12, text="Assigned To", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=50, y=10)
        l35 = Label(f12, text="Access Code", bg="grey", fg="black", font=("comicsansms", 12, "bold"),
                    relief=FLAT).place(x=900, y=10)
        f12.pack(side=TOP, fill=X, padx=10)
        f11 = Frame(root, height="800", bg="grey", borderwidth=5)

        listbox = Listbox(f11, height=900, width=100)
        listbox.pack(side=LEFT, fill=Y, padx=6, pady=0)
        listbox2 = Listbox(f11, height=900, width=100)
        try:
            f = open("assigned_name", "r")
            z = f.readlines()
            for i in z:
                k = i
                listbox.insert(1, k)
                f.close()
            t = open("access_code", "r")
            j = t.readlines()
            for i in j:
                k = i
                listbox2.insert(1, k)
        except:
            messagebox.showinfo("information", "no Access code")

        listbox2.pack(side=RIGHT, fill=Y, padx=6, pady=0)


        f11.pack(side=TOP, fill=X, padx=10)
        btn = Button(f12, text="Delete Name",relief=FLAT, command=lambda listbox=listbox: listbox.delete(ANCHOR))
        btn.place(x=450, y=1)
        btn90 = Button(f12, text="Delete Access code",relief=FLAT, command=lambda listbox2=listbox2: listbox2.delete(ANCHOR))
        btn90.place(x=1150, y=1)
        root.mainloop()
    #it will decide on the bases of Entered Access code that, the end user is adminstrator or user
    #So, as a result it will call Admin window or User window(Billing window)
    def pro():
        # f = open("sign_in.log", "w").write(sie.get())
        try:
            f = open("pa", "r")
            f.close()
        except:
            messagebox.showinfo("Error","Create a Admin Account First\n Click on SignUp to create")
        k = sie.get()
        if k != "":
            f = open("pa", "r")
            s = f.readline()
            if s != k:
                y = open("access_code", "r")
                d = y.readline()
                if k in d:
                    messagebox.showinfo("information", "User Login Success")
                    root1.destroy()
                    f.close()
                    main()
                else:
                    f.close()
                    messagebox.showinfo("warning", "Incorrect Access Code")
            else:
                dis3()
        else:
            messagebox.showinfo("Information", "Enter Access Code")

    # n = root
    root1.title("")
    # root1.minsize(965, 460)
    # root1.maxsize(965, 460)
    f1 = Frame(root1, bg="black", height=460, width=965).pack()
    # root1.configure(bg="black")
    l35 = Label(f1, text="SignIn TO BILLING SOFTWARE.", bg="black", fg="grey",
                font=("comicsansms", 30, "bold")).place(x=190, y=80)
    l36 = Label(f1, text="Access Code", bg="black", fg="grey", font=("comicsansms", 20, "bold"), relief=FLAT).place(
        x=270, y=170)
    global sie
    sie = Entry(f1, show="*", relief=SUNKEN, borderwidth=5)
    sie.place(x=450, y=170)
    btn8 = Button(f1, text="SignIn", bg="Grey", fg="Black", font=("comicsansms", 20, "bold"),
                  command=pro).place(x=620, y=300)
    l37 = Label(f1, text="If you are new at Billing Software,then", bg="black", fg="grey",
                font=("comicsansms", 20, "bold"),
                relief=FLAT).place(x=220, y=360)
    btn9 = Button(f1, text="SignUp", bg="black", fg="Blue", font=("comicsansms", 10, "bold"), relief=FLAT,
                  command=dis).place(x=650, y=360)
    root1.mainloop()
#destroy root window then,go for signin window
def dis():
    root.destroy()
    sgnin()
#destroy root window then,go for signup window
def dis2():
    root.destroy()
    sgnup()
root.title("")
photo = PhotoImage(file="IMG_20200626_141510.png")
x_lable = Label(image=photo)
Label.pack(self=x_lable)
root.minsize(880, 460)
root.maxsize(880, 460)
root.configure(bg="black")
l34 = Label(root, text="WELCOME TO BILLING SOFT", bg="black", fg="grey",
            font=("comicsansms", 30, "bold")).place(x=130, y=80)
btn6 = Button(root, text="SignIn", bg="Grey", fg="Black", font=("comicsansms", 20, "bold"),
              command=dis).place(x=170, y=300)
btn7 = Button(root, text="SignUp", bg="Grey", fg="Black", font=("comicsansms", 20, "bold"),
              command=dis2).place(x=610, y=300)
root.mainloop()
