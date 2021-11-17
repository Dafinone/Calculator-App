from flask import Flask, render_template
import arithmetic
import numberdoc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    del arithmetic.completeList[:]
    del arithmetic.t[:]
    message = 0
    return render_template('calc.html', message=message)


@app.route('/eq', methods=['GET'])
def main_calculator():
    if len(arithmetic.completeList) >= 2 and type(arithmetic.completeList[0]) == str:
        t = ""
        for elem in arithmetic.completeList:
            t += str(elem)
        y = [a for a in t]
        if '+' in y:
            arithmetic.Combination.main_calc_checker('+', y)
            x = arithmetic.Combination.equal_to('+')
        elif '-' in y:
            arithmetic.Combination.main_calc_checker('-', y)
            x = arithmetic.Combination.equal_to('-')
        elif '/' in y:
            arithmetic.Combination.main_calc_checker('/', y)
            x = arithmetic.Combination.equal_to('/')
        elif '*' in y:
            arithmetic.Combination.main_calc_checker('*', y)
            x = arithmetic.Combination.equal_to('*')
        else:
            x = 0
        message = x
        return render_template('calc.html', message=message)
    if '+' in arithmetic.completeList:
        x = arithmetic.Combination.equal_to('+')
    elif '-' in arithmetic.completeList:
        x = arithmetic.Combination.equal_to('-')
    elif '/' in arithmetic.completeList:
        x = arithmetic.Combination.equal_to('/')
    elif '*' in arithmetic.completeList:
        x = arithmetic.Combination.equal_to('*')
    else:
        x = 0

    message = x
    return render_template('calc.html', message=message)


@app.route('/one', methods=['GET'])
def calc_one():
    one_value = numberdoc.Numerics.one()
    message = one_value
    return render_template('calc.html', message=message)


@app.route('/two', methods=['GET'])
def calc_two():
    two_value = numberdoc.Numerics.two()
    message = two_value
    return render_template('calc.html', message=message)


@app.route('/three', methods=['GET'])
def calc_three():
    three_value = numberdoc.Numerics.three()
    message = three_value
    return render_template('calc.html', message=message)


@app.route('/four', methods=['GET'])
def calc_four():
    four_value = numberdoc.Numerics.four()
    message = four_value
    return render_template('calc.html', message=message)


@app.route('/five', methods=['GET'])
def calc_five():
    five_value = numberdoc.Numerics.five()
    message = five_value
    return render_template('calc.html', message=message)


@app.route('/six', methods=['GET'])
def calc_six():
    six_value = numberdoc.Numerics.six()
    message = six_value
    return render_template('calc.html', message=message)


@app.route('/seven', methods=['GET'])
def calc_seven():
    seven_value = numberdoc.Numerics.seven()
    message = seven_value
    return render_template('calc.html', message=message)


@app.route('/eight', methods=['GET'])
def calc_eight():
    eight_value = numberdoc.Numerics.eight()
    message = eight_value
    return render_template('calc.html', message=message)


@app.route('/nine', methods=['GET'])
def calc_nine():
    nine_value = numberdoc.Numerics.nine()
    message = nine_value
    return render_template('calc.html', message=message)


@app.route('/zero', methods=['GET'])
def calc_zero():
    zero_value = numberdoc.Numerics.zero()
    message = zero_value
    return render_template('calc.html', message=message)


@app.route('/percent', methods=['GET'])
def calc_percent():
    if arithmetic.completeList == []:
        message = 0
        return render_template('calc.html', message=message)
    else:
        percent_value = arithmetic.completeList[-1]
        percent = arithmetic.Combination.percentage(percent_value)
        del arithmetic.completeList[:]
        arithmetic.completeList.append(percent)
        return render_template('calc.html', message=percent)


@app.route('/over_x', methods=['GET'])
def calc_over_x():
    s = ""
    for elem in arithmetic.completeList:
        s += str(elem)
    over_x_value = s
    if over_x_value == '':
        message = 0
        return render_template('calc.html', message=message)
    over_x = arithmetic.Combination.over_x(float(over_x_value))
    if over_x == "Cannot divide by 0":
        message = over_x
    else:
        message = round(over_x, 2)
    return render_template('calc.html', message=message)


