# Given a list of integers, return a list of numbers that after being squared
# and added 10, the last digit is not 5 or 6.
# Complete the kinderSquare method. It receives an array of integers, arr.
# It returns a list of integers consisting of those elements of the original
# list that after being squared and added 10, their last digit is not 5 or 6.
# Please note that the relative order of the elements in the output array
# must be the same order that the one in the input array


print("--Kinder Square--")
numbers = []

with open('exercise_1.txt', 'r') as f:
    for line in f:
        numbers.append(line.split(',')[0])


def kinderSquare():
    n = int(numbers[0])
    for i in range(1, n + 1):
        value = (int(numbers[i]) ** 2) + 10
        value_string = str(value)
        last_digit = value_string[len(value_string) - 1]
        if last_digit != "5" and last_digit != "6":
            print(value)


kinderSquare()

print("--Minefield--")

# You have to walk through a minefield and you know the steps you can
# take in order to not come across a mine. The field is mapped to a
# cartesian coordinate system and each step you could take is in a straight
# line, adding to one of the coordinates (x or y) of the standing point, the
# value of the other coordinate. This means that from point (x, y) you can
# go either to (x + y, y) or (x, x + y). The idea is to see if it is possible to go
# from a starting point (x , y ) to an ending point (x , y ).

input = [2, 1, 1, 2, 5, 1, 1, 6, 3]


def isPossible(x_start, y_start, x_end, y_end):
    if x_start == x_end and y_start == y_end:
        return 1
    if x_start > x_end and y_start > y_end:
        return 0
    if x_start + y_start <= x_end:
        return isPossible(x_start + y_start, y_start, x_end, y_end)
    if x_start + y_start <= y_end:
        return isPossible(x_start, x_start + y_start, x_end, y_end)


n = input[0]
value = input[1:]
index = 0
for time in range(0, n):
    slice = value[index:index + 4]
    response = isPossible(slice[0], slice[1], slice[2], slice[3])
    if response:
        print('YES')
    else:
        print('NO')
    index += 3

print("--Multiple Choice Panic--")

with open('exercise_3.txt', 'r') as f:
    line_index = 0
    t = 0
    exams = []
    exam = [0, 0, 0, 0, 0]
    for line in f:
        if line_index == 0:
            t = line.rstrip()
        elif line_index == 1:
            n = line.rstrip()  # cantidad de preguntas
            exam[0] = n
        elif line_index == 2:
            p = line.rstrip()  # puntos necesarios para pasar el examen
            exam[1] = p
        elif line_index == 3:
            q = line.rstrip().split(' ')  # numero de opciones por pregunta
            exam[2] = q
        elif line_index == 4:
            pc = line.rstrip().split(' ')  # punto obtenidos por respuesta
            exam[3] = pc
        else:
            pw = line.rstrip().split(' ')  # punto perdidos por respuesta
            exam[4] = pw
            exams.append(exam)
            line_index = 0
            exam = [0, 0, 0, 0, 0]
        line_index += 1


def weightedAverage(cant, cantip, cantin):
    return ((1 / float(cant)) * cantip) - (((float(cant) - 1) / float(cant)) * cantin)


def isExpectedToPassExam(n, p, q, pc, pw):
    # - N: Number of questions
    # - P: Score Bob needs to pass
    # - q: An array of N integers, q being the number of options for question i
    # - pc: An array of N numbers, pc being the points gained for answering question i correctly
    # - pw: An array of N numbers, pw being the points lost for answering question i wrongly It returns the string
    # YES if the expected score of answering all questions randomly is P or higher,
    # otherwise it returns NO.
    score = 0

    for answer_index in range(0, int(n)):
        score += weightedAverage(int(q[answer_index]), float(pc[answer_index]), float(pw[answer_index]))

    if score >= float(p):
        return 'YES'
    return 'NO'


for exam in exams:
    print(isExpectedToPassExam(exam[0], exam[1], exam[2], exam[3], exam[4]))

print("--OpenMateLab--")

# As part of an initiative to develop an open source alternative to "Matelab"
# (a numerical methods environment), we must implement the sequences module.
# Although most common sequences (such as Fibonacci) have been implemented,
# the team also included the Jaime Roos sequence, which is defined the following way:
# JR0=a
# JR1 = b
# JR2 = c
# JRn = JRn-1 + JRn-2 + JRn-3
# With a, b and c being variable and 2 < n.

# Input Format
# Input will consist of 7 lines.
# Line 1 will be the first term of the Fibonacci sequence, Fib0
# Line 2 will be the second term of the Fibonacci sequence, Fib1
# Line 3 will be the term of the Fibonacci sequence that needs to be calculated. (i such that we want Fibi)
# Line 4 will be the first term of the Jaime Roos sequence, JR0
# Line 5 will be the second term of the Jaime Roos sequence, JR1
# Line 6 will be the third term of the Jaime Roos sequence, JR2
# Line 7 will be the term of the Jaime Roos sequence that needs to be calculated (j such that we want JRj)

