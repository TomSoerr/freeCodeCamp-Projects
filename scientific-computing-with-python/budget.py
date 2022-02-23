class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def center_name(self, name):
        ret = str()
        stars_total = 30 - len(name)
        right = stars_total % 2
        stars_total = stars_total - right
        temp = stars_total / 2
        right = right + int(temp)
        left = int(temp)
        for x in range(left):
            ret = ret + "*"
        ret = ret + name
        for x in range(right):
            ret = ret + "*"

        if len(ret) == 30:
            return ret + "\n"
        else:
            return "ERROR"

    def center(self, amount, description):
        if len(description) > 23:
            description = description[:23]
        elif len(description) == 23:
            pass
        elif len(description) < 23:
            temp1 = 23 - len(description)
            for x in range(temp1):
                description = description + " "

        amount = str(amount)
        if len(amount) > 7:
            amount = amount[:7]
        elif len(amount) == 7:
            pass
        elif len(amount) < 7:
            temp2 = 7 - len(amount)
            for x in range(temp2):
                amount = " " + amount

        return description + amount + "\n"

    def make_zeros(self, number):
        if number % 1 == 0:
            return str(int(number)) + ".00"
        else:
            return str(number)

    def __str__(self):
        total = "Total: " + self.make_zeros(self.get_balance())
        ret = self.center_name(self.name)
        for x in self.ledger:
            ret = ret + self.center(self.make_zeros(x["amount"]), x["description"])
        return ret + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for x in self.ledger:
            total = total + x["amount"]
        return total

    def transfer(self, amount, des_bud):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + des_bud.name)
            des_bud.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(some_input):
    categorys = list()
    for item in some_input:
        withdraw = 0
        for x in item.ledger:
            if x["amount"] < 0:
                withdraw = withdraw + x["amount"]
        categorys.append([item.name, withdraw])

    output = [
        "Percentage spent by category",
        "100| ",
        " 90| ",
        " 80| ",
        " 70| ",
        " 60| ",
        " 50| ",
        " 40| ",
        " 30| ",
        " 20| ",
        " 10| ",
        "  0| ",
        "    -",
    ]

    total = 0
    for x in categorys:
        total = total + x[1]
    for x in categorys:
        x[1] = int((x[1] / total) * 10)

    longest = ""
    for item in categorys:
        if len(item[0]) > len(longest):
            longest = item[0]
    longest = len(longest)
    for x in range(longest):
        output.append("     ")

    length = len(output)
    for item in categorys:
        while len(item[0]) < longest:
            item[0] = str(item[0]) + " "

        for x in range(11, 0, -1):
            if item[1] >= (x - 11) * -1:
                output[x] = output[x] + "o"
            else:
                output[x] = output[x] + " "
        output[12] = output[12] + "-"

        y = 0
        for x in range(13, 13 + longest):
            output[x] = output[x] + item[0][y]
            y += 1

        for x in range(length):
            if x == 0:
                continue
            elif x == 12:
                output[12] = output[12] + "--"
            else:
                output[x] = output[x] + "  "

    ret = str()
    for x in output:
        if x == output[-1]:
            ret = ret + x
        else:
            ret = ret + x + "\n"
    return ret