@app.route('/sq_x', methods=['GET'])
def square_x():
    s = ""
    for elem in arithmetic.completeList:
        s += str(elem)
    squared = s
    if squared == '':
        message = 0
        return render_template('calc.html', message=message)
    sq = arithmetic.Combination.square_x(float(squared))
    return render_template('calc.html', message=sq)


@app.route('/sqrt', methods=['GET'])
def sqrt_x():
    s = ""
    for elem in arithmetic.completeList:
        s += str(elem)
    sqrt_x = s
    if sqrt_x == '':
        message = 0
        return render_template('calc.html', message=message)
    sqrt = arithmetic.Combination.square_root_x(float(sqrt_x))
    return render_template('calc.html', message=sqrt)


@app.route('/plusminus', methods=['GET'])
def plusminus():
    s = ""
    for elem in arithmetic.completeList:
        s += str(elem)
    p = s
    if p == '':
        message = 0
        return render_template('calc.html', message=message)
    x = arithmetic.Combination.plus_minus(float(p))
    return render_template('calc.html', message=x)


@app.route('/dot', methods=['GET'])
def dots():
    s = ""
    for elem in arithmetic.completeList:
        s += str(elem)
    d = s
    if d == '':
        numberdoc.Numerics.zero()
        message = arithmetic.Combination.dot()
        return render_template('calc.html', message=message)
    if arithmetic.completeList[-1] in ('+', "-", "/", "*"):
        numberdoc.Numerics.zero()
        message = arithmetic.Combination.dot()
        return render_template('calc.html', message=message)
    x = arithmetic.Combination.dot()
    return render_template('calc.html', message=x)


@app.route('/add', methods=['GET'])
def add_values():
    addition = arithmetic.Combination.add()
    return render_template('calc.html', message=addition)


@app.route('/subt', methods=['GET'])
def sub_values():
    subtraction = arithmetic.Combination.subt()
    return render_template('calc.html', message=subtraction)


@app.route('/mult', methods=['GET'])
def mult_values():
    multiplier = arithmetic.Combination.mult()
    return render_template('calc.html', message=multiplier)


@app.route('/div', methods=['GET'])
def div_values():
    division = arithmetic.Combination.div()
    return render_template('calc.html', message=division)


@app.route('/cls', methods=['GET'])
def cls_screen():
    clear = 0
    del arithmetic.completeList[:]
    return render_template('calc.html', message=clear)


@app.route('/cancel', methods=['GET'])
def cancel_value():
    if arithmetic.completeList == []:
        cancel = 0
        return render_template('calc.html', message=cancel)
    else:
        arithmetic.completeList.pop()
    s = ""
    for elem in arithmetic.completeList:
        s += str(elem)
    if s == "":
        cancel = 0
    else:
        cancel = s
    return render_template('calc.html', message=cancel)


###############################################################
#                                                             #
#                   DATA SCIENCE CALCULATOR                   #
#                                                             #
###############################################################


@app.route('/ds', methods=['GET'])
def ds_home():
    del arithmetic.completeList[:]
    del arithmetic.t[:]
    message = 0
    return render_template('data_science.html', message=message)


@app.route('/show', methods=['GET'])
def ds_show():
    curr = arithmetic.Combination.ds_show_calc()
    if curr == [] or "" in curr:
        del arithmetic.t[:]
        message = 0
        return render_template('data_science.html', message=message)
    s = ""
    if len(curr) == 1:
        s = str(curr[-1])
        return render_template('data_science.html', message=s)
    else:
        for elem in range(len(curr)-1):
            s += str(curr[elem]) + ", "
        s = s + str(curr[-1])
        if len(curr) > 15:
            curr.pop()
            err = "You can only use 15 samples!"
            return render_template('data_science.html', err_msg=err)
        return render_template('data_science.html', message=s)


