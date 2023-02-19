import budget
import bookitem
from tkinter import *
from tkinter import messagebox

formA = Tk()
formA.title('โปรแกรมซื้อชายหนังสือ')
formA.geometry('400x500')

global netamt
global sum_payment
global sum_receive
global payment
global receive

payment=0
sum_payment=0
sum_receive=0


def button1_clicked():
    bookname = input('กรุณาใส่ชื่อหนังสือ ')
    bookitem.book.append(bookname)
    message = "รายการหนังสือที่ซื้อคือ "+bookname
    messagebox.showinfo("Message",message)    
B1 = Button(formA,text='บันทึกการซื้อหนังสือ',command=button1_clicked)
B1.place(x=10,y=20)

def button2_clicked():
    payment = int(input('กรุณาใส่จำนวนเงินค่าซื้อหนังสือ  '))
    print(payment)
    sumpayment(payment)
    #print(sum_payment)
    #message1 = "จำนวนเงินที่จ่ายเท่ากับ "+str(payment)+" บาท"
    #message2 = "และมียอดจ่ายซื้อสะสมเท่ากับ "+str(sum_payment)+" บาท"
    #messagebox.showinfo("Message",message1+message2)
B2 = Button(formA,text='บันทึกจ่ายเงินค่าหนังสือ',command=button2_clicked)
B2.place(x=10,y=50)

def button3_clicked():
    bookname = input('กรุณาใส่ชื่อหนังสือ ')
    bookitem.book.remove(bookname)
    message = "รายการหนังสือที่ขายคือ "+bookname
    messagebox.showinfo("Message",message) 
B3 = Button(formA,text='บันทึกการขายหนังสือ',command=button3_clicked)
B3.place(x=10,y=80)

def button4_clicked():
    receive = int(input('กรุณาใส่จำนวนเงินค่าขายหนังสือ  '))
    budgetbal = budget.balance
    sum_receive=recieve+sum_receive
    message1 = "จำนวนเงินที่ขายเท่ากับ "+str(receive)+" บาท"
    message2 = "และมียอดเงินรับค่าขายสะสมเท่ากับ "+str(sum_receive)+" บาท"
    messagebox.showinfo("Message",message1+message2)
B4 = Button(formA,text='บันทึกการรับเงินค่าขายหนังสือ',command=button4_clicked)
B4.place(x=10,y=110)

def button5_clicked():
    print("รายการหนังสือคงเหลือคือ")
    print(bookitem.book)
B5 = Button(formA,text='แสดงรายการหนังสือคงเหลือ',command=button5_clicked)
B5.place(x=10,y=140)

def button6_clicked():
    print("จำนวนยอดเงินคงเหลือเท่ากับ")
    budgetbal = budget.balance
    totalnetamt=budgetbal.balance+sum_receive-sum_payment
    print(str(totalnetamt)+"  บาท")
B6 = Button(formA,text='แสดงเงินสดคงเหลือ',command=button6_clicked)
B6.place(x=10,y=170)


def sumpayment(payment):
    sum_payment = sum_payment+payment
    return sum_payment
sumpayment(payment)
print(sum_payment)

def sumreceive():
    sum_receive = sum_receive+receive
    return sum_receive

def sumbalance():
    netamt=budget.balance+sum_receive-sum_payment
    return netamt






formA.mainloop()





