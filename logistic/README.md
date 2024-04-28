# Logistic Growth
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
The Runge-Kutta Fourth Order (RK4) method is a popular numerical method for solving ordinary different equations such as the logistic growth equation.  It is considered to be _explicit method_, because the method only requires that we use the information about the state of our system from a previous time step to solve for the state of our system at the current time.  

This method attempts to model the behavior of the system more accurately by using an average of weighted terms to _interpolate_ what the state of the system will be in the future.  Describing the Runge-Kutta method in detail is beyond the intended scope of this repository.  However, the following YouTube video provides a very brief, but helpful description of how the RK4 method of estimation is implemented:

<p align="center">
  <a href = "https://youtu.be/ydFM5yON-24?feature=shared">The Runge-Kutta Fourth Order Method (YouTube)</a>
</p>

The Python program, <a href="./Logistic.py">Logistic.py</a>, has code that calculates the estimated population size at time $t = t_{i+1}$ using the average of the four weighted RK terms:

```
# the rate equation for our system.
def rateEqn(N, t):
    # note for logistic growth, the rate does not depend on time.
    # instead, it's based on the current population and carrying capacity.
    # will still pass time as an argument to this function, 
    # even though it's not needed.
    val = R * ((K - N)/K) * N
    return val

# calculate next value in population using previous value and previous time.
def calcNext(N, t):
    # calculate the runge kutta terms.
    k1 = rateEqn(N, t)
    k2 = rateEqn(N + k1 / 2, t + H/2)
    k3 = rateEqn(N + k2 / 2, t + H/2)
    k4 = rateEqn(N + k3, t + H)
    
    # estimate the next value based on previous value.
    nextVal = N + H * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return nextVal
```

If you run the program you see that the RK4 estimated population values (represented by the '^' symbols on the plot) are very close to the exact values (represented by the '.' symbols on the plot):

<p align="center">
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/757d9566-69ee-4f9c-88da-f8df8267edf9" width="400" >
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/db4110c4-68f4-40fb-9f66-e49f1ba4eeba" width="400" >
</p>

Interestingly enough, while the RK4 method does a good job in this example at modeling the logistic growth of a population, it generally does a poor job modeling the behavior of a system that experiences <a href="../exponential/README.md">exponential growth</a>. The RK4 method is an _explicit_ method.  This means that in order to solve for the current system state, it uses past system state information and interpolates this data to estimate what the current system state should be.  Explicit methods can have difficulty modeling systems that experience large changes in short time periods (like exponential growth).

The RK4 method uses four weighted terms that are generated using previous data to estimate what the future growth of the system will look like. For exponential growth, where the rate of change is very rapid over time, the interpolation scheme of the RK4 method has a hard time accurately modeling this rapidly changing system. An implicit method like the backwards Euler method can often lead to more accurate results for this type of system.