@app.route('/mean', methods=['GET'])
def ds_mean():
    s = arithmetic.t
    if s == []:
        message = 0
        return render_template('data_science.html', message=message)
    c = arithmetic.Combination.mean_func()
    message = "Mean: " + str(c)
    return render_template('data_science.html', message=message)


@app.route('/median', methods=['GET'])
def ds_median():
    p = arithmetic.t
    if p == []:
        message = 0
        return render_template('data_science.html', message=message)
    c = arithmetic.Combination.median_func()
    message = "Median: " + str(c)
    return render_template('data_science.html', message=message)


@app.route('/mode', methods=['GET'])
def ds_mode():
    p = arithmetic.t
    if p == []:
        message = 0
        return render_template('data_science.html', message=message)
    c = arithmetic.Combination.mode_func()
    message = "Mode: " + str(c)
    return render_template('data_science.html', message=message)


@app.route('/skew', methods=['GET'])
def ds_skew():
    if arithmetic.t == []:
        message = 0
        return render_template('data_science.html', message=message)
    mean_value = arithmetic.Combination.mean_func()
    median_value = arithmetic.Combination.median_func()
    mode_value = arithmetic.Combination.mode_func()
    if mode_value == "No Mode!":
        message = "No Skew!"
        return render_template('data_science.html', message=message)
    if mean_value > median_value or mean_value > mode_value:
        skew_value = "Positive or Right Skew!"
    elif mean_value < median_value or mean_value < mode_value:
        skew_value = "Negative or Left Skew!"
    elif mean_value == median_value == mode_value:
        skew_value = "Zero Skew!"
    message = "Skewness: " + skew_value
    return render_template('data_science.html', message=message)


@app.route('/var', methods=['GET'])
def ds_var():
    if arithmetic.t == []:
        message = 0
        return render_template('data_science.html', message=message)
    mean_variance = arithmetic.Combination.var_func()
    message = "Sample Variance: " + str(mean_variance)
    return render_template('data_science.html', message=message)


@app.route('/std', methods=['GET'])
def ds_std():
    if arithmetic.t == []:
        message = 0
        return render_template('data_science.html', message=message)
    std_value = arithmetic.Combination.std_func()
    message = "Standard Deviation: " + str(std_value)
    return render_template('data_science.html', message=message)


@app.route('/cov', methods=['GET'])
def ds_cov():
    if arithmetic.t == []:
        message = 0
        return render_template('data_science.html', message=message)
    cov_value = arithmetic.Combination.cov_func()
    message = "Coefficient of STD.: " + str(cov_value)
    return render_template('data_science.html', message=message)


@app.route('/stderr', methods=['GET'])
def ds_stderr():
    if arithmetic.t == []:
        message = 0
        return render_template('data_science.html', message=message)
    stderr_value = arithmetic.Combination.stderr_func()
    message = "Standard Error: " + str(stderr_value)
    return render_template('data_science.html', message=message)


@app.route('/prob', methods=['GET'])
def ds_prob():
    prob = arithmetic.d
    if arithmetic.t == []:
        message = 0
        return render_template('data_science.html', message=message)
    if prob == []:
        prob.append(0)
        err_msg = "Enter no. to get Prob. & punch the \"Prob. Key\": "
        return render_template('data_science.html', err_msg=err_msg)
    try:
        num = arithmetic.completeList[-1]
    except:
        message = "Float not allowed!"
        return render_template('data_science.html', err_msg=message)
    prob_value = arithmetic.Combination.prob_func(num)
    del prob[:]
    message = "Probability: " + str(prob_value)
    return render_template('data_science.html', message=message)


