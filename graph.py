from enum import Enum


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


class Calculator:
    def __init__(self):
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
        else:
            return Sign.number

    
    def element(self):
        if self.get_lexem() == Sign.op:
            self.ind += 1
            res = self.addition()
            self.ind += 1
            return res
        else:
            return self.str_to_number()

        
    def exponentiation(self):
        res = self.element()
        while self.get_lexem() == Sign.pw:
            self.ind += 1
            res **= self.exponentiation()
        return res
    

    def multiplication(self):
        res = self.exponentiation()
        while self.get_lexem() == Sign.mul or self.get_lexem() == Sign.div:
            if self.get_lexem() == Sign.mul:
                self.ind += 1
                res *= self.multiplication()
            else:
                self.ind += 1
                res /= self.multiplication()
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
        return self.addition()


fr = input()
clcltr = Calculator()
print(clcltr.calc(fr))
