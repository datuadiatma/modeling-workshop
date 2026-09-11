# Forward Euler

*Numerical Modeling Workshop — Fall 2026*

In our first session we learn that models are **mathematical description of temporal and/or spatial changes in a system** (Slingerland and Kump, 2011). Which means, what we refer to as a model is not the code nor the pretty figures they usually put in their papers but the sets of equations modelers use to describe a process or a system.

In most cases, the equations that modelers use to describe the process or system they try to model are in the form of differential equations (or a set of differential equations). The equations can either be `ordinary` or `partial`. Ordinary differential equations (or ODEs) refer to differential equations with one variable. The reservoir and isotope mass balance that we discussed in our previous session are examples of ODE.

$$\frac{dM_o}{dt} = F_{input} - F_{output}$$

$$\frac{d(R_o M_o)}{dt} = F_{input} R_{input} - F_{output} R_{output}$$

So what does solving ODEs mean? It simply means removing the $\frac{d}{dt}$ and find the values of $M_o(t)$ (the size of the reservoir at time $t$). In other words, we need to integrate the equations.

## Solving ODEs numerically
For simple cases we can solve ODEs with pen and paper. (If you took Calc 1 or Calc 2 recently, you are probably better at doing this that the old heads in our group). The act of find the exact solutions of ODEs is known as *solvinf ODEs **analytically***. However, in most cases the ODEs we need to solve are too difficult to solve (or the modelers are too lazy, I can't really tell 😩), such that we have to make *an estimation*. This process is known as *solving ODEs* ***numerically***.

The core process of solving ODEs numerically is discretization, or cutting a continous function into discrete chunks. What do I mean by that?

If we take a stroll down the memory lane and recall what we learn from a Calc 1 or Calc 2 class, you may remember that we define the derivative of function $y(t)$ at time $t$ as:

$$\frac{dy(t)}{dt}=\lim_{\Delta t \to 0} \frac{y(t + \Delta t) - y(t)}{\Delta t}$$

Now, as a numerical approximation to the derivative, the simplest option is simply not taking the limit $\lim_{\Delta t \to 0}$, but assume a small (which of course, relative) $\Delta t$. This is refered to as the **finite difference method** of discretization. If we take this `lazy` approach we can transform *Eq. 3* into something that looks more managable such as this:

$$\frac{dy(t)}{dt} \approx \frac{y(t + \Delta t) - y(t)}{\Delta t}$$

In practice, discretization means instead of solving the ODE to find $M_o$ at all $t$, we need to divide the function into smaller chunks of discrete time-steps.

## Forward Euler / Euler's Method

Now that we have a more *manageable* way to estimate the derivative of a function, we can re-arrange the *Eq. 4* into:

$$ y(t + \Delta t) =y(t) +  \frac{dy(t)}{dt} \times \Delta t$$

This equation shows that we can make a numerical solutions of ODEs by stepping forward in time: start from a known state, estimate how fast it's changing, and take a small step.

In other words, if the ODE to describe the reservoir mass balance, we can estimate the size of reservoir $M_o$ at time $t1$ by plugging $t1$ into $\frac{dM_o}{dt}$ multiply the result by the time step we choose ($\Delta t$) and add the result to the previous known value (or the initial value).

Geometrically, solving ODEs using this method can be illustrated in the figure below.

```{figure} https://upload.wikimedia.org/wikipedia/commons/e/ee/Forward_Euler_method_illustration.png
:name: fig-euler
:width: 60%
:align: center

Forward Euler: each step follows the tangent at the start of the interval, drifting away from the true curve. Source: Wikimedia Commons.
```

This method, while being one of the oldest numerical method to solve ODE, is still one of the most popular.

:::{note}
This method even made a *cameo* in the movie Hidden Figure (see below).

```{iframe} https://www.youtube.com/embed/v-pbGAts_Fg
:width: 65%
The scene from the movie **Hidden Figures** where Katherine Johnson and her team realize they can use Forward Euler Method to solve complex re-entry trajectory for John Glenn's space capsule.
```
:::


In the next section we will practice what we learn by solving an ODE using Forward Euler in Excel.