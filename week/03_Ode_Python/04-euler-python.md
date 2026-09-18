# Forwar Euler Implementation in Python

*Numerical Modeling Workshop — Fall 2026*

We will solve a simple ODE step by step in Python using the Forward Euler method:

$$
\frac{dy}{dt} = \cos(t), \qquad y(0) = 0, \qquad 0 \le t \le 2\pi
$$

We pick this equation on purpose: we know the exact answer, so we can check how good our numerical solution is.

Recall the Forward Euler update:

$$
y^{n+1} = y^{n} + \Delta t^{n} \cdot \cos(t^{n})
$$

:::{note}
The superscript $n$ is **not** a power. It is an *index* that counts time steps: $t^{1}$ is the first time, $t^{2}$ the second, and so on. In Excel, each $n$ is simply one row.
:::

## Importing libraries
One of the many perks of using Python is its *rich ecosystem* meaning it has a lot of libraries that makes code writing so much easier. Libraries is a `fancy` word to describe ***Python code and functions other people have written that are available to us***.

Here are the three most important libaries in scientific computing.

```Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

This is the part where I explain what each library does ....

## Function in Python
A function is an object that takes inputs, do some stuff (which includes mathematical operations, if statements evaluations, for loops, etc) and produce outputs. 

We create a function in Python using `def`.

```Python
def square(x):
    return x**2
```

We use functions, to **define** or **initialize** our ODEs / governing equations. This is how we translate $\frac{dy}{dt} = \cos(t)$ into a python function called `dy_dt`.

```Python
def dy_dt(t):
    return np.cos(t)
```