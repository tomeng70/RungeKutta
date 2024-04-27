import math
from matplotlib import pyplot as plt

H = 0.01                # time step (seconds)
R = 0.3                 # growth rate
N0 = 1                  # initial population (at t = 0)
TIME_LIMIT = 50         # time limit for plot (seconds)

# calculate the population using exponential growth equation.
def popExp(t):
    val = N0 * math.exp(R * t)
    return val

# estimate population using backward Euler method.
def calcNext(Nprev):
    # calculate the population at the next step in time
    # using backward Euler method (an implicit solution).
    val = Nprev / (1 - R * H)
    return val

# our main function.
def main():
    # t is the current time in seconds.
    t = 0

    # tList holds the time values.
    tList = [0]

    # Nlist holds the analytical values for population size.
    NList = [N0]

    # NEstList holds the estimated values for population size (backwards Euler).
    NEstList = [N0]

    while (t <= TIME_LIMIT):
        # use previous estimated pop
        # and previous time to 
        # calculate the next estimated pop
        NPrev = NEstList[-1]
        NNext = calcNext(NPrev)
        NEstList.append(NNext)

        # update time.
        t = t + H
        tList.append(t)

        # calculate the next exact value for population and add to list.
        pop = popExp(t)
        NList.append(pop)

    # plot results. 
    plt.plot( tList, NList, ".", tList, NEstList, '+')
    plt.title("Exponential Growth: Population vs Time (sec)")
    plt.show()

main()
