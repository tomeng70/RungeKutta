import math
from matplotlib import pyplot as plt

H = 0.01                # the time step (seconds)
R = 0.03                # growth rate
K = 100                 # carrying capacity
N0 = 1                  # initial population (at t = 0)
TIME_LIMIT = 500        # time limit for plot (seconds)

# our analytical solution.
def popLogistic(t):
    val = K / (1 + (K / N0 - 1) * math.exp(-R * t))
    return val

# the rate equation for our system.
def rateEqn(N, t):
    # note for logistic growth, the rate does not depend on time.
    # instead, it's based on the current population and carrying capacity.
    # will still pass time as an argument to this function, 
    # even though it's not needed.
    val = R * ((K - N)/K) * N
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

def main():
    # t is the current time in seconds.
    t = 0

    # tList holds the time values.
    tList = [0]

    # Nlist holds the analytical values for population size.
    NList = [N0]

    # NRKList holds the estimated values for population size (RK4).
    NRKList = [N0]

    while (t <= TIME_LIMIT):
        # use previous estimated pop
        # and previous time to calculate 
        # the next estimated pop
        NPrev = NRKList[-1]
        NNext = calcNextRK(NPrev, t)
        NRKList.append(NNext)

        # add time to list
        t = t + H
        tList.append(t)

        # add next element in list analytic solution
        pop = popLogistic(t)
        NList.append(pop)

    # plot results. 
    plt.plot(tList, NList, ".", tList, NRKList, "^")
    plt.title("Logistic Growth: Population vs Time (sec)")
    plt.show()

main()
