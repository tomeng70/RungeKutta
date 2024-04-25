# Introduction
This repository demonstrates how you can numerically estimate values for exponential growth and for logistic growth.

The Python program ExponentialGrowth shows how to calculate exponential growth using the theoretical solution. 
It also shows how to estimate the growth by discretizing the rate equation.
Finally, it also shows how to estimate the growth using an application of the Runge Kutta method (4 terms).

The Python program Logistic shows how to calculate logistic growth using the theoretical solution.
It also shows how to estimate the growth using an application of the Runge Kutta Method (4 terms).

Both programs plot the theoretical and estimated values vs time.

# Exponential Growth
The following plots shows exponential growth calculated three ways:
- "." are the analytically derived values for population.
- "+" ar the estimated values calculated using the time discretized rate equation.
- "^" are the estimated values calculated using the Runge Kutta method.

<img src="https://github.com/tomeng70/RungeKutta/assets/12796159/03d08a3d-01ab-4fa8-98de-719df0bb2c1f" width="500" >
<BR>
<img src="https://github.com/tomeng70/RungeKutta/assets/12796159/3d8d1e91-a5d0-4747-aa79-d62eb25e96bb" width="500" >

# Logistic Growth
The following plots shows exponential growth calculated two ways:
- "." are the analytically derived values for population.
- "+" are the estimated values calculated using the Runge Kutta method.

<img src="https://github.com/tomeng70/RungeKutta/assets/12796159/8805a7d6-7ae0-46c2-b6b5-17e40b702895" width="500" >
<BR>
<img src="https://github.com/tomeng70/RungeKutta/assets/12796159/91c3fc51-807c-4ed5-84ac-6139722c9f2c" width="500" >







