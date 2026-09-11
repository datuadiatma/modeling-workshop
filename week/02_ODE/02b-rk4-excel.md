# Exercise 2: Runge–Kutta 4 in Excel

*Numerical Modeling Workshop — Fall 2026*

We continue with the same ODE and the same spreadsheet from Exercise 1:

$$
\frac{dy}{dt} = \cos(t), \qquad y(0) = 0, \qquad 0 \le t \le 2\pi
$$

Keep your 20 time steps ($\Delta t = 2\pi/20$). The goal is to see how much more accurate RK4 is **with the same time step** as Euler.

Recall the RK4 update:

$$
\begin{aligned}
k_1 &= f\!\left(t^{n},\; y^{n}\right) \\
k_2 &= f\!\left(t^{n} + \tfrac{\Delta t}{2},\; y^{n} + \tfrac{\Delta t}{2}\,k_1\right) \\
k_3 &= f\!\left(t^{n} + \tfrac{\Delta t}{2},\; y^{n} + \tfrac{\Delta t}{2}\,k_2\right) \\
k_4 &= f\!\left(t^{n} + \Delta t,\; y^{n} + \Delta t\,k_3\right) \\[4pt]
y^{n+1} &= y^{n} + \frac{\Delta t}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
\end{aligned}
$$

:::{note}
In our ODE, $f(t, y) = \cos(t)$ depends only on $t$, not on $y$. So when we evaluate the slopes, we only need to shift the **time**. For most real models (like box models), $f$ depends on $y$ too, and you would also compute the shifted $y$ values shown above.
:::

## Spreadsheet layout

We add new columns to the right of Exercise 1:

| Column | H | I | J | K | L | M |
|---|---|---|---|---|---|---|
| **Header** | `k1` | `k2` | `k3` | `k4` | `y_rk4` | `error_rk4` |

## Step 1: The four slopes (H–K)

Type the headers in row 1, then enter these formulas in row 2:

| Cell | Formula | Meaning |
|---|---|---|
| `H2` | `=COS(A2)` | slope at the start of the step |
| `I2` | `=COS(A2 + B2/2)` | slope at the midpoint |
| `J2` | `=COS(A2 + B2/2)` | slope at the midpoint (again) |
| `K2` | `=COS(A2 + B2)` | slope at the end of the step |

Select `H2:K2` and fill down to row 22.

:::{admonition} Check yourself
:class: dropdown
Row 2 should give `k1 = 1.0000`, `k2 = k3 ≈ 0.9877`, `k4 ≈ 0.9511`.
:::

## Step 2: The RK4 solution (L)

1. In `L2`, enter the initial value: `0`
2. In `L3`, take the RK4 step using the weighted average of the slopes:

```
   =L2 + B2/6*(H2 + 2*I2 + 2*J2 + K2)
```

3. Fill down to `L22`.

## Step 3: The RK4 error (M)

1. In `M2`: `=L2 - E2`
2. Fill down to `M22`.

:::{tip}
The RK4 errors are tiny. Format columns F and M as **Scientific** (Home → Number Format) so you can actually compare them.
:::

## Step 4: Plot

1. Add `y_rk4` to your chart from Exercise 1. Can you tell it apart from the exact solution?
2. Make a second chart: plot the **absolute** error of Euler and RK4 against $t$. (Use `=ABS(F2)` and `=ABS(M2)` in new columns if needed.) Set the y-axis to a **logarithmic scale** (Format Axis → Logarithmic scale).

## Questions

1. What is the largest error for Euler? For RK4? Roughly how many times smaller is the RK4 error?
2. Why do $k_2$ and $k_3$ come out identical in this exercise? Would they be identical for $\dfrac{dy}{dt} = -y$?
3. Change to 40 steps (update `A3` to `=A2 + 2*PI()/40` and extend all columns to row 42). By what factor did the Euler error shrink? The RK4 error? Compare with the expected factors of 2 and 16.
4. RK4 does four slope calculations per step, Euler does one. For a fair comparison, run Euler with 80 steps (80 slope calculations) and compare it with RK4 at 20 steps (also 80). Which is more accurate?
5. Given your answers, why do modern solvers use Runge–Kutta methods instead of simply making $\Delta t$ very small with Euler?

:::{admonition} Looking ahead
:class: dropdown
In Python, all of this becomes one line with `scipy.integrate.solve_ivp`, which uses an adaptive Runge–Kutta method (`RK45`) by default. It picks $\Delta t$ for you by estimating its own error at every step.
:::