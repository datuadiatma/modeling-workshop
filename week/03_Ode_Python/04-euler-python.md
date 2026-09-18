# Forward Euler Implementation in Python

*Numerical Modeling Workshop — Fall 2026*

We will solve a simple ODE step by step in Python using the Forward Euler method:

$$
\frac{dy}{dt} = \cos(t), \qquad y(0) = 0, \qquad 0 \le t \le 2\pi
$$

We pick this equation on purpose: we know the exact answer, $y(t) = \sin(t)$, so we can check how good our numerical solution is.

Recall the Forward Euler update:

$$
y^{n+1} = y^{n} + \Delta t^{n} \cdot \cos(t^{n})
$$

:::{note}
The superscript $n$ is **not** a power. It is an *index* that counts time steps: $t^{0}$ is the starting time, $t^{1}$ is the next one, $t^{2}$ the one after that, and so on. In Excel, each $n$ is simply one row. Starting the count at $0$ is deliberate — Python counts from $0$ too.
:::

## Importing libraries
One of the many perks of using Python is its *rich ecosystem*, meaning it has a lot of libraries that make writing code so much easier. Library is a fancy word for ***Python code and functions other people have written that are available to us***.

Here are the three most important libraries in scientific computing.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

- **NumPy** (`np`) gives us fast arrays of numbers and math functions that work on them: `np.cos`, `np.sin`, `np.pi`, `np.zeros`, and many more. Think of a NumPy array as a single column in a spreadsheet.
- **pandas** (`pd`) gives us tables with named columns, called *DataFrames*. This is the closest thing Python has to an Excel sheet.
- **Matplotlib** (`plt`) makes plots.

The short names `np`, `pd`, and `plt` are just nicknames (aliases) so we don't have to type the full name every time. Everyone uses these same nicknames, so you'll see them in almost any scientific Python code online.

## Function in Python
A function is an object that takes inputs, does some stuff (mathematical operations, if statements, for loops, etc.), and produces outputs.

We create a function in Python using `def`.

```python
def square(x):
    return x**2
```

:::{important}
The indentation (4 spaces) is not decoration. Python uses indentation to know which lines belong *inside* the function. If you forget to put indentation (exactly 4 spaces, no more no less) Python will throw an `IndentationError`.
:::

We use functions to **define** or **initialize** our ODEs / governing equations. This is how we translate $\frac{dy}{dt} = \cos(t)$ into a Python function called `dy_dt`.

```python
def dy_dt(t):
    return np.cos(t)
```

Try it out:

```python
dy_dt(0)
```

You should get `1.0`, because $\cos(0) = 1$.

## For loops: doing the same thing many times

Forward Euler is just one simple step, repeated over and over. In Excel, you'd write the formula once and **drag it down**. In Python, we use a **for loop**.

Here is the simplest possible loop:

```python
for i in range(5):
    print(i)
```

This prints `0, 1, 2, 3, 4`. Two things to notice:

1. `range(5)` starts at `0` and stops **before** `5`. So it runs 5 times, but the last number is `4`.
2. Just like functions, the indented lines are the "body" of the loop. Everything indented runs once per trip through the loop.

Now a loop that *remembers* something from the previous step. Let's add up the numbers 1 through 5:

```python
total = 0
for i in range(1, 6):
    total = total + i
    print(i, total)
```

Look closely at the line `total = total + i`. It says: *the new total is the old total plus something*. That is exactly the structure of Forward Euler:

$$
\underbrace{y^{n+1}}_{\text{new}} = \underbrace{y^{n}}_{\text{old}} + \underbrace{\Delta t \cdot \cos(t^{n})}_{\text{something}}
$$

The only difference is that instead of overwriting one number, we'll keep every step in an array so we can plot it later.

## Setting up the problem

First, define the parameters of our problem.

```python
t_start = 0
t_end = 2 * np.pi
dt = np.pi / 8        # time step, about 0.39
y0 = 0                # initial condition, y(0) = 0

n_steps = int(round((t_end - t_start) / dt))
print(n_steps)
```

