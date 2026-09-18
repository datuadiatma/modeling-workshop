# Runge–Kutta 4 (RK4)

*Numerical Modeling Workshop — Fall 2026*

Forward Euler uses only one slope per step: the slope at the *start*. When the slope changes during the step, Euler drifts off the true curve.

The idea behind Runge–Kutta is simple: **sample the slope at several points within the step, then take a weighted average.** A better slope means a better step.

For an ODE $\dfrac{dy}{dt} = f(t, y)$, RK4 computes four slopes:

$$
\begin{aligned}
k_1 &= f\!\left(t^{n},\; y^{n}\right) && \text{slope at the start} \\
k_2 &= f\!\left(t^{n} + \tfrac{\Delta t}{2},\; y^{n} + \tfrac{\Delta t}{2}\,k_1\right) && \text{slope at the midpoint, using } k_1 \\
k_3 &= f\!\left(t^{n} + \tfrac{\Delta t}{2},\; y^{n} + \tfrac{\Delta t}{2}\,k_2\right) && \text{slope at the midpoint, using } k_2 \\
k_4 &= f\!\left(t^{n} + \Delta t,\; y^{n} + \Delta t\,k_3\right) && \text{slope at the end, using } k_3
\end{aligned}
$$

and then takes the step:

$$
y^{n+1} = y^{n} + \frac{\Delta t}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

The two midpoint slopes get double weight because they best represent the whole step.

Geometrically this method can be illustrated as

```{figure} ../../_assets/figs/RK4.svg
:name: fig-rk4
:width: 60%
:align: center
Slopes used by the classical Runge-Kutta method (RK4). 

Source: HilberTraum, CC BY-SA 4.0, [via Wikimedia Commons](https://creativecommons.org/licenses/by-sa/4.0)
```
**Why this method is powerful:** Euler's error shrinks in proportion to $\Delta t$ (halve the step, halve the error). RK4's error shrinks in proportion to $\Delta t^4$ (halve the step, and the error drops **16 times**). It costs four slope calculations per step instead of one, but you can take much bigger steps for the same accuracy.

:::{note}
Most modern ODE solvers are built on this Runge–Kutta idea. Python's `scipy.integrate.solve_ivp` uses `RK45` by default: a Runge–Kutta method that also estimates its own error at every step and adjusts $\Delta t$ automatically.
:::