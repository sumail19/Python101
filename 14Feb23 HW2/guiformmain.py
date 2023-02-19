import budget
import bookitem
from tkinter import *
from tkinter import messagebox

formA = Tk()
formA.title('โปรแกรมซื้อชายหนังสือ')
formA.geometry('400x500')

def button1_clicked():
    bookname = input('กรุณาใส่ชื่อหนังสือที่ซื้อ ')
    bookitem.book.append(bookname)
    message = "รายการหนังสือที่ซื้อคือ "+bookname
    messagebox.showinfo("Message",message)    
B1 = Button(formA,text='บันทึกการซื้อหนังสือ',command=button1_clicked)
B1.place(x=10,y=20)

def button2_clicked():
    payment = int(input('กรุณาใส่จำนวนเงินค่าซื้อหนังสือ '))
    message = "จำนวนเงินที่จ่ายเท่ากับ "+str(payment)+" บาท" 
    messagebox.showinfo("Message",message)
B2 = Button(formA,text='บันทึกจ่ายเงินค่าหนังสือ',command=button2_clicked)
B2.place(x=10,y=50)

def button3_clicked():
    bookname = input('กรุณาใส่ชื่อหนังสือที่ขาย ')
    bookitem.book.remove(bookname)
    message = "รายการหนังสือที่ขายคือ "+bookname
    messagebox.showinfo("Message",message) 
B3 = Button(formA,text='บันทึกการขายหนังสือ',command=button3_clicked)
B3.place(x=10,y=80)

def button4_clicked():
    receive = int(input('กรุณาใส่จำนวนเงินค่าขายหนังสือ '))
    message = "จำนวนเงินที่ขายเท่ากับ "+str(receive)+" บาท"   
    messagebox.showinfo("Message",message)
B4 = Button(formA,text='บันทึกการรับเงินค่าขายหนังสือ',command=button4_clicked)
B4.place(x=10,y=110)

def button5_clicked():
    print("รายการหนังสือคงเหลือคือ")
    print(bookitem.book)
B5 = Button(formA,text='แสดงรายการหนังสือคงเหลือ',command=button5_clicked)
B5.place(x=10,y=140)

formA.mainloop()





