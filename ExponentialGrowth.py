import math
from matplotlib import pyplot as plt

H = 0.01
R = 0.3                # growth rate
N0 = 1                  # initial population (at t = 0)
TIME_LIMIT = 50        # time limit for plot (seconds)

def popExp(t):
    # calculate the population using exponential growth equation.
    val = N0 * math.exp(R * t)
    return val

def calcNext(Nprev):
    val = Nprev / (1 - R * H)
    return val

def main():
    print("hello")

    t = 0
    deltaT = H
    tList = [0]
    NList = [N0]
    NEstList = [N0]
    errList = [0]


    while (t <= TIME_LIMIT):
        # use previous estimated pop
        # and previous time to 
        # calculate the next estimated pop
        NPrev = NEstList[-1]
        NNext = calcNext(NPrev)
        NEstList.append(NNext)

        err = NList[-1] - NNext
        errList.append(err)

        # add time to list
        t = t + deltaT
        tList.append(t)

        # add next element in list analytic solution
        pop = popExp(t)
        NList.append(pop)

    # plot results. 
    plt.plot( tList, NList, ".", tList, NEstList, '+')
    plt.title("Population Growth vs Time (sec)")
    plt.show()

    print("goodbye!")

main()


    