You should see `16`. We chose $\Delta t = \pi/8$ so that it divides $2\pi$ into a whole number of steps.

## Initializing arrays to store the solution

Before the loop runs, we need empty "columns" to hold our answers. We create them with `np.zeros`, which makes an array full of zeros that we will overwrite as we go.

```python
t = np.zeros(n_steps + 1)
y = np.zeros(n_steps + 1)

# initial conditions go in the first slot
t[0] = t_start
y[0] = y0
```

:::{note}
**Why `n_steps + 1`?** 16 steps need 17 points: the starting point plus one new point per step. Think of fence posts: 16 sections of fence need 17 posts.
:::

You access or change a single element with square brackets: `y[0]` is the first element, `y[1]` the second, and `y[-1]` is the last one.

## The Excel parallel

If you built this model in Excel earlier, here's how every piece maps onto Python:

| What it is | Excel | Python |
|---|---|---|
| Time step $\Delta t$ | a cell, e.g. `$F$1` | `dt` |
| Time column | column A | array `t` |
| Solution column | column B | array `y` |
| Initial condition | row 2 | `t[0]`, `y[0]` |
| Next time | `=A2+$F$1` | `t[n+1] = t[n] + dt` |
| Euler update | `=B2+$F$1*COS(A2)` | `y[n+1] = y[n] + dt * dy_dt(t[n])` |
| Repeat for every row | drag the formula down | `for` loop |

Notice that in the Excel formula, row 3 only ever looks at row 2. In Python, index `n+1` only ever looks at index `n`. Same idea.

## Stepping forward with Forward Euler

Now we put it together. For each step `n`, we compute the next time and the next value of $y$:

```python
for n in range(n_steps):
    t[n+1] = t[n] + dt
    y[n+1] = y[n] + dt * dy_dt(t[n])
```

That's it — the entire solver is three lines.

`range(n_steps)` gives `n = 0, 1, ..., 15`. On the last trip, `n = 15`, so we fill in `t[16]` and `y[16]`, which is the last slot of our arrays. Everything fits exactly.

:::{tip}
Want to watch it work? Add `print(n, t[n+1], y[n+1])` as a third indented line inside the loop and run it again. You'll see the "rows" being filled in one by one.
:::

## Looking at the results like a spreadsheet

Let's put our arrays into a pandas DataFrame so we can see them as a table, next to the exact solution.

```python
df = pd.DataFrame({
    't': t,
    'y_euler': y,
    'y_exact': np.sin(t),
})
df['error'] = df['y_euler'] - df['y_exact']

df
```

This should look very familiar if you've done this in Excel. Row `0` of the DataFrame is row 2 of your spreadsheet.

## Plotting the solution

Numbers in a table are hard to judge. A plot is much better.

For the exact solution, we evaluate $\sin(t)$ at many closely spaced points so it looks like a smooth curve. `np.linspace(a, b, N)` makes `N` evenly spaced points between `a` and `b`.

```python
t_exact = np.linspace(t_start, t_end, 500)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_exact, np.sin(t_exact), 'k-', label='Exact: sin(t)')
ax.plot(t, y, 'o-', label=f'Forward Euler, dt = {dt:.3f}')
ax.set_xlabel('t')
ax.set_ylabel('y')
ax.legend()
plt.show()
```

A quick guide to the plotting code:

- `fig, ax = plt.subplots()` creates a blank figure (`fig`) with a set of axes (`ax`) to draw on.
- `ax.plot(x, y, style, label=...)` draws a line. `'k-'` means black solid line; `'o-'` means circles connected by lines.
- `ax.set_xlabel`, `ax.set_ylabel`, and `ax.legend` add labels and a legend.
- `plt.show()` displays the figure.

