# Introduction
This repository contains code that demonstrates how an estimated solution to an ordinary differential equation can be generated using numerical methods.  There are two projects within this repository.  The project <a href="./exponential/">exponential/</a> demonstrates how the backwards Euler method can be used to obtain an estimated solution for the exponential growth rate problem.  The project plots the population vs time for a colony that grows exponentially.  The estimated results are compared to the exact (analytical) results in the plot.

The second project, <a href="./logistic/">logistic/</a>, demonstrates how the Runge-Kutta 4th order (RK4) method can be used to obtain an estimated solution for the logistic growth rate problem.  While the RK4 does not work well for modeling a system that grows exponentially, it can be used to model a system that experiences logistic growth.  In logistic growth, the carrying capacity of the system limits the growth of the population and the RK4 method is able to more accurately model the population size as a function of time.


# Exponential Growth
The folder <a href="./exponential/">exponential/</a> contains a Python program, <a href="./exponential/ExponentialGrowth.py">ExponentialGrowth.py</a>, which plots two curves that represent the exponential growth of a colony:
- The data points that are marked with the "." symbols are the analytically derived values for population.
- The data points that are marked with the "+" symbols are the estimated values that were calculated using an _implicit_ iterative method.

<p align="center">
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/3f153c81-e8bc-485a-ac10-b79ee426a811" width="400" >
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/c8319182-0b20-4e42-be49-c26ce5d9f819" width="400" >
</p>


Click <a href="./exponential/README.md">here</a> for a detailed description of the <a href="./exponential/README.md">Exponential Growth problem</a>.

# Logistic Growth
The following plots shows exponential growth calculated two ways:
- "." are the analytically derived values for population.
- "+" are the estimated values calculated using the Runge Kutta method.

<img src="https://github.com/tomeng70/RungeKutta/assets/12796159/8805a7d6-7ae0-46c2-b6b5-17e40b702895" width="500" >
<BR>
<img src="https://github.com/tomeng70/RungeKutta/assets/12796159/91c3fc51-807c-4ed5-84ac-6139722c9f2c" width="500" >







