def space(string, app, typ=" "):
    while app > 0:
        string = typ + string
        app -= 1
    return string


def arithmetic_arranger(data, answer=False):
    line1 = ""  # first operands
    line2 = ""  # second operands
    line3 = ""  # ----
    line4 = ""  # answers
    free = "    "
    x = 0
    ret = list()

    if not len(data) <= 5:
        return "Error: Too many problems."

    for i in data:
        operand1, operator, operand2 = i.split()

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        try:
            operand1, operand2 = int(operand1), int(operand2)
        except:
            return "Error: Numbers must only contain digits."

        if operand1 > 9999 or operand2 > 9999:
            return "Error: Numbers cannot be more than four digits."

        ret.append([operand1, operator, operand2])


    retl = len(ret)
    for i in range(retl):

        if len(str(ret[i][0])) > len(str(ret[i][2])):
            length = len(str(ret[i][0])) + 2
        elif len(str(ret[i][0])) < len(str(ret[i][2])):
            length = len(str(ret[i][2])) + 2
        else:
            length = len(str(ret[i][2])) + 2

        if ret[i][1] == "+":
            x = ret[i][0] + ret[i][2]
        elif ret[i][1] == "-":
            x = ret[i][0] - ret[i][2]

        x = str(x)

        line4 = line4 + space(x, length - len(x))
        line3 = line3 + space("", length, "-")
        line2 = line2 + ret[i][1] + space(str(ret[i][2]), length - len(str(ret[i][2])) - 1)
        line1 = line1 + space(str(ret[i][0]), length - len(str(ret[i][0])))

        if i < len(ret) - 1:
            line1 = line1 + free
            line2 = line2 + free
            line3 = line3 + free
            line4 = line4 + free

    if answer:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        return line1 + "\n" + line2 + "\n" + line3