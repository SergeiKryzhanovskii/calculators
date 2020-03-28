# !/usr/bin/python3

from tkinter import *
from tkinter import messagebox



def help():
    messagebox.showinfo('Help', 'Введите 2 числа.\nВыберите необходимую операцию:\n"сложение" или "+"; \n"вычитание" или "-";'
                                '\n"умножение" или "*"; \n"деление" или "/"; \n"степень" или "^".')


def operation_add():
    add = int(txt1.get()) + int(txt2.get())
    lbl_x.configure(text='Ответ: {}'.format(add))


def operation_sub():
    add = int(txt1.get()) - int(txt2.get())
    lbl_x.configure(text='Ответ: {}'.format(add))


def operation_mult():
    add = int(txt1.get()) * int(txt2.get())
    lbl_x.configure(text='Ответ: {}'.format(add))


def operation_dev():
    add = int(txt1.get()) / int(txt2.get())
    lbl_x.configure(text='Ответ: {}'.format(add))


def operation_cub():
    add = int(txt1.get()) ** int(txt2.get())
    lbl_x.configure(text='Ответ: {}'.format(add))


window = Tk()
window.title('Simple calculator')
window.geometry('400x250+300+200')
window.resizable(False, False)
lbl1 = Label(window, text='Введите числа:').grid(column=0, row=0)
lbl2 = Label(window, text='Число 1:').grid(column=0, row=1)
txt1 = Entry(window, width=35)
txt1.grid(column=1, row=1, columnspan=4)
txt1.focus()
lbl3 = Label(window, text='Число 2:').grid(column=0, row=2)
txt2 = Entry(window, width=35)
txt2.grid(column=1, row=2, columnspan=4)
lbl4 = Label(window, text='').grid(column=0, row=5)
lbl_x = Label(window, text='')
lbl_x.grid(column=0, row=6)
btn_add = Button(window, text=' + ', font=('Arial', 20), command=operation_add).grid(column=0, row=5)
btn_sub = Button(window, text=' - ', font=('Arial', 20), command=operation_sub).grid(column=1, row=5)
btn_mult = Button(window, text=' x ', font=('Arial', 20), command=operation_mult).grid(column=2, row=5)
btn_dev = Button(window, text=' / ', font=('Arial', 20), command=operation_dev).grid(column=3, row=5)
btn_cub = Button(window, text=' ^ ', font=('Arial', 20), command=operation_cub).grid(column=4, row=5)
btn_help = Button(window, text='Help', command=help)
btn_help.grid(column=0, row=7)

window.mainloop()