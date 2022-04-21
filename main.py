import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from random import uniform


def create_table(step, table, equipment):
    x1 = 0
    x2 = 2
    x1_line =x1
    n = step
    mytable = table
    x_list_line = []
    y_list= []
    y_list_line = []
    x_list = []
    step2 = 1 * x2 / 1000
    step = (x2 - x1) / n
    Integral = 0
    for i in range(0, 1000):
        x_list_line.append(x1_line)
        y = math.pow(x1_line, 3) # function
        x1_line += step2
        y_list_line.append(y)
    for i in range(0, n + 1):
        x_list.append(x1)
        x1 += step
    if equipment == "left":
        for i in range(0, len(x_list)-1):
            arg = x_list[i]
            y = math.pow(arg, 3)  # function
            y_list.append(y)
            Integral += abs(y * step)
        x_list.pop(len(x_list) - 1)
    if equipment == "middle":
        for i in range(0, len(x_list)-1):
            arg = (x_list[i] + x_list[i+1])/2
            y = math.pow(arg, 3)  # function
            y_list.append(y)
            Integral += abs(y * step)
        x_list.pop(len(x_list)-1)

    if equipment == "random":
        for i in range(0, len(x_list)-1):
            arg = uniform(x_list[i], x_list[i+1])
            y = math.pow(arg, 3)  # function
            y_list.append(y)
            Integral += abs(y * step)
        x_list.pop(len(x_list)-1)
    if equipment == "right":
        for i in range(0, len(x_list)-1):
            arg = x_list[i+1]
            y = math.pow(arg, 3)  # function
            y_list.append(y)
            Integral += abs(y * step)
        x_list.pop(len(x_list) - 1)

    plt.title('Integral, countOfIteration = ' + str(n) +' equipment = '+ equipment)
    plt.bar(x_list, y_list, width=step, align='edge', color='g')
    plt.plot(x_list, y_list, 'y')
    plt.plot(x_list_line, y_list_line, 'k')
    mytable.add_row([Integral, step, 4, Integral - 4, n, equipment])
    plt.show()

step = int(input("Введите количество итераций: "))
equipment = input("Введите оснащение: ")
mytable = PrettyTable()
mytable.field_names = ["\033[34m{}".format("Интеграл ") + "\033[0m ",
                       "\033[34m{}".format("Шаг интегрирования ") + "\033[0m ",
                       "\033[34m{}".format("Численное решение ") + "\033[0m ",
                       "\033[34m{}".format("Погрешность ") + "\033[0m ",
                       "\033[34m{}".format("Количество итераций ") + "\033[0m ",
                       "\033[34m{}".format("Оснащение ") + "\033[0m "]
equipments = ["left", "right", "middle", "random"]
if(equipment in equipments):
     create_table(step, mytable, equipment)
     print(mytable)
else:
    print("Chose equipment from the list: "+ str(equipments))


