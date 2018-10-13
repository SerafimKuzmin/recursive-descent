from enum import Enum


class Sign(Enum):
    minus = 1
    plus = 2
    mul = 3
    div = 4
    exp = 5
    last = 6
    op = 7
    cl = 8
    count = 9


def digit():
    global ind
    if formula[ind].isdigit():
        return 1
    elif formula[ind] == "-" and (ind == 0 or formula[ind - 1] == "("):
        return 1
    return 0


def cnt():
    global ind
    res = ""
    if formula[ind] == "-":
        ind += 1
        res += "-"
    while ind < len(formula) and (formula[ind].isdigit() or formula[ind] == "."):
        res += formula[ind]
        ind += 1
    return float(res)


def lex():
    global ind
    if ind >= len(formula):
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
        return Sign.exp
    else:
        return Sign.count



def bracket():
    global ind
    if lex() == Sign.op:
        ind += 1
        res = addition()
        ind += 1
        return res
    else:
        return cnt()

def exponentiation():
    global ind
    res = bracket()
    while lex() == Sign.exp:
        ind += 1
        res **= bracket()
    return res


def multiplication():
    global ind
    res = exponentiation()
    while lex() == Sign.mul or lex() == Sign.div:
        if lex() == Sign.mul:
            ind += 1
            res *= multiplication()
        else:
            ind += 1
            res /= multiplication()
    return res
    

def addition():
    global ind
    res = multiplication()
    while lex() == Sign.plus or lex() == Sign.minus:
        if lex() == Sign.plus:
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
    return addition()


fr = input()
print(calc(fr))
