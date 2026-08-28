# Exercise: Steady-State Isotope Mass Balance

*Numerical Modeling Workshop — Fall 2026*

## The problem

Consider a hypothetical element **X** dissolved in the global ocean. The ocean is a single well-mixed box (the main assumption of a box model) of size $M_o$, with two sources and two sinks.

**Sources**

| Source | Flux (Gmol kyr⁻¹) | $\delta_{in}$ (‰) |
|---|---|---|
| Rivers | $F_{riv} = 40$ | $\delta_{riv} = -0.30$ |
| Hydrothermal | $F_{hyd} = 10$ | $\delta_{hyd} = -0.60$ |

**Sinks**

Both sinks draw from the same seawater reservoir, but each fractionates X as it is removed. Define the fractionation factor as

$$\Delta_i = \delta_i - \delta_o$$

that is, the offset between the sink and the seawater it precipitates from.

| Sink | Flux (Gmol kyr⁻¹) | $\Delta_i$ (‰) |
|---|---|---|
| Oxic sediments | $F_{ox} = 40$ | $\Delta_{ox} = 0.00$ |
| Anoxic sediments | $F_{anox} = 10$ | $\Delta_{anox} = +0.60$ |

The reservoir size is $M_o = 19{,}000$ Gmol.

### Questions

**(a)** Confirm that the reservoir is at steady state with respect to *mass*.

**(b)** Write down the steady-state isotope mass balance and solve for $\delta_o$, the isotopic composition of seawater. What is the numerical value?

**(c)** Now suppose ocean anoxia expands, so that the anoxic sink takes 40% of the total removal instead of 20% ($F_{anox} = 20$, $F_{ox} = 30$), with the total output flux unchanged. What is the new steady-state $\delta_o$? Which direction did seawater move, and why?

**(d)** Compute the residence time of X in the ocean. Does $M_o$ appear anywhere in your answer to (b) or (c)? What does that tell you about the role of reservoir size in a steady-state calculation?

```{tip}
Work in delta notation throughout. For small fractionations the algebra of $\delta$ behaves like the algebra of $R$, which is why we can write $\delta_{sink} = \delta_o + \Delta$ and add fluxes linearly.
```

---

## Solution

:::{dropdown} Click to reveal the solution
:animate: fade-in-slide-down

....x....

::: 