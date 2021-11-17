import math
from collections import deque
from flask import Flask, render_template


class Arithmetics:

    def __init__(self):
        self.calc = 0

    def div(self):
        division = '/'
        completeList.append(division)
        return division

    def mult(self):
        multiplier = '*'
        completeList.append(multiplier)
        return multiplier

    def subt(self):
        subtraction = '-'
        completeList.append(subtraction)
        return subtraction

    def add(self):
        addition = '+'
        completeList.append(addition)
        return addition

    def over_x(self, x):
        self.x = x
        if self.x == 0:
            del completeList[:]
            completeList.append("Cannot divide by 0")
            overage = completeList[-1]
        else:
            overage = 1 / self.x
        del completeList[:]
        completeList.append(overage)
        return overage

    def square_x(self, x):
        self.x = x
        squared = self.x * self.x
        del completeList[:]
        completeList.append(squared)
        return squared

    def square_root_x(self, x):
        self.x = x
        square_root = math.sqrt(self.x)
        del completeList[:]
        completeList.append(int(square_root))
        return square_root

    def percentage(self, a):
        self.a = a
        percent = self.a / 100
        return percent

    def dot(self):
        global completeList
        global d
        if type(completeList[-1]) != int:
            for elem in completeList:
                completeList = [x for x in elem]
                if '+' in completeList or '-' in completeList or '/' in completeList or '*' in completeList:
                    completeList.append('.')
                    s = ""
                    for elem in completeList:
                        s += str(elem)
                    del completeList[:]
                    completeList.append(s)
                    final_dot_value = completeList[-1]
                    return final_dot_value
        else:
            s = ""
            for elem in completeList:
                s += str(elem)
            curr_val = s
            dot_value = str(curr_val) + '.'
            del completeList[:]
            completeList.append(dot_value)
            final_dot_value = completeList[-1]
            return final_dot_value

    def plus_minus(self, a):
        self.a = a
        checker = -(self.a)
        del completeList[:]
        completeList.append(float(checker))
        return checker

    def equal_to(self, signal):
        self.signal = signal
        counter = 0
        for elem in completeList:
            if elem == self.signal:
                a = counter
                break
            counter += 1
        y = ""
        for elem in completeList[:a]:
            y += str(elem)
        if y == '':
            s = 0
        else:
            s = float(y)
        y = ""
        for elem in completeList[a + 1:]:
            y += str(elem)
        ab = []
        cd = ""
        for elem in y:
            if elem not in ('+', '-', '/', '*'):
                cd += elem
            else:
                if elem == self.signal:
                    ab.append(cd)
                    cd = ""
        ab.append(cd)
        for elem in ab:
            if self.signal == '+':
                s += float(elem)
            elif self.signal == '-':
                s -= float(elem)
            elif self.signal == '/':
                if elem == "0":
                    del completeList[:]
                    completeList.append("Cannot divide by 0")
                    x = completeList[-1]
                    return x
                else:
                    s /= float(elem)
            else:
                s *= float(elem)
        del completeList[:]
        completeList.append(float(s))
        x = completeList[-1]
        return x

    def main_calc_checker(self, symbol, y):
        self.symbol = symbol
        self.y = y
        d = []
        s = ""
        counter = 0
        for e in self.y:
            if self.y[0] == self.symbol and counter == 0:
                s += str(e)
                counter += 1
            elif e not in ('+', '-', '/', '*'):
                s += str(e)
                counter += 1
            elif e == self.symbol and counter != 0:
                d.append(s)
                c = self.y[counter]
                d.append(str(c))
                s = ""
        d.append(s)
        del completeList[:]
        for elem in d:
            completeList.append(elem)

    def ds_show_calc(self):
        global t
        y = completeList.copy()
        del completeList[:]
        s = ""
        if y == []:
            mes = t
            return mes
        for elem in y:
            s += str(elem)
        t.append(s)
        mes = t
        return mes

    def ds_dot(self):
        global t
        global d
        if type(t[-1]) != int:
            if t[-1]:
                new_t = [x for x in t[-1]]
                new_new_t = new_t.copy()
                new_new_t.append('.')
                s = ""
                for elem in new_new_t:
                    s += str(elem)
                t.pop()
                t.append(s)
                final_dot_value = t[-1]
                return final_dot_value
        else:
            s = ""
            for elem in t:
                s += str(elem)
            curr_val = s
            dot_value = str(curr_val) + '.'
            del t[:]
            t.append(dot_value)
            final_dot_value = t[-1]
            return final_dot_value

    def numbers_func(self, num):
        self.num = num
        if t[-1]:
            counter = 0
            x = [a for a in t[-1]]
            new_x = x.copy()
            s = ""
            if '.' in new_x and new_x[-1] == '.':
                new_x.append(str(self.num))
                del completeList[:]
                for elem in new_x:
                    s += str(elem)
                t.pop()
                t.append(s)
                y = t[-1]
                return "1"
            else:
                return "2"

    def mean_func(self):
        s = t
        d = 0
        counter = 0
        for elem in s:
            if elem == ', ':
                continue
            d += float(elem)
            counter += 1
        x = d / counter
        mean_ds = round(x, 2)
        return mean_ds

    def median_func(self):
        p = t
        d = []
        s = []
        counter = 0
        for elem in p:
            if elem == ', ':
                continue
            d.append(float(elem))
            counter += 1
        s = sorted(d)
        if counter % 2 == 1:
            m = (counter + 1) / 2
            median_ds = s[int(m)-1]
        else:
            m = counter / 2
            n = m + 1
            x = (s[int(m) - 1] + s[int(n) - 1]) / 2
            median_ds = round(x, 2)
        return median_ds

    def mode_func(self):
        p = t
        d = []
        s = []
        for elem in p:
            if elem == ', ':
                continue
            d.append(float(elem))
        s = sorted(d)
        newCounter = 0
        for elem in range(len(s)):
            count = 0
            for a in s:
                if a == s[elem]:
                    count += 1
                if count > 1:
                    newCounter = s[elem]
        if newCounter == 0:
            mode_ds = "No Mode!"
        else:
            mode_ds = newCounter
        return mode_ds

    def var_func(self):
        mean_value = self.mean_func()
        s = t
        c = 0
        counter = 0
        for elem in t:
            if elem == ", ":
                continue
            c += ((float(elem) - mean_value) * (float(elem) - mean_value))
            counter += 1
        x = c / (counter - 1)
        mean_variance = round(x, 2)
        return mean_variance

    def std_func(self):
        var_value = self.var_func()
        x = math.sqrt(var_value)
        std_value = round(x, 2)
        return std_value

    def cov_func(self):
        std_value = self.std_func()
        mean_value = self.mean_func()
        x = std_value / mean_value
        cov_value = round(x, 2)
        return cov_value

    def stderr_func(self):
        std_value = self.std_func()
        counter = 0
        for elem in t:
            if elem == ", ":
                continue
            counter += 1
        sq_counter = math.sqrt(counter)
        x = std_value / sq_counter
        stderr_value = round(x, 2)
        return stderr_value

    def prob_func(self, num):
        self.num = num
        p = t
        d = []
        s = []
        for elem in p:
            if elem == ', ':
                continue
            d.append(float(elem))
        s = sorted(d)
        tot_count = len(s)
        count = 0
        for a in s:
            if a == self.num:
                count += 1
        if count == 0:
            prob_value = "Number not amongst List Entered!"
            return prob_value
        else:
            x = (count / tot_count)
            prob_value = round(x, 2)
            return prob_value


Combination = Arithmetics()
completeList = []
d = []
t = []
