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

# the rate equation for our system.
def rateEqn(N, t):
    # note for exponential growth, the rate does not depend on time.
    # instead, it's based on the current population and carrying capacity.
    # will still pass time as an argument to this function, 
    # even though it's not needed.
    val = R * N
    return val

# calculate next value in population using previous value and previous time.
def calcNextRK(N, t):
    # calculate the runge kutta terms.
    k1 = rateEqn(N, t)
    k2 = rateEqn(N + k1 / 2, t + H/2)
    k3 = rateEqn(N + k2 / 2, t + H/2)
    k4 = rateEqn(N + k3, t + H)
    
    # estimate the next value based on previous value.
    nextVal = N + H * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return nextVal


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

    # NRKList holds the RK4 estimated values for population size.
    NRKList = [N0]

    while (t <= TIME_LIMIT):
        # use previous estimated pop
        # and previous time to 
        # calculate the next estimated pop
        NPrev = NEstList[-1]
        NNext = calcNext(NPrev)
        NEstList.append(NNext)

        # use previous RK estimated pop
        # and previous time to calculate
        # the next RK estimated pop size.
        NRKPrev = NRKList[-1]
        rk = calcNextRK(NRKPrev, t)
        NRKList.append(rk)

        # update time.
        t = t + H
        tList.append(t)

        # calculate the next exact value for population and add to list.
        pop = popExp(t)
        NList.append(pop)

    # plot results. 
    plt.plot( tList, NList, '.', tList, NEstList, '+', tList, NRKList, '^')
    plt.title("Exponential Growth: Population vs Time (sec)")
    plt.ylim(0, 3.5E6)
    plt.show()

main()
