# Exercise 1: Solve an ODE in Excel

*Numerical Modeling Workshop — Fall 2026*

We will solve a simple ODE step by step in Excel using the Forward Euler method:

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

## Spreadsheet layout

By the end, your sheet will look like this (row 1 holds the headers):

| Column | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| **Header** | `t` | `dt` | `cos(t)` | `y_euler` | `y_exact` | `error` |

## Step 1: Time column (A)

We will use $N = 21$ points between $0$ and $2\pi$, which gives 20 steps of equal size.

1. Type `t` in `A1`.
2. In `A2`, enter the starting time: `0`
3. In `A3`, add one time step to the row above:

   ```
   =A2 + 2*PI()/20
   ```

4. Fill `A3` down to `A22`. The last value should be $2\pi \approx 6.2832$.

:::{tip}
Excel writes $\pi$ as `PI()`. If your Excel uses a comma as the decimal separator (common in European and Indonesian settings), separate function arguments with `;` instead of `,`.
:::

## Step 2: Time step column (B)

1. Type `dt` in `B1`.
2. In `B3`, compute the difference between this time and the previous one:

   ```
   =A3 - A2
   ```

3. Fill `B3` down to `B22`.
4. Row 2 has no previous time. Since all our steps are equal, copy the same value into `B2`:

   ```
   =B3
   ```

:::{note}
Computing $\Delta t$ from the time column (rather than typing a constant) means your spreadsheet still works if you later use unequal time steps.
:::

## Step 3: Right-hand side of the ODE (C)

1. Type `cos(t)` in `C1`.
2. In `C2`:

   ```
   =COS(A2)
   ```

3. Fill down to `C22`.

This column is the slope $dy/dt$ at each time.

## Step 4: Initial value (D)

1. Type `y_euler` in `D1`.
2. In `D2`, enter the initial value $y^{1} = 0$:

   ```
   0
   ```

## Step 5: Solve the ODE (D)

Now apply Forward Euler: the new value equals the old value plus (time step × slope at the old time).

1. In `D3`:

   ```
   =D2 + B2*C2
   ```

2. Fill down to `D22`.

That's it. Column D is your numerical solution.

:::{admonition} Check yourself
:class: dropdown
Your value in `D3` should be about `0.3142`, which is just $\Delta t \times \cos(0) = \Delta t$.
:::

## Step 6: Plot the solution

1. Select columns A and D.
2. Insert a **scatter chart** (with lines and markers).
3. Add a title, axis labels ($t$ and $y$), and a legend.

## Step 7: Compare with the exact solution (E, F)

1. Type `y_exact` in `E1`. What function has $\cos(t)$ as its derivative and equals 0 at $t = 0$? Put its formula in `E2` and fill down.

:::{admonition} Hint
:class: dropdown
$\dfrac{d}{dt}\sin(t) = \cos(t)$ and $\sin(0) = 0$, so in `E2` use `=SIN(A2)`.
:::

2. Type `error` in `F1`. In `F2`, compute `=D2 - E2` and fill down.
3. Add the exact solution to your chart as a second series.

## Questions

1. Are the numerical and exact solutions the same? Describe how they differ.
2. Is the numerical solution too high or too low between $t = 0$ and $t = \pi$? Look at the slope Euler uses during each step, and explain why.
3. At which $t$ is the error largest? What is its value, and how does it compare to $\Delta t$?
4. Look at the error at $t = 2\pi$. It is (nearly) zero. Does this mean Euler is accurate here? Why might the errors cancel out?
5. Change the number of steps from 20 to 40. Update the formula in `A3` to `=A2 + 2*PI()/40` and extend all columns down to row 42. What happens to the largest error? Try 80. What pattern do you see?
6. How else could you improve the solution *without* making $\Delta t$ smaller? (Hint: Euler only uses the slope at the *start* of each step.)

:::{admonition} Bonus: a better slope
:class: dropdown
Instead of the slope at the start of the step, use the average of the slopes at the start and end:

$$
y^{n+1} = y^{n} + \Delta t \cdot \frac{\cos(t^{n}) + \cos(t^{n+1})}{2}
$$

Add a column `G` called `y_improved`. Enter `0` in `G2`, then in `G3` use `=G2 + B2*(C2 + C3)/2`. Fill down, add it to your chart, and compare its error with Euler's at the same $\Delta t$.

This is a simple **Runge–Kutta** method (Heun's method). We will build the more powerful RK4 next.
:::