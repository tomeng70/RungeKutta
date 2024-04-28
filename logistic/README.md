Logistic Growth
Imagine you have a population of foxes that live on an island. If you were to track the population size over time, you might observe that as the population size increases, the rate of growth of the population slows down. In an environment like an island, the resources available to the foxes are limited. As a result, the island can only supported a limited number of foxes at any point in time.

<p align="center">
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/7a303080-d4b1-4927-93e8-2ec8024b021e" width=200></img>
</p>

Biologists refer to this limit as the _carrying capacity_ of the island.  The rate of change of a resource-constrained population can be modeled using the following equation,

<p align="center">
  $\dfrac{dN}{dt} = r \cdot (\dfrac{K - N}{K}) \cdot N$
</p>

In this equation, which describes _logistic growth_, the variable $N$ represents the population size, the constant $r$ represents the growth rate, and the constant $K$ represents the carrying capacity of the environment.  

For logistic growth, if the population size relative to the carrying capacity of the environment is low, then the rate of change of the population "looks" exponential in nature.  However, as the population increases and approaches the carrying capacity, the rate of change of the population approaches zero.

## An Exact Solution
The rate equation can be rewritten in the following form,

<p align="center">
  $\dfrac{K}{N(K-N)} \, dN = r \, dt$
</p>

This rate equation <a href = "../doc/logisticgrowth.pdf">can be integrated</a> to solve for the population size as a function of time.

<p align="center">
  $\int{\dfrac{K}{N(K-N)} \, dN } = \int{r \, dt}$
</p>

The solution is known as the logistic growth equation:

<p align="center">
  $N(t) = \dfrac{K}{1 + (K/N_0 - 1) \, e^{-rt}}$
</p>

where $N$ is the population size as a function of time, $t$, $K$ is the carrying capacity of the environment, $N_0$ is the initial population size, and $r$ is the rate of growth of the population.

## Runge Kutta Fourth Order Method
The numerical method that we used in the previous section is considered to be an _implicit method_ because in order to solve for the value of our population function at the current time, we have to solve an equation that involves both the previous value of the population function as well as the current value of the population function.  

The Runge-Kutta Fourth Order (RK4) method is a popular numerical method for solving ordinary different equations such as the exponential growth equation.  It is considered to be _explicit method_, because the method only requires that we use the information about the state of our system from a previous time step to solve for the state of our system at the current time.  

Describing the Runge-Kutta method in detail is beyond the intended scope of this repository.  However, the following YouTube video provides a very brief, but helpful description of how the RK4 method of estimation is implemented:

<p align="center">
  <a href = "https://youtu.be/ydFM5yON-24?feature=shared">The Runge-Kutta Fourth Order Method (YouTube)</a>
</p>

The Python program, ExponentialGrowth.py, has code that calculates the estimated population size at time $t = t_{i+1}$ using the average of the four weighted RK terms:

```
def rateEqn(N, t):
    # note for exponential growth growth, the rate does not depend on time.
    # instead, it's based on the current population only.
    # we will still pass time as an argument to this function, 
    # even though it's not needed.
    val = R * N
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
```
If you run the program you see that the estimated population values (represented by the '^' symbols on the plot) are very close to the exact values (represented by the '.' symbols on the plot):
