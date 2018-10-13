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


def digit():
    global ind
    if formula[ind].isdigit():
        return 1
    elif formula[ind] == "-" and (ind == 0 or formula[ind - 1] == "("):
        return 1
    return 0


def str_to_number():
    global ind
    res = ""
    if formula[ind] == "-":
        ind += 1
        res += "-"
    while formula[ind] != "$" and (formula[ind].isdigit() or formula[ind] == "."):
        res += formula[ind]
        ind += 1
    return float(res)


def get_lexem():
    global ind
    if ind == "$":
        return Sign.last
    if formula[ind] == "+":
        return Sign.plus
    elif formula[ind] == "-" and not digit():
        return Sign.minus
    elif formula[ind] == "(":
        return Sign.op
    elif formula[ind] == ")":
        return Sign.cl
    elif formula[ind] == "*":
        return Sign.mul
    elif formula[ind] == "/":
        return Sign.div
    elif formula[ind] == "^":
        return Sign.pw
    else:
        return Sign.number



def element():
    global ind
    if get_lexem() == Sign.op:
        ind += 1
        res = addition()
        ind += 1
        return res
    else:
        return str_to_number()

def exponentiation():
    global ind
    res = element()
    while get_lexem() == Sign.pw:
        ind += 1
        res **= exponentiation()
    return res


def multiplication():
    global ind
    res = exponentiation()
    while get_lexem() == Sign.mul or get_lexem() == Sign.div:
        if get_lexem() == Sign.mul:
            ind += 1
            res *= multiplication()
        else:
            ind += 1
            res /= multiplication()
    return res
    

def addition():
    global ind
    res = multiplication()
    while get_lexem() == Sign.plus or get_lexem() == Sign.minus:
        if get_lexem() == Sign.plus:
            ind += 1
            res += multiplication()
        else:
            ind += 1
            res -= multiplication()
    return res


def calc(fr):
    global formula, ind 
    ind = 0
    formula = fr
    formula += "$"
    return addition()


fr = input()
print(calc(fr))
