import tkinter as tk
from tkinter import ttk
import math

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simpl()

    def simpl(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __radd__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __rsub__(self, other):
        numerator = other.numerator * self.denominator - self.numerator * other.denominator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __rmul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            return 'Ошибка: деление на 0'
        else:
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator, denominator)

    def __rtruediv__(self, other):
        if other.numerator == 0:
            return 0
        else:
            numerator = self.denominator * other.numerator
            denominator = self.numerator * other.denominator
            return Rational(numerator, denominator)

    def __pow__(self, power, modulo=None):
        numerator = self.numerator ** power
        denominator = self.denominator ** power
        return Rational(numerator, denominator)



class Calculator2:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.current_field = 'num1'

        self.create_widgets()

    def create_widgets(self):
        #Поля для ввода и вывода
        ttk.Label(self.root, text="Число 1:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.root, text="Число 2:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.root, text="Результат:").grid(row=2, column=0, padx=5, pady=5)

        self.num1_entry = ttk.Entry(self.root, textvariable=self.num1_var)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_entry = ttk.Entry(self.root, textvariable=self.num2_var)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.result_entry = ttk.Entry(self.root, textvariable=self.result_var, state='readonly')
        self.result_entry.grid(row=2, column=1, padx=5, pady=5)

        #Кнопки операций
        self.button_neg = ttk.Button(self.root, text='-', command=lambda: self.append_digit('-'))
        self.button_neg.grid(row=3, column=0, padx=5, pady=5)

        self.button1 = ttk.Button(self.root, text='/', command=lambda: self.append_digit('/'))
        self.button1.grid(row=3, column=1, padx=5, pady=5)

        self.switching_button = ttk.Button(self.root, text="-->", command=self.switching)
        self.switching_button.grid(row=3, column=2, padx=5, pady=5)

        #Кнопки ввода
        self.button1 = ttk.Button(self.root, text='1', command=lambda: self.append_digit('1'))
        self.button1.grid(row=4, column=0, padx=5, pady=5)

        self.button2 = ttk.Button(self.root, text='2', command=lambda: self.append_digit('2'))
        self.button2.grid(row=4, column=1, padx=5, pady=5)

        self.button3 = ttk.Button(self.root, text='3', command=lambda: self.append_digit('3'))
        self.button3.grid(row=4, column=2, padx=5, pady=5)

        self.button4 = ttk.Button(self.root, text='4', command=lambda: self.append_digit('4'))
        self.button4.grid(row=5, column=0, padx=5, pady=5)

        self.button5 = ttk.Button(self.root, text='5', command=lambda: self.append_digit('5'))
        self.button5.grid(row=5, column=1, padx=5, pady=5)

        self.button6 = ttk.Button(self.root, text='6', command=lambda: self.append_digit('6'))
        self.button6.grid(row=5, column=2, padx=5, pady=5)

        self.button7 = ttk.Button(self.root, text='7', command=lambda: self.append_digit('7'))
        self.button7.grid(row=6, column=0, padx=5, pady=5)

        self.button8 = ttk.Button(self.root, text='8', command=lambda: self.append_digit('8'))
        self.button8.grid(row=6, column=1, padx=5, pady=5)

        self.button9 = ttk.Button(self.root, text='9', command=lambda: self.append_digit('9'))
        self.button9.grid(row=6, column=2, padx=5, pady=5)

        self.button0 = ttk.Button(self.root, text='0', command=lambda: self.append_digit('0'))
        self.button0.grid(row=7, column=0, padx=5, pady=5)

        self.button_clear = ttk.Button(self.root, text='C', command=self.clear_last)
        self.button_clear.grid(row=7, column=2, padx=5, pady=5)

        #Операции
        self.div_button = ttk.Button(self.root, text="div", command=self.div)
        self.div_button.grid(row=8, column=0, padx=5, pady=5)

        self.div_button = ttk.Button(self.root, text="*", command=self.mul)
        self.div_button.grid(row=8, column=1, padx=5, pady=5)

        self.div_button = ttk.Button(self.root, text="+", command=self.add)
        self.div_button.grid(row=8, column=2, padx=5, pady=5)

        self.div_button = ttk.Button(self.root, text="-", command=self.sub)
        self.div_button.grid(row=9, column=0, padx=5, pady=5)

        self.div_button = ttk.Button(self.root, text="**", command=self.pow)
        self.div_button.grid(row=9, column=1, padx=5, pady=5)

    def splitf(self, s):
        if '/' in s:
            num, den = map(int, s.split('/'))
        else:
            num = int(s)
            den = 1
        return Rational(num, den)

    def append_digit(self, digit):
        if self.current_field == 'num1':
            current_var = self.num1_var
        else:
            current_var = self.num2_var
        if digit == '-' and current_var.get():
            return
        current_var.set(current_var.get() + digit)

    def clear_last(self):
        if self.current_field == 'num1':
            current_var = self.num1_var
        else: current_var = self.num2_var
        current_var.set(current_var.get()[:-1])

    def switching(self):
        if self.current_field == 'num1':
            self.current_field = 'num2'
        else: self.current_field = 'num1'

    def add(self):
        num1 = self.splitf(self.num1_var.get())
        num2 = self.splitf(self.num2_var.get())
        self.result_var.set(str(num1 + num2))

    def sub(self):
        num1 = self.splitf(self.num1_var.get())
        num2 = self.splitf(self.num2_var.get())
        self.result_var.set(str(num1 - num2))

    def mul(self):
        num1 = self.splitf(self.num1_var.get())
        num2 = self.splitf(self.num2_var.get())
        self.result_var.set(str(num1 * num2))

    def div(self):
        num1 = self.splitf(self.num1_var.get())
        num2 = self.splitf(self.num2_var.get())
        self.result_var.set(str(num1 / num2))

    def pow(self):
        num1 = self.splitf(self.num1_var.get())
        num2 = self.splitf(self.num2_var.get())
        self.result_var.set(str(num1 ** num2.numerator))

root = tk.Tk()
Calculator2(root)
root.mainloop()

