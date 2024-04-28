# Introduction
This repository contains code that demonstrates how an estimated solution to an ordinary differential equation can be generated using numerical methods.  There are two projects within this repository.  The project <a href="./exponential/">exponential/</a> demonstrates how the backwards Euler method can be used to obtain an estimated solution for the exponential growth rate problem.  The project plots the population vs time for a colony that grows exponentially.  The estimated results are compared to the exact (analytical) results in the plot.

The second project, <a href="./logistic/">logistic/</a>, demonstrates how the Runge-Kutta 4th order (RK4) method can be used to obtain an estimated solution for the logistic growth rate problem.  While the RK4 does not work well for modeling a system that grows exponentially, it can be used to model a system that experiences logistic growth.  In logistic growth, the carrying capacity of the system limits the growth of the population and the RK4 method is able to more accurately model the population size as a function of time.

# Requirements
In order to be able to the run the programs in this repository, you will need Python3 installed on your computer.  You will also need the matplotlib package installed in your Python3 environment.

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
The folder <a href="./logistic/">logistic/</a> contains a Python program, <a href="./logistic/Logistic.py">Logistic.py</a>, which plots two curves that represent the logistic growth of a colony:
- The data points that are marked with the "." symbols are the analytically derived values for population.
- The data points that are marked with the "+" symbols are the estimated values that were calculated using the RK4 iterative method.

<p align="center">
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/e96dec8e-d006-4004-a1fc-775c300a0d0b" width="400" >
  <img src="https://github.com/tomeng70/RungeKutta/assets/12796159/8ef079f1-1169-4fc5-b450-3ac0e665deec" width="400" >
</p

Click <a href="./logistic/README.md">here</a> for a detailed description of the <a href="./logistic/README.md">Logistic Growth problem</a>.