# Output Format
# Output will consist of two lines.
# The first line will contain an integer denoting Fibi
# The second line will contain an integer denoting JRj

input = []  # [Fib0, Fib1, i, JR0, JR1, JR2, j]  i => Fibi, j => JRj

with open('exercise_4.txt', 'r') as f:
    for line in f:
        input.append(int(line))


def fibonacci(Fib0, Fib1, i):
    fib_i_minus_2 = Fib0
    fib_i_minus_1 = Fib1
    fib_i = 0
    for i in range(2, i + 1):
        fib_i = fib_i_minus_1 + fib_i_minus_2
        fib_i_minus_2 = fib_i_minus_1
        fib_i_minus_1 = fib_i

    return fib_i


result = fibonacci(input[0], input[1], input[2])
print(result)


def jaime_roos(jr0, jr1, jr2, j):
    jr_j_minus_3 = jr0
    jr_j_minus_2 = jr1
    jr_j_minus_1 = jr2
    jr_j = 0
    for i in range(3, j + 1):
        jr_j = jr_j_minus_3 + jr_j_minus_2 + jr_j_minus_1
        jr_j_minus_3 = jr_j_minus_2
        jr_j_minus_2 = jr_j_minus_1
        jr_j_minus_1 = jr_j

    return jr_j


result = jaime_roos(input[3], input[4], input[5], input[6])

print(result)

print("--Dishwashers Paradise--")


class KitchenPorter:

    def __init__(self, size_stack):
        self.stacks_dish = []
        self.size_stack = size_stack
        self.instructions = {"ADD": self.add, "REMOVE": self.remove, "COUNT": self.count}

    def add(self, id_dish):
        if len(self.stacks_dish) > 0 and len(self.stacks_dish[-1]) < self.size_stack:
            self.stacks_dish[-1] = [id_dish] + self.stacks_dish[-1]
        else:
            self.stacks_dish.append([id_dish])

    def remove(self, _param):
        if len(self.stacks_dish) != 0:
            print(self.stacks_dish[0].pop(0))
            self.order_dishes()

    def count(self, id_stack):
        if id_stack + 1 > len(self.stacks_dish):
            print(-1)
        else:
            print(len(self.stacks_dish[id_stack]))

    def order_dishes(self):
        if not len(self.stacks_dish) or not len(self.stacks_dish[1]):
            return

        to_remove = []
        for i in range(1, len(self.stacks_dish)):
            self.stacks_dish[i - 1] = [self.stacks_dish[i].pop(0)] + self.stacks_dish[i - 1]
            if not len(self.stacks_dish[i]):
                to_remove.append(i)

        for index in to_remove:
            self.stacks_dish.pop(index)

    def read_instruction(self, instruction, param):
        self.instructions[instruction](param)


input = []

with open('exercise_5.txt', 'r') as f:
    for line in f:
        input.append(line.strip().split(" "))

n = int(input[0][0])  # stack size
q = int(input[1][0])  # queries amount

instructions = input[2:]

kitchen_porter = KitchenPorter(n)

for instruction in instructions:
    instruction_word = instruction[0]
    param = 0
    if len(instruction) > 1:
        param = int(instruction[1])
    kitchen_porter.read_instruction(instruction_word, param)



print("--Freeing the Zoo--")

input = []

with open('exercise_6_1.txt', 'r') as f:
    for line in f:
        input.append(line.strip().split(" "))

print(input)

import functools


def getAnimals(array, capacity_truck):
    sol = []
    legth = len(array)
    if legth < 2:
        return sol
    sol = [0] * 2
    for i in range(0,legth):
        for j in range(0,legth):
            if i != j:
                new_weights = [int(array[i]), int(array[j])]
                sol = getHeaviest(new_weights, sol, capacity_truck)
    if sol == [0]*2:
        sol = []

    return sol


def getHeaviest(new_weights, weights, capacity):
    weight_new = functools.reduce(lambda x, y: x+y, new_weights)
    weight_old = functools.reduce(lambda x, y: x+y, weights)
    if weight_new > capacity:
        return weights
    if weight_new < weight_old:
        return weights
    elif weight_new > weight_old:
        return new_weights
    else:
        max_new = functools.reduce(lambda x,y: max(x,y), new_weights)
        max_old = functools.reduce(lambda x, y: max(x, y), weights)
        if max_new > max_old:
            return new_weights
        else:
            return weights


sol = getAnimals(input[1], int(input[2][0]))
print("Sol is: %s" % sol)

input = []

with open('exercise_6_2.txt', 'r') as f:
    for line in f:
        input.append(line.strip().split(" "))

print(input)

sol = getAnimals(input[1], int(input[2][0]))
print("Sol is: %s" % sol)