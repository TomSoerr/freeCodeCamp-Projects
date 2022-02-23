import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            self.add(key, value)

    def draw(self, balls):
        ret = list()
        if balls >= len(self.contents):
            ret = self.contents
        else:
            for x in range(balls):
                ret.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return ret

    def add(self, key, value):
        for x in range(value):
            self.contents.append(key)


def test_exp(expected, real):
    ret = None
    try:
        for x in expected:
            if real[x] >= expected[x]:
                if ret is None:
                    ret = True
                if ret:
                    ret = True

            else:
                ret = False
                break
    except KeyError:
        return False

    if ret is True:
        return True
    else:
        return False


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = num_experiments
    m = 0
    for x in range(num_experiments):
        real = dict()
        copy = hat.contents.copy()

        got_balls = list()
        if num_balls_drawn >= len(copy):
            got_balls = copy
        else:
            for balls in range(num_balls_drawn):
                got_balls.append(copy.pop(random.randint(0, len(copy) - 1)))

        for ball in got_balls:
            if ball not in real:
                real[ball] = 1
            else:
                real[ball] += 1
        if test_exp(expected_balls, real):
            m += 1

    return m / n