:::{admonition} Checkpoint
:class: tip
Look at your plot. Is Forward Euler above or below the exact solution during the first half ($0 < t < \pi$)? Look at the slope $\cos(t)$ on that interval. Can you explain why, using the fact that Euler always uses the slope at the *start* of each step?
:::

## Making the time step smaller

Our solution has the right shape, but it's visibly off. The obvious fix: take smaller steps. Let's repeat the whole process with a time step 8 times smaller.

### Set up and initialize

We use new variable names (`_small`) so we don't overwrite our first solution — we want to compare them.

```python
dt_small = np.pi / 64      # about 0.049
n_steps_small = int(round((t_end - t_start) / dt_small))
print(n_steps_small)

t_small = np.zeros(n_steps_small + 1)
y_small = np.zeros(n_steps_small + 1)

t_small[0] = t_start
y_small[0] = y0
```

This time you should see `128` steps.

### Step forward

The loop is identical — only the names changed.

```python
for n in range(n_steps_small):
    t_small[n+1] = t_small[n] + dt_small
    y_small[n+1] = y_small[n] + dt_small * dy_dt(t_small[n])
```

:::{note}
In Excel, going from 16 rows to 128 rows means dragging the formula a lot further down. Try 10,000 rows and you'll feel it. In Python, you change one number.
:::

## Comparing the two solutions

### Plot both solutions against the exact answer

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_exact, np.sin(t_exact), 'k-', label='Exact: sin(t)')
ax.plot(t, y, 'o-', label=f'dt = {dt:.3f}')
ax.plot(t_small, y_small, '.-', markersize=3, label=f'dt = {dt_small:.3f}')
ax.set_xlabel('t')
ax.set_ylabel('y')
ax.legend()
plt.show()
```

The small-step solution should sit almost on top of the exact curve.

### Plot the error

The error is the difference between the numerical and exact solutions. We take the absolute value so we only care about *how far off* we are, not in which direction.

```python
err = np.abs(y - np.sin(t))
err_small = np.abs(y_small - np.sin(t_small))

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, err, 'o-', label=f'dt = {dt:.3f}')
ax.plot(t_small, err_small, '.-', markersize=3, label=f'dt = {dt_small:.3f}')
ax.set_xlabel('t')
ax.set_ylabel('|y_euler - y_exact|')
ax.legend()
plt.show()
```

### Put a number on it

```python
max_err = err.max()
max_err_small = err_small.max()

print(f"dt = {dt:.4f}  ->  max error = {max_err:.4f}")
print(f"dt = {dt_small:.4f}  ->  max error = {max_err_small:.4f}")
print(f"dt got {dt / dt_small:.0f}x smaller")
print(f"error got {max_err / max_err_small:.1f}x smaller")
```

You should find that making $\Delta t$ **8 times smaller** makes the error about **8 times smaller**. When the error shrinks in direct proportion to $\Delta t$, we call the method **first-order accurate**. That's Forward Euler: simple and reliable, but you pay for accuracy with lots of small steps.

:::{admonition} Something sneaky
:class: warning
Look at the last point, $t = 2\pi$, in both solutions (`y[-1]` and `y_small[-1]`). Both land essentially on the exact answer, $\sin(2\pi) = 0$! That isn't because Euler is suddenly perfect — the overshoot from the first half of the curve happens to be cancelled by the undershoot in the second half, because $\cos(t)$ is symmetric.
:::

## Exercises

1. Try `dt = np.pi / 4` and `dt = np.pi / 256`. Does the "8x smaller step, 8x smaller error" pattern still hold for the ratios you pick?
2. Make a DataFrame for the small-step solution, like we did for the first one. How many rows does it have?
3. Change the ODE to $\frac{dy}{dt} = -y$ with $y(0) = 1$ (exact solution: $y = e^{-t}$). What do you need to change in `dy_dt`, and what do you need to change inside the loop?
4. **Bonus:** We wrote nearly the same code twice. Wrap the setup and the loop into a single function `forward_euler(dt)` that returns `t` and `y`. Then use it to solve with five different time steps in a few lines.