"""
calculator -- written by newman
V0.1
- support +-*/
- support brackets
- the number in expression must be integer

V0.2 in planning
- support decimal
- support function
  - power function a^b
  - logarithmic function  base L x
  - sqrt function a S b 对a开b次根号
- context与操作符的概念让新的计算的扩展变得非常容易，半个小时的时间即支持了三种计算
- 当然，如果出现更复杂的函数模式，比如f(a,b,c)，就需要考虑新的解析和计算方式
"""


class Element:
    def __init__(self, index, value):
        self.index = index
        self.value = value


class Context:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def cal_expr(expr):
    return cal_expr_list(trans1(expr))


def trans(expr):
    expr_list = []
    for index in range(len(expr)):
        expr_list.append(Element(index, expr[index]))
    return expr_list


def trans1(expr):
    expr_list = []
    i = 0
    temp = ""
    while i < len(expr):
        if not is_number(expr[i]) and expr[i] != '.':
            if temp != "":
                expr_list.append(Element(len(expr_list), temp))
                temp = ""
            expr_list.append(Element(len(expr_list), expr[i]))
        else:
            temp += expr[i]
        i = i + 1
    if temp != "":
        expr_list.append(Element(len(expr_list), temp))
    return expr_list


def cal_expr_list(expr_list):
    if len(expr_list) == 1:
        return float(expr_list[0].value)
    for index in range(len(expr_list)):
        e = expr_list[index]
        context = get_context(e, expr_list)
        if is_op(e) and can_cal(e, context) and (is_prior(e, expr_list) or is_last_op(e, expr_list)):
            v = cal(e, context)
            new_expr_list = expr_list[0: e.index - 1] + [Element(-1, str(v))] + expr_list[e.index + 2:]
            new_expr_list = del_brackets(new_expr_list)
            update_list_index(new_expr_list)
            print_expr_list(new_expr_list)
            return cal_expr_list(new_expr_list)
    return "error"


def update_list_index(expr_list):
    for index in range(len(expr_list)):
        expr_list[index].index = index


def get_context(op, expr_list):
    return Context(expr_list[op.index - 1], expr_list[op.index + 1])


def is_op(e):
    if e.value == '+' or e.value == '-' or e.value == '*' or e.value == '/' or e.value == '^' or e.value == 'L' or e.value == 'S':
        return True
    return False


def can_cal(e, context):
    if is_number(context.left.value) and is_number(context.right.value):
        return True
    return False


def is_prior(op, expr_list):
    if op.value == '*' or op.value == '/':
        return True
    if op.index - 2 >= 0 and op.index + 2 < len(expr_list) and expr_list[op.index - 2].value == '(' and expr_list[op.index + 2].value == ')':
        return True
    return False


def is_last_op(e, expr_list):
    for index in range(e.index + 1, len(expr_list)):
        if is_op(expr_list[index]):
            return False
    return True


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


def cal(op, context):
    import math
    a = float(context.left.value)
    b = float(context.right.value)
    if op.value == '+':
        return a + b
    if op.value == '-':
        return a - b
    if op.value == '*':
        return a * b
    if op.value == '/':
        return float(a / b)
    if op.value == '^':
        return a**b
    if op.value == 'L':
        return math.log(b, a)
    if op.value == 'S':
        return math.pow(a, 1/b)


def del_brackets(expr_list):
    for index in range(len(expr_list)):
        if index > 0 and expr_list[index - 1].value == '(' and expr_list[index + 1].value == ')':
            return del_brackets(expr_list[0: index - 1] + [expr_list[index]] + expr_list[index + 2:])
    return expr_list


def print_expr_list(expr_list):
    str = ""
    for index in range(len(expr_list)):
        str = str + expr_list[index].value
    print(str)

"""
=====================================================================================
test code
=====================================================================================
"""
print("------------------------------------------")
assert(cal_expr("1+2*3+2") == 9.0)
print("------------------------------------------")
assert(cal_expr("1+2*3/2+4*5+4-6") == 22.0)
print("------------------------------------------")
assert(cal_expr("1+2*3/(2+4)*5+4-6") == 4.0)
print("------------------------------------------")
assert(cal_expr("((1+2))*3/((2+4))*5+4-6") == 5.5)
print("------------------------------------------")
assert(cal_expr("((1+2))*3/((1+0.5))*5+4-6") == 28.0)
print("------------------------------------------")
assert(cal_expr("((1+2))*3/((1+0.5))*5+2^5") == 62.0)
print("------------------------------------------")
assert(cal_expr("((1+2))*3/((1+0.5))*5+2L32") == 35.0)
print("------------------------------------------")
assert(cal_expr("((1+2))*3/((1+0.5))*5+4S2") == 32.0)
