import random
from data.io import *

def board_boundaries(x,y):
        num = x * y
        if num % 2 == 0:
            print("Good boundaries")
            return True
        else:
            print("error out of boundaries")
            return False





def symbols_and_letters(state):
    x = int(state["is x"])
    y = int(state["is y"])
    combaine = x * y // 2
    numbers = []
    for i in range(combaine):
        numbers.append(i)
        numbers.append(i)
    print(numbers)
    return numbers



def shuffel(state,deck):
    r =deck
    new_matrix = []
    for i in range(state["is x"]):
        mat = []
        for j in range(state["is y"]):
            mat.append(random.shuffle(r))
    return new_matrix



def bingo(x,y):
    if x == y:
        print("correct")
        return True
    else:
        print("not this time try again")


def create_matrix(state,list_num):
    new_list = list_num
    count = 0
    matrix = []
    for i in range(state["is x"]):
        mat = []
        for j in range(state["is y"]):
            mat.append(new_list[count])
            count += 1
        matrix.append(mat)
    return matrix
def print_matrix(matrix):
    for i in matrix:
        print(i)


def user_matrix(state):
    user = []
    for i in range(state["is x"]):
        mat = []
        for j in range(state["is y"]):
            mat.append("x")
        user.append(mat)
    return user

