# The Exponential Growth Problem
Imagine you had a colony of bacteria that lives in an ideal environment.  In this ideal environment, the bacteria have virtually unlimited food and space to grow.

<p align="center">
  <img  src="https://github.com/tomeng70/RungeKutta/assets/12796159/096f552f-b429-4001-8588-ad25ea19b4a1"> 
</p>

In this scenario, the rate at which the population size of the colony changes is directly proportional to the size of the population itself.
The more bacteria you have, the faster the population will grow.

This rate equation for population growth can be expressed as follows,

<p align="center">
  $\dfrac{dN}{dt} = r \cdot N$
</p>

In this equation, $N$ represents the population size, $t$ represents time, and the variable $r$ is a constant value know as the <i>rate of growth</i> of the population.

## An Exact Solution
An analytical solution for this rate equation can be obtained using calculus. Using algebra, you can rearrange the terms so you get the following equation,

<p align="center">
  $\dfrac{dN}{N} = r \cdot dt$
</p>

You can integrate this equation to solve for $N$ in terms of $t$.

<p align="center">
  $\int{\dfrac{dN}{N}} = \int{ r \cdot dt }$
</p>

Which gives us the following equation,  
<p align="center">
  $ln(N) = r \cdot t + C$
</p>

where the variable $C$ represents a constant value.  This equation can be rewritten in the following form,

<p align="center">
  $N = N_0 \cdot e^{rt}$
</p>

This equation is an exact solution for the population size, $N$, as a function of time, $t$. $N_0$ is the initial population size at time $t = 0$.  If you know the value of your rate of growth, $r$, and the initial population size, $N_0$, then you can calculate the population size at any time, $t$.

## An Implicit Numerical Solution
Some rate problems are not as tractable as this example problem and do not have an analytical solution. If a rate equation does not have a analytical solution, often a numerical method can be used instead to approximate a solution for the equation. A numerically derived solution, which typically requires the power of a digital computer to calculate the solution, can be useful when solving various scientific, engineering, or business-related problems.

The exponential growth rate equation can be used to demonstrate how a numerical or computational solution can be used to calculate an approximate solution for a differential equation.

Imagine we have a bacterial colony that has a growth rate of $r$ and an initial population size of $N_0$ (at time $t = t_0$).  Suppose we wanted to estimate the size of the colony at some later time, where $t = t_1$.  

We can use our rate equation (which tells us what the slope of our solution is at time $t$) and the previous population size to estimate the size at time $t = t_1$:

<p align="center">
  $N(t_1) = N(t_0) + (t_1 - t_0) \cdot \dfrac{dN}{dt}$ 
</p>

If we use the variable $\Delta t$ for the expression $(t_1 - t_0)$, we get the following equation

<p align="center">
  $N(t_1) = N(t_0) + \Delta t \cdot \dfrac{dN}{dt}$ 
</p>

We can substitute our rate equation in place of $\frac{dN}{dt}$ to represent the slope of the population curve at time $t_1$:

<p align="center">
  $N(t_1) = N(t_0) + \Delta t \cdot r \cdot N(t_1)$ 
</p>

Note that the numerical method that we are using to solve for $N(t_1)$ is an _implicit_ method, since in order to solve for $N(t_1)$ we have to solve an equation that involves both $N(t_1)$ and the previous value $N(t_0)$. If we use algebra to solve this implicit equation for $N(t_1)$ we get the following equation,

<p align="center">
  $N(t_1) = \dfrac{N(t_0)} {1 -  r \cdot \Delta t}$ 
</p>

This equation gives us an approximate value of $N$ at time $t = t_1$ in terms of $N$ at time $t = t_0$.  We can then use our estimate of $N(t_1)$ to solve for $N(t_2)$ and continue this process iteratively to generate an estimate of the population size as a function of time.

Our generic equation looks like the following,

<p align="center">
  $N(t_{i+1}) = \dfrac{N(t_i)} {1 -  r \cdot h}$ 
</p>

Note that by convention, the variable $h$ is used in place of $\Delta t$.  The variable $h$ is referred to as the _time step_. 

A computer program can use this equation to generate an array of values that represent the estimated population size at sequential, discrete instances in time.  

The Python program, ExponentialGrowth.py, has a function called calcNext().  This function calculates the estimated population size at time $t = t_{i+1}$ using the estimated population size at time $t = t_i$:

```
# estimate population using backward Euler method.
def calcNext(Nprev):
    # calculate the population at the next step in time
    # using backward Euler method (an implicit solution).
    val = Nprev / (1 - R * H)
    return val
```
ExponentialGrowth.py also has a function called popExp() that calculates the exact population size using the exponential growth equation:

```
# calculate the population using exponential growth equation.
def popExp(t):
    val = N0 * math.exp(R * t)
    return val
```

If you run the program you see that the estimated population values (represented by the '+' symbols on the plot) are very close to the exact values (represented by the '.' symbols on the plot):

<p align="center">
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/3f153c81-e8bc-485a-ac10-b79ee426a811" width="400" >
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/c8319182-0b20-4e42-be49-c26ce5d9f819" width="400" >
</p>

## Runge-Kutta Method
For the other project in this repository (logistic growth) a technique known as the Runge-Kutta 4th order (RK4) method is used to model the system behavior as a function of time.  While the RK4 method does a good job modeling logistic growth of a population, it generally does a poor job modeling the behavior of a system that experiences exponential growth.  The RK4 method is an _explicit_ method.  This means that in order to solve for the current system state, it uses past system state information and interpolates this data to estimate what the current system state should be.

The RK4 method uses four weighted terms that are generated using previous data to estimate what the future growth of the system will look like. For exponential growth, where the rate of change is very rapid over time, the interpolation scheme of the RK4 method has a hard time accurately modeling this rapidly changing system. An implicit method like the backwards Euler method can often lead to more accurate results for this type of system.

The Python program, <a href="./ExponentialGrowthWithRK.py">ExponentialGrowthWithRK.py</a> contains additional code that estimates the exponential population growth using the RK4 method.  You can see from the plots of this version of the program that the RK4 scheme (represented by the green '^' symbols in the plots) does not accurately model the exponential population growth, especially when compared to the accuracy of the results calculated using the implicit backwards Euler method (represented by the orange '+' symbols).

<p align="center">
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/96433a46-8698-4fe7-9529-fd6f4750bd6a" width="400" >
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/8c85cf13-ce9d-4635-ac94-1a0577ce05eb" width="400" >
</p>
