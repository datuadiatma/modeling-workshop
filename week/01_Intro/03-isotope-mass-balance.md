# Isotope Mass Balance Box Modeling

*Numerical Modeling Workshop — Fall 2026*

## The general form

A box model treast a reservoir as a single well-mixed volume with fluxes in and out (this is the main assumption). For an isotope system we need to track two things at once: **how much** of the element is in the box, and **what its isotopic composition is**.

That gives us a pair of coupled equations.

### Mass balance

The first equation describes changes in the reservoir size $M_o$ as a balance between the input flux $F_{input}$ and the output flux(es) $F_{output}$:

$$\frac{dM_o}{dt} = F_{input} - F_{output} \tag{1}$$

This is pretty intuitive and straight forward. The box (how many moles of elements are in the ocean) grows when more comes in than goes out and *vice versa*.

### Isotopic mass balance

The second equation describes the change in the isotopic mass balance. Each flux carries its own isotopic composition, so we track the product $R_o M_o$, the isotopic composition of the reservoir times its size:

$$\frac{d(R_o M_o)}{dt} = F_{input} R_{input} - F_{output} R_{output} \tag{2}$$

:::{note}
$R$ here is a generic isotope ratio. In practice we usually work in delta notation ($\delta^{13}\mathrm{C}$, $\delta^{238}\mathrm{U}$, $\delta^{205}\mathrm{Tl}$).
:::

### Expanding with the product rule

Equation 2 as written isn't yet in a form we can hand to a numerical solver (i.e., Euler method, Runge Kutta, etc), because the left-hand side is the derivative of a *product* of two things that both change with time. Applying the product rule,

$$\frac{d(uv)}{dt} = u\frac{dv}{dt} + v\frac{du}{dt}$$

the left-hand side of Eq. 2 expands to:

$$\frac{d(R_o M_o)}{dt} = M_o \frac{dR_o}{dt} + R_o \frac{dM_o}{dt}$$

This is the key step. We now have a $dM_o/dt$ term sitting inside the isotope equation — and we already have an expression for it, namely Eq. 1. Substituting it in and rearranging gives an equation for $dR_o/dt$ alone. This will be the form of equations we will solve using Python.

:::{admonition} We'll do this on the board
:class: important
We will carry out this derivation by hand in class. We'll also derive the **steady-state** version of the equations by setting the time derivatives to zero, which is how you find the baseline conditions a model starts from and how you sanity-check a run that seems to be misbehaving.

Bring papers and pencil.
:::

## Case study: Kump & Arthur (1999)

Once the general form is in hand, we'll apply it to a real, widely-used model of the global carbon cycle: Kump & Arthur (1999), *Interpreting carbon-isotope excursions: carbonates and organic matter*.

The setup should look familiar. The amount of inorganic carbon in the ocean–atmosphere system, $M_o$, changes on multimillennial timescales primarily because of imbalances between carbon inputs from weathering ($F_w$) and metamorphism/volcanism ($F_{volc}$), and the sediment burial outputs as organic matter ($F_{b,org}$) and carbonate minerals ($F_{b,carb}$):

$$\frac{dM_o}{dt} = F_w + F_{volc} - F_{b,org} - F_{b,carb} \tag{KA-1}$$

And the isotopic mass balance, with each flux carrying its own $\delta^{13}\mathrm{C}$:

$$\frac{d(\delta_o M_o)}{dt} = F_w \delta_w + F_{volc} \delta_{volc} - F_{b,org} \delta_{org} - F_{b,carb} \delta_{carb} \tag{KA-2}$$

If you compare these to Eqs. 1 and 2 above, you can see tha they are practically the *same two equations*. One input flux is split into two (weathering and volcanism), one output flux into two (organic and carbonate burial), and $R$ is written as $\delta$. The structure is identical.

:::{admonition} In class
:class: important
We'll spend real time on this paper: expanding KA-2 with the product rule, deciding what $\delta_{org}$ should be relative to $\delta_{carb}$ (this is where the photosynthetic fractionation $\Delta_B$ enters), and working out what the model predicts when you perturb organic carbon burial. Then we'll code it up.
:::

## Take away

- Every isotope box model is two coupled ODEs: one for mass, one for isotopic mass.
- The product rule is what connects them. The isotope equation cannot be solved without the mass equation.
- Published models differ mostly in *how many* fluxes there are and *what sets* their isotopic compositions.

## References

- Kump, L.R. & Arthur, M.A., 1999. Interpreting carbon-isotope excursions: carbonates and organic matter. *Chemical Geology* 161, 181–198.