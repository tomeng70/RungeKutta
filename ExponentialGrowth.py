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

def rateEqn(N, t):
    # note for exponential growth growth, the rate does not depend on time.
    # instead, it's based on the current population only.
    # we will still pass time as an argument to this function, 
    # even though it's not needed.
    val = R * N
    return val

def calcNext(Nprev):
    val = Nprev / (1 - R * H)
    return val

def calcRKNext(N, t):
    # calculate the runge kutta terms.
    k1 = rateEqn(N, t)
    k2 = rateEqn(N + k1 / 2, t + H/2)
    k3 = rateEqn(N + k2 / 2, t + H/2)
    k4 = rateEqn(N + k3, t + H)
    
    # estimate the next value based on previous value.
    nextVal = N + H * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return nextVal

def main():
    print("hello")

    t = 0
    deltaT = H
    tList = [0]
    NList = [N0]
    NEstList = [N0]
    NRKList = [N0]

    while (t <= TIME_LIMIT):
        # use previous estimated pop
        # and previous time to 
        # calculate the next estimated pop
        NPrev = NEstList[-1]
        NNext = calcNext(NPrev)
        NEstList.append(NNext)

        # use runge kutta method to get next
        Nrk = calcRKNext(NPrev, t)
        NRKList.append(Nrk)

        # add time to list
        t = t + deltaT
        tList.append(t)

        # add next element in list analytic solution
        pop = popExp(t)
        NList.append(pop)

    # plot results. 
    plt.plot( tList, NList, ".", tList, NEstList, '+', tList, NRKList, "^")
    plt.title("Population Growth vs Time (sec)")
    plt.show()

    print("goodbye!")

main()


    
