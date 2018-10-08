

def lex(ind):
    if ind >= len(formula):
        return "last"
    if formula[ind] == "+":
        return "plus"
    elif formula[ind] == "-":
        return "minus"
    elif formula[ind] == "(":
        return "open"
    elif formula[ind] == ")":
        return "close"
    else:
        cnt = ""
        while ind < len(formula) and formula[ind].isdigit():
            cnt += formula[ind]
            ind += 1
        return cnt



def bracket(ind):
    value = lex(ind)
    if value == "last":
        return "l"
    elif value.isdigit():
        return int(value), len(value)
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



def plus(ind):
    res = 0
    a = bracket(ind)
    res += a[0]
    ind += a[1]
    while l < r:
        if lex(l) == "plus":
            a = bracket(l + 1)
            res += a[0]
            l += a[1] + 1
        elif lex(l) == "minus":
            a = bracket(l + 1)
            res -= a[0]
            l += a[1] + 1
    return res


def calc(formula):
    global formula
    return plus(0)


formula = input()
print(calc(0, len(formula)))
