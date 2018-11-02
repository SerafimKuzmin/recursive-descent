from enum import Enum
import math


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
    sin = 12
    cos = 13
    tg = 14
    ctg = 15
    log = 16


class Calculator:
    def __init__(self):
        self.variables = dict()
        self.formula = ""
        self.ind = 0

        
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
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.sin(math.radians(res))
        elif name == "cos":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.cos(math.radians(res))
        elif name == "tg":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.tan(math.radians(res))
        elif name == "ctg":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return 1 / math.tan(math.radians(res))
        elif name == "sec":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return 1 / math.sin(math.radians(res))
        elif name == "cosec":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return 1 / math.cos(math.radians(res))
        elif name == "arcsin":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.degrees(math.asin(res))
        elif name == "arccos":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.degrees(math.acos(res))
        elif name == "arctg":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.degrees(math.atan(res))
        elif name == "arcctg":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.degrees(math.atan(1 / res))
        elif name == "log2":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.log2(res)
        elif name == "log10":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.log10(res)
        elif name == "loge":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.log1p(res - 1)
        elif name == "exp":
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return math.exp(res)
        elif name == "sqrt":
            self.ind += 1
            res = self.addition()
            self.ind += 1
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
        elif self.formula[self.ind].isdigit():
            return Sign.number
        else:
            return Sign.function

    
    def element(self):
        if self.get_lexem() == Sign.op:
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return res
        elif self.get_lexem() == Sign.variable:
            return self.variable_value()
        elif self.get_lexem() == Sign.number:
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
        flag = 0
        self.formula = fr
        self.formula += "$"
        self.ind = 0
        for i in range(len(fr)):
            self.ind = i
            if self.get_lexem() == Sign.variable:
                flag = 1
        d = dict()
        if flag:
            n = int(input("How many variables?\n"))
            for i in range(n):
                name, f = input().split(" = ")
                d[name] = float(self.calc(f))
        self.variables = d
        self.formula = fr
        self.formula += "$"
        self.ind = 0
        return self.addition()


clcltr = Calculator()
while 1:
    fr = input()
    print(clcltr.calc(fr))
