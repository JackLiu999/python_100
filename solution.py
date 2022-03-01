import datetime
import string


def question1():
    list1 = [1, 2, 3, 4]
    ans = []
    for i in list1:
        for x in list1:
            for w in list1:
                # 应多加一行判断ixw不能是一样的
                ans.append(str(i) + str(x) + str(w))
    print(ans)


def question2(profit):
    # 看不明白题
    money = 0
    if profit < 100000:
        money = profit * 0.1
    if 100000 < profit < 200000:
        money = 100000 * 0.1 + profit - 100000 * 0.075
    if 200000 < profit < 400000:
        money = (profit - 200000) * 0.05
    if 400000 < profit < 600000:
        money = (profit - 400000) * 0.03
    if 600000 < profit < 1000000:
        money = (profit - 600000) * 0.015
    if 1000000 < profit:
        money = (profit - 1000000) * 0.01
    return money


def question3():
    ans = []
    for i in range(2000):
        for w in range(2000):
            for q in range(2000):
                if i + 100 == w * w and i + 100 + 168 == q * q:
                    ans.append(i)
    return ans


def question4(month, date, year):
    days = 0
    MonthDaysFor366 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MonthDaysFor365 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 闰年366天 2月29天
    if year % 4 == 0:
        list1 = MonthDaysFor366[0:month - 1]
        for i in list1:
            days += i
        days += date
        return days
    else:
        list1 = MonthDaysFor365[0:month - 1]
        print(list1)
        for i in list1:
            days += i
        days += date
        return days


def question5(x, y, z):
    list1 = [x, y, z]
    list1.sort()
    return list1


def question6(x):
    # 抄的 费数列
    if x == 1 or x == 2:
        return 1
    else:
        number = question6(x - 1) + question6(x - 2)
        return number


def question7(inputList):
    list2 = []
    for i in inputList:
        list2.append(i)
    return list2


def question8():
    list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in list1:
        for w in list1:
            print(i + '*' + w + '=' + str(int(i) * int(w)))


# 暂停一秒不会
def question9():
    return


# 暂停一秒不会
def question10():
    return


# 看不懂题
def question11():
    return


def question12():
    list1 = []
    for i in range(101, 200):
        count = 0
        for w in range(2, i - 1):
            for q in range(2, i - 1):
                if w * q == i:
                    count += 1
        if count == 0:
            list1.append(i)
    return list1


def question13():
    list1 = []
    for i in range(9):
        for w in range(9):
            for q in range(9):
                num = (i * i + w * w + q * q)
                if len(str(num)) == 3:
                    if num not in list1:
                        list1.append(num)
    return list1


def question14():
    # 不会
    return


def question15(score):
    if score >= 90:
        print('your grade is A')
    elif 89 > score > 60:
        print('your grade is B')
    else:
        print('your grade is C')


#  datetime
def question16():
    print(datetime.date.today())
    print(datetime.date.today().strftime('%d,%m,%y'))
    return


#  import string
def question17(x):
    intCount = 0
    charCount = 0
    spaceCount = 0
    elseCount = 0
    for i in x:
        if i.isalpha():
            charCount += 1
        elif i.isdigit():
            intCount += 1
        elif i.isspace():
            spaceCount += 1
        else:
            elseCount += 1
    print(intCount)
    print(charCount)
    print(spaceCount)
    print(elseCount)
    return


def question18(number, many):
    list1 = []
    for i in range(1, many+1):
        if i >= 1:
            str1 = str(number)
            str1 = str1*i
            list1.append(int(str1))
        else:
            list1.append(number)
    print(list1)
    return sum(list1)


if __name__ == '__main__':
    print(question18(4, 4))
