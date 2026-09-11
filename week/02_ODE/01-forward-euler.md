# Forward Euler

*Numerical Modeling Workshop — Fall 2026*
---

In our first session we learn that models are **mathematical description of temporal and/or spatial changes in a system** (Slingerland and Kump, 2011). So, what we refer to as a model is not the code nor the pretty figures they usually put in their papers but the sets of equations modelers use to describe a process or a system.

In most cases, the equations that modelers use to describe the process or system they try to model are in the form of differential equations (or a set of differential equations). The equations can either be `ordinary` or `partial`. Ordinary differential equations (or ODEs) refer to differential equations with one variable. The reservoir and isotope mass balance that we discussed in our previous session are examples of ODE.

$$\frac{dM_o}{dt} = F_{input} - F_{output}$$

$$\frac{d(R_o M_o)}{dt} = F_{input} R_{input} - F_{output} R_{output}$$

So what does solving ODEs mean? It simply means removing the $\frac{d}{dt}$ and find the values of $M_o(t)$ (the size of the reservoir at time $t$). In other words, we need to integrate the equations.

## Solving ODEs numerically
For simple cases we can solve ODEs with pen and paper. (If you took Calc 1 or Calc 2 recently, you are probably better at doing this that the old heads in our group :)). The act of find the exact solutions of ODEs ** However, in most cases the ODEs we need to solve are too difficult to solve (or the modelers are too lazy, I can't really tell!). Therefore 


:::{danger} Come again later!
:class: dropdown
Content is under construction, check again in a few days.
:::