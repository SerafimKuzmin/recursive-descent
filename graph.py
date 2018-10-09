def f(ind):
    return lex(ind) != "plus" and lex(ind) != "minus" and lex(ind) != "last" and lex(ind) != "close"


def f1(ind):
    return lex(ind) != "plus" and lex(ind) != "minus" and lex(ind) != "last" and lex(ind) != "close" and lex(ind) != "umn" and lex(ind) != "div"


def f2(ind):
    return ind == len(formula) or formula[ind] == "+" or formula[ind] == "-" or formula[ind] == "(" or formula[ind] == ")" or formula[ind] == "*" or formula[ind] == "/" or formula[ind] == "^" 


def digit(ind):
    if formula[ind].isdigit():
        return 1
    elif formula[ind] == "-" and (ind == 0 or formula[ind - 1] == "("):
        return 1
    return 0


def cnt(ind):
    res = ""
    flg = 0
    if formula[ind] == "-":
        ind += 1
        res += "-"
    while not f2(ind):
        res += formula[ind]
        ind += 1
    return res


def lex(ind):
    if ind >= len(formula):
        return "last"
    if formula[ind] == "+":
        return "plus"
    elif formula[ind] == "-" and not digit(ind):
        return "minus"
    elif formula[ind] == "(":
        return "open"
    elif formula[ind] == ")":
        return "close"
    elif formula[ind] == "*":
        return "umn"
    elif formula[ind] == "/":
        return "div"
    elif formula[ind] == "^":
        return "step"
    else:
        return cnt(ind)


def bracket(ind):
    value = lex(ind)
    if value == "last":
        return "l"
    elif value == "open":
        r = ind
        bal = 1
        while bal != 0:
            r += 1
            if lex(r) == "open":
                bal += 1
            elif lex(r) == "close":
                bal -= 1
        return plus(ind + 1, r), r - ind + 1
    else:
        return float(value), len(value)


def st(ind):
    res = 0
    a = bracket(ind)
    res = a[0]
    ind += a[1]
    while f1(ind):
        if lex(ind) == "step":
            a = bracket(ind + 1)
            if a == "l":
                break
            res = res ** a[0]
            ind += a[1] + 1
    return res, ind


def pro(ind):
    res = 0
    a = st(ind)
    res = a[0]
    ind = a[1]
    while f(ind):
        if lex(ind) == "umn":
            a = st(ind + 1)
            res *= a[0]
            ind = a[1]
        elif lex(ind) == "div":
            a = st(ind + 1)
            res /= a[0]
            ind = a[1]
    return res, ind
    

def plus(l, r):
    res = 0
    a = pro(l)
    res += a[0]
    l = a[1]
    while l < r:
        if lex(l) == "plus":
            a = pro(l + 1)
            res += a[0]
            l = a[1]
        elif lex(l) == "minus":
            a = pro(l + 1)
            res -= a[0]
            l = a[1]
    return res


def calc(fr):
    global formula
    formula = fr
    return plus(0, len(formula))

fr = input()
print(calc(fr))
