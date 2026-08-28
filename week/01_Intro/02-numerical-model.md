# What is a Numerical Model?

*Numerical Modeling Workshop — Fall 2026*

Before we dive in to the fun parts of the workshop let's spend some time to discussing some definitions.

## Two definitions of models and modeling

These two definitions capture most of what we'll do in this workshop.

> A numerical model is a mathematical description of temporal and/or spatial changes in a system.
>
> — Slingerland & Kump (2011)

The first one is an operational defintion: a model is math that tracks how something changes in time, in space, or both.

> Models are devices that mirror nature by embodying empirical knowledge in forms that permit (quantitative) inference to be derived from them.
>
> — Dutton (1987)

 The second is philosophical. A model *mirrors* nature, it is not nature. Everything it "knows" was put there by us, in the form of equations and parameter values. What we get out is inference, not observation.

:::{tip} A useful habit
 After every model run, ask *what did I assume that produced this result?* Keep track of all assumptions made in your model. If the models end up in your paper you need to outline those, either in the main manuscript, or at the very least in the supplement.

 This is a "low hanging fruit" for reviewers to criticize your manuscript.
:::

## Forward and inverse models

Within the context of numerical models and this workshop, we'll further divide numerical models into these two types:

**Forward models** go from parameters to predicted behavior:

$$
 \text{parameters} \xrightarrow{\text{model}} \text{predicted behavior/data} 
$$

We set a volcanic outgassing rate and predict how temperature changes. We prescribe the inputs and let the system evolve.

**Inverse models** the opposite, from data back to parameters:

$$
 \text{data} \xrightarrow{\text{model}} \text{inferred parameters} 
$$


We take a reconstructed temperature record and back-calculate the outgassing rate that could have produced it.

Forward models have one answer for a given set of inputs. Inverse problems in Earth science are usually *underdetermined* — many different parameter combinations can reproduce the same data equally well. That's why inverse methods tend to come with heavy statistics (Monte Carlo, Bayesian inference): often time the output isn't a number, it's a distribution (of all possible paramaters that can reproduce our data).

## Modeling in practice

Whatever the flavor, building a numerical model comes down to two steps.

**1. Abstraction.** Translate Earth system processes into mathematical equations, usually ordinary differential equations (ODEs) when the system varies only in time, or partial differential equations (PDEs) when it varies in space as well. This is the intellectual work: deciding what to include, what to lump together, and what to leave out entirely. A box model of the ocean carbon cycle is a set of ODEs precisely because we've chosen to ignore space inside each box.

**2. Solve those equations numerically.** This is the computational work.

:::{note} Important to remember
Step 1 is where the science lives. This is the hard part of modeling. Step 2 is the focus of this workshop. We will get a taste of Step 1 a little bit when we are discussing the Kump and Arthur (1999) paper, but next week and the rest of the workshop we'll focus more on how to solve ODEs.
:::

## Techniques and tools

Common numerical techniques you'll encounter:

| Technique | Typical use |
|---|---|
| Euler method | Simplest ODE solver; good for building intuition |
| Runge–Kutta | Workhorse ODE solvers, much better accuracy for the same step size |
| Monte Carlo inversion | Sampling parameter space to find what fits the data |
| Bayesian inversion | Same, but with prior knowledge and full posterior uncertainty |

And the tools people actually use: pen and paper, Excel, STELLA, MATLAB, Python, and plenty of others. All of them can solve the same equations.

### Why Python for this workshop

- **Popular** — a large community, so your question has probably already been answered somewhere.
- **Readable** — the code , by design, looks close enough to plain english and the math that you can check it against your equations.
- **Rich ecosystem** — `numpy`, `scipy`, `matplotlib`, `pandas` cover essentially everything we need.
- **Scalable** 
- **Free and open** — no license, and your collaborators and reviewers can run exactly what you ran.


## References

- Dutton, J.A., 1987. *The Ceaseless Wind: An Introduction to the Theory of Atmospheric Motion*. Dover.
- Slingerland, R. & Kump, L., 2011. *Mathematical Modeling of Earth's Dynamical Systems: A Primer*. Princeton University Press.