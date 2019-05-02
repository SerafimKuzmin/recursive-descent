from enum import Enum
import math
from tkinter import *


class Sign(Enum):
    minus = 1
    plus = 2
    mul = 3
    div = 4
    pw = 5
    last = 6
    op = 7
    cl = 8
    number = 9
    variable = 10
    function = 11


class Calculator:
    def __init__(self):
        self.variables = dict()
        self.formula = ""
        self.ind = 0
        self.master = Tk()
        self.master.geometry("600x400")
        self.button1 = Button(self.master, text = "1", width = 3, height = 2, command = self.clicked_button1)
        self.button1.place(x = 200, y = 25)
        self.button2 = Button(self.master, text = "2", width = 3, height = 2, command = self.clicked_button2)
        self.button2.place(x = 230, y = 25)
        self.button3 = Button(self.master, text = "3", width = 3, height = 2, command = self.clicked_button3)
        self.button3.place(x = 260, y = 25)
        self.plus = Button(self.master, text = "+", width = 3, height = 2, command = self.clicked_plus)
        self.plus.place(x = 290, y = 25)
        self.button = Button(self.master, text = "=", width = 3, height = 2, command = self.clicked)
        self.button.place(x = 320, y = 25)
        self.dot = Button(self.master, text = "CE", width = 3, height = 2, command = self.clicked_del)
        self.dot.place(x = 350, y = 25)
        self.button4 = Button(self.master, text = "4", width = 3, height = 2, command = self.clicked_button4)
        self.button4.place(x = 200, y = 60)
        self.button5 = Button(self.master, text = "5", width = 3, height = 2, command = self.clicked_button5)
        self.button5.place(x = 230, y = 60)
        self.button6 = Button(self.master, text = "6", width = 3, height = 2, command = self.clicked_button6)
        self.button6.place(x = 260, y = 60)
        self.minus = Button(self.master, text = "-", width = 3, height = 2, command = self.clicked_minus)
        self.minus.place(x = 290, y = 60)
        self.parenthesis = Button(self.master, text = "(", width = 3, height = 2, command = self.clicked_parenthesis)
        self.parenthesis.place(x = 320,y = 60)
        self.parenthesis0 = Button(self.master, text = ")", width = 3, height = 2, command = self.clicked_parenthesis0)
        self.parenthesis0.place(x = 350,y = 60)
        self.button7 = Button(self.master, text = "7", width = 3, height = 2, command = self.clicked_button7)
        self.button7.place(x = 200, y = 95)
        self.button8 = Button(self.master, text = "8", width = 3, height = 2, command = self.clicked_button8)
        self.button8.place(x = 230, y = 95)
        self.button9 = Button(self.master, text = "9", width = 3, height = 2, command = self.clicked_button9)
        self.button9.place(x = 260, y = 95)
        self.multiply = Button(self.master, text = "*", width = 3, height = 2, command = self.clicked_multiply)
        self.multiply.place(x = 290, y = 95)
        self.button_sin = Button(self.master, text = "sin", width = 3, height = 2, command = self.clicked_sin)
        self.button_sin.place(x = 320, y = 95)
        self.button_cos = Button(self.master, text = "cos", width = 3, height = 2, command = self.clicked_cos)
        self.button_cos.place(x = 350, y = 95)
        self.dot = Button(self.master, text = ".", width = 3, height = 2, command = self.clicked_dot)
        self.dot.place(x = 200, y = 130)
        self.button0 = Button(self.master, text = "0", width = 3, height = 2, command = self.clicked_button0)
        self.button0.place(x = 230, y = 130)
        self.exp = Button(self.master, text = "^", width = 3, height = 2, command = self.clicked_exp)
        self.exp.place(x = 260, y = 130)
        self.div = Button(self.master, text = "/", width = 3, height = 2, command = self.clicked_div)
        self.div.place(x = 290, y = 130)
        self.button_tg = Button(self.master, text = "tg", width = 3, height = 2, command = self.clicked_tg)
        self.button_tg.place(x = 320, y = 130)
        self.button_ctg = Button(self.master, text = "ctg", width = 3, height = 2, command = self.clicked_ctg)
        self.button_ctg.place(x = 350, y = 130)
        self.button_asin = Button(self.master, text = "asin", width = 3, height = 2, command = self.clicked_arcsin)
        self.button_asin.place(x = 200, y = 165)
        self.button_acos = Button(self.master, text = "acos", width = 3, height = 2, command = self.clicked_arccos)
        self.button_acos.place(x = 230, y = 165)
        self.button_atg = Button(self.master, text = "atg", width = 3, height = 2, command = self.clicked_arctg)
        self.button_atg.place(x = 260, y = 165)
        self.button_actg = Button(self.master, text = "actg", width = 3, height = 2, command = self.clicked_arcctg)
        self.button_actg.place(x = 290, y = 165)
        self.button_arctg = Button(self.master, text = "atg", width = 3, height = 2, command = self.clicked_arctg)
        self.button_arctg.place(x = 320, y = 165)
        self.button_arcctg = Button(self.master, text = "actg", width = 3, height = 2, command = self.clicked_arcctg)
        self.button_arcctg.place(x = 350, y = 165)
        self.button_log2 = Button(self.master, text = "log2", width = 4, height = 2, command = self.clicked_log2)
        self.button_log2.place(x = 200, y = 200)
        self.button_log10 = Button(self.master, text = "log10", width = 4, height = 2, command = self.clicked_log10)
        self.button_log10.place(x = 240, y = 200)
        self.button_loge = Button(self.master, text = "loge", width = 4, height = 2, command = self.clicked_loge)
        self.button_loge.place(x = 280, y = 200)
        self.button_exp = Button(self.master, text = "exp", width = 3, height = 2, command = self.clicked_exponent)
        self.button_exp.place(x = 320, y = 200)
        self.button_sqrt = Button(self.master, text = "√", width = 3, height = 2, command = self.clicked_sqrt)
        self.button_sqrt.place(x = 350, y = 200)
        self.entry = Entry(self.master)
        self.entry.place(x = 200, y = 0)
        self.master.mainloop()


    def clicked_del(self):
        self.entry.delete(len(self.entry.get()) - 1)

    def clicked_log2(self):
        self.entry.insert(END, "log2(")

    def clicked_log10(self):
        self.entry.insert(END, "log10(")

    def clicked_loge(self):
        self.entry.insert(END, "loge(")

    def clicked_exponent(self):
        self.entry.insert(END, "exp(")

    def clicked_sqrt(self):
        self.entry.insert(END, "sqrt(")
        
    def clicked_tg(self):
        self.entry.insert(END, "tg(")

    def clicked_ctg(self):
        self.entry.insert(END, "ctg(")

    def clicked_arctg(self):
        self.entry.insert(END, "arctg(")

    def clicked_arcctg(self):
        self.entry.insert(END, "arcctg(")

    def clicked_arcsin(self):
        self.entry.insert(END, "arcsin(")

    def clicked_arccos(self):
        self.entry.insert(END, "arccos(")

    def clicked_sin(self):
        self.entry.insert(END, "sin(")

    def clicked_cos(self):
        self.entry.insert(END, "cos(")

    def clicked_parenthesis(self):
        self.entry.insert(END, "(")

    def clicked_parenthesis0(self):
        self.entry.insert(END, ")")

    def clicked_exp(self):
        self.entry.insert(END, "^")

    def clicked_dot(self):
        self.entry.insert(END, ".")

    def clicked_multiply(self):
        self.entry.insert(END, "*")

    def clicked_div(self):
        self.entry.insert(END, "/")

    def clicked_minus(self):
        self.entry.insert(END, "-")

    def clicked_plus(self):
        self.entry.insert(END, "+")

    def clicked_button1(self):
        self.entry.insert(END, "1")

    def clicked_button2(self):
        self.entry.insert(END, "2")

    def clicked_button3(self):
        self.entry.insert(END, "3")

    def clicked_button4(self):
        self.entry.insert(END, "4")

    def clicked_button5(self):
        self.entry.insert(END, "5")

    def clicked_button6(self):
        self.entry.insert(END, "6")

    def clicked_button7(self):
        self.entry.insert(END, "7")

    def clicked_button8(self):
        self.entry.insert(END, "8")

    def clicked_button9(self):
        self.entry.insert(END, "9")

    def clicked_button0(self):
        self.entry.insert(END, "0")

    def clicked(self):
        fr = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(self.calc(fr)))

        
    def digit(self):
        if self.formula[self.ind].isdigit():
            return 1
        elif self.formula[self.ind] == "-" and (self.ind == 0 or self.formula[self.ind - 1] == "("):
            return 1
        return 0

    
    def str_to_number(self):
        res = ""
        if self.formula[self.ind] == "-":
            self.ind += 1
            res += "-"
        while self.formula[self.ind] != "$" and (self.formula[self.ind].isdigit() or self.formula[self.ind] == "."):
            res += self.formula[self.ind]
            self.ind += 1
        return float(res)


    def variable_value(self):
        name = ""
        while self.formula[self.ind].isdigit() or self.formula[self.ind].isalpha():
            name += self.formula[self.ind]
            self.ind += 1
        return self.variables[name]
    

    def func(self):
        name = ""
        while self.get_lexem() != Sign.op:
            name += self.formula[self.ind]
            self.ind += 1
        if name == "sin":
            res = self.element()
            return math.sin(math.radians(res))
        elif name == "cos":
            res = self.element()
            return math.cos(math.radians(res))
        elif name == "tg":
            res = self.element()
            return math.tan(math.radians(res))
        elif name == "ctg":
            res = self.element()
            return 1 / math.tan(math.radians(res))
        elif name == "arcsin":
            res = self.element()
            return math.degrees(math.asin(res))
        elif name == "arccos":
            res = self.element()
            return math.degrees(math.acos(res))
        elif name == "arctg":
            res = self.element()
            return math.degrees(math.atan(res))
        elif name == "arcctg":
            res = self.element()
            if res == 0:
                return 90
            return math.degrees(math.atan(1 / res))
        elif name == "log2":
            res = self.element()
            return math.log2(res)
        elif name == "log10":
            res = self.element()
            return math.log10(res)
        elif name == "loge":
            res = self.element()
            return math.log1p(res - 1)
        elif name == "exp":
            res = self.element()
            return math.exp(res)
        elif name == "sqrt":
            res = self.element()
            return math.sqrt(res)

    
    def get_lexem(self):
        if self.ind == "$":
            return Sign.last
        if self.formula[self.ind] == "+":
            return Sign.plus
        elif self.formula[self.ind] == "-" and not self.digit():
            return Sign.minus
        elif self.formula[self.ind] == "(":
            return Sign.op
        elif self.formula[self.ind] == ")":
            return Sign.cl
        elif self.formula[self.ind] == "*":
            return Sign.mul
        elif self.formula[self.ind] == "/":
            return Sign.div
        elif self.formula[self.ind] == "^":
            return Sign.pw
        elif self.formula[self.ind] == "x" or self.formula[self.ind] == "y":
            return Sign.variable
        elif self.formula[self.ind].isalpha():
            return Sign.function
        else:
            return Sign.number

    
    def element(self):
        if self.get_lexem() == Sign.op:
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return res
        elif self.get_lexem() == Sign.variable:
            return self.variable_value()
        elif (self.get_lexem() == Sign.number) or (self.get_lexem() == Sign.minus):
            return self.str_to_number()
        else:
            return self.func()

        
    def exponentiation(self):
        res = self.element()
        while self.get_lexem() == Sign.pw:
            self.ind += 1
            res **= self.element()
        return res
    

    def multiplication(self):
        res = self.exponentiation()
        while self.get_lexem() == Sign.mul or self.get_lexem() == Sign.div:
            if self.get_lexem() == Sign.mul:
                self.ind += 1
                res *= self.exponentiation()
            else:
                self.ind += 1
                res /= self.exponentiation()
        return res


    def addition(self):
        res = self.multiplication()
        while self.get_lexem() == Sign.plus or self.get_lexem() == Sign.minus:
            if self.get_lexem() == Sign.plus:
                self.ind += 1
                res += self.multiplication()
            else:
                self.ind += 1
                res -= self.multiplication()
        return res


    def calc(self, fr):
        self.formula = fr
        self.formula += "$"
        self.ind = 0
        d = dict()
        self.variables = d
        self.formula = fr
        self.formula += "$"
        self.ind = 0
        return self.addition()



clcltr = Calculator()