@app.route('/one_ds', methods=['GET'])
def ds_one():
    one_value = numberdoc.Numerics.one()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(one_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = one_value
            return render_template('data_science.html', message=message)
    message = one_value
    return render_template('data_science.html', message=message)


@app.route('/two_ds', methods=['GET'])
def ds_two():
    two_value = numberdoc.Numerics.two()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(two_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = two_value
            return render_template('data_science.html', message=message)
    message = two_value
    return render_template('data_science.html', message=message)


@app.route('/three_ds', methods=['GET'])
def ds_three():
    three_value = numberdoc.Numerics.three()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(three_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = three_value
            return render_template('data_science.html', message=message)
    message = three_value
    return render_template('data_science.html', message=message)


@app.route('/four_ds', methods=['GET'])
def ds_four():
    four_value = numberdoc.Numerics.four()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(four_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = four_value
            return render_template('data_science.html', message=message)
    message = four_value
    return render_template('data_science.html', message=message)


@app.route('/five_ds', methods=['GET'])
def ds_five():
    five_value = numberdoc.Numerics.five()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(five_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = five_value
            return render_template('data_science.html', message=message)
    message = five_value
    return render_template('data_science.html', message=message)


@app.route('/six_ds', methods=['GET'])
def ds_six():
    six_value = numberdoc.Numerics.six()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(six_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = six_value
            return render_template('data_science.html', message=message)
    message = six_value
    return render_template('data_science.html', message=message)


@app.route('/seven_ds', methods=['GET'])
def ds_seven():
    seven_value = numberdoc.Numerics.seven()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(seven_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = seven_value
            return render_template('data_science.html', message=message)
    message = seven_value
    return render_template('data_science.html', message=message)


@app.route('/eight_ds', methods=['GET'])
def ds_eight():
    eight_value = numberdoc.Numerics.eight()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(eight_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = eight_value
            return render_template('data_science.html', message=message)
    message = eight_value
    return render_template('data_science.html', message=message)


@app.route('/nine_ds', methods=['GET'])
def ds_nine():
    nine_value = numberdoc.Numerics.nine()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(nine_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = nine_value
            return render_template('data_science.html', message=message)
    message = nine_value
    return render_template('data_science.html', message=message)


@app.route('/zero_ds', methods=['GET'])
def ds_zero():
    zero_value = numberdoc.Numerics.zero()
    if arithmetic.t != []:
        x = arithmetic.Combination.numbers_func(zero_value)
        if x == "1":
            s = arithmetic.t[-1]
            return render_template('data_science.html', message=s)
        else:
            message = zero_value
            return render_template('data_science.html', message=message)
    message = zero_value
    return render_template('data_science.html', message=message)


@app.route('/dot_ds', methods=['GET'])
def ds_dots():
    d = arithmetic.t
    a = arithmetic.completeList
    if d == [] and a == []:
        numberdoc.Numerics.zero()
        a = arithmetic.completeList
        arithmetic.t = a.copy()
        del arithmetic.completeList[:]
        message = arithmetic.Combination.ds_dot()
        return render_template('data_science.html', message=message)
    elif a == []:
        numberdoc.Numerics.zero()
        a = arithmetic.completeList
        arithmetic.t.append(str(a[-1]))
        del arithmetic.completeList[:]
        message = arithmetic.Combination.ds_dot()
        return render_template('data_science.html', message=message)
    s = ""
    for elem in a:
        s += str(elem)
    arithmetic.t.append(s)
    del arithmetic.completeList[:]
    x = arithmetic.Combination.ds_dot()
    return render_template('data_science.html', message=x)


@app.route('/cls_ds', methods=['GET'])
def ds_cls_screen():
    clear = 0
    del arithmetic.t[:]
    del arithmetic.completeList[:]
    # check here for irregularities
    del arithmetic.d[:]
    return render_template('data_science.html', message=clear)


@app.route('/cancel_ds', methods=['GET'])
def ds_cancel_value():
    if arithmetic.t == []:
        arithmetic.completeList.pop()
        cancel = 0
        return render_template('data_science.html', message=cancel)
    else:
        arithmetic.t.pop()
    s = ""
    if arithmetic.t[:] == []:
        cancel = 0
    else:
        for elem in range(len(arithmetic.t)-1):
            s += str(arithmetic.t[elem]) + ", "
        s = s + str(arithmetic.t[-1])
        cancel = s
    return render_template('data_science.html', message=cancel)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
