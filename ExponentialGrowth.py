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

# this is our rate equation for exponential growth.
def rateEqn(N, t):
    # note for exponential growth growth, the rate does not depend on time.
    # instead, it's based on the current population only.
    # we will still pass time as an argument to this function, 
    # even though it's not needed.
    val = R * N
    return val

# this method calculates the population at the next step in time
# using the Runge-Kutta 4th order method.
def calcRKNext(N, t):
    # calculate the runge-kutta terms.
    k1 = rateEqn(N, t)
    k2 = rateEqn(N + k1 / 2, t + H/2)
    k3 = rateEqn(N + k2 / 2, t + H/2)
    k4 = rateEqn(N + k3, t + H)
    
    # estimate the next value based on previous value.
    # use a weighted average of the 4 RK terms.
    nextVal = N + H * (k1 +  2 * k2 +  2 * k3 + k4) / 6
    return nextVal

# our main function.
def main():
    # t is the current time in seconds.
    t = 0

    # deltaT is our step size.
    deltaT = H

    # tList holds the time values.
    tList = [0]

    # Nlist holds the analytical values for population size.
    NList = [N0]

    # NEstList holds the estimated values for population size (backwards Euler).
    NEstList = [N0]

    # NRKList holds the estimated RK4 values for population size.
    NRKList = [N0]

    while (t <= TIME_LIMIT):
        # use previous estimated pop
        # and previous time to 
        # calculate the next estimated pop
        NPrev = NEstList[-1]
        NNext = calcNext(NPrev)
        NEstList.append(NNext)

        # use runge-kutta method with the previous value 
        # and previous time to estimate the next value of N.
        NrkPrev = NRKList[-1]
        Nrk = calcRKNext(NrkPrev, t)
        NRKList.append(Nrk)

        # update time.
        t = t + deltaT
        tList.append(t)

        # calculate the next exact value for population and add to list.
        pop = popExp(t)
        NList.append(pop)

    # plot results. 
    plt.plot( tList, NList, ".", tList, NEstList, '+', tList, NRKList, "^")
    plt.title("Population Growth vs Time (sec)")
    plt.show()

main()


    
