# Ordinary Differential Equations
Week 2 provides an overview on how to solve a system of Ordinary Differential Equations using the forward Euler method.

The main paper reference for this week is still [Kump and Arthur (1999)](../../_assets/KumpArthur1999.pdf). We will spend some time at the begining of our workshop discussing the paper in a little bit more details. One of the things I would like to highlight during the paper discussion is the similarity between the general form of ODE equations we discussed last week and the equations shown in the paper. However, if you look at their equations more closely there are some "peculiarities". The first one is their steady state equations, (**Eq. 4**). It looks a bit different from the general form that we derrived in the class last week. See if you can derive **Eq.4** from the techniques and approaches we discussed last week. The second interesting aspect of their sets of ODEs is the fact they put weathering of silicate rocks (`Fwsil`) as a sink, instead of a source (**Eq. 13**). I would recommend paying attention to their argument, see if you can understand and follow their arguments from geologic persepective and how this can be valid mathematically.

Second, we will go over some numerical techniques that can be used to solve systems of Ordinary Differential Equations (ODEs) which include `forward Euler` or `Euler Method`, `backward euler`, and `Runge Kutta`. We will work through some excel-based exercises, and if time permits some hands-on python exercise.

:::{tip} Learning Objectives
After this session, you should be able to:
 - Derive Kump and Arthur (1999) canonical isotope mass balance equations.
 - Solve differential equations using forward euler and Runge-Kutta in excel

_Optional, if time permits:_
 - Run Python on your local machine.
 - Use Jupyter Notebooks to display and run Python code.
 - Write a simple ODE solver program in Python.
:::

---

## Additional resources
 - [Libre Text Chapter on Forward Euler](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_(Brorson)/02%3A_Forward_Euler_method)
 - Chapter 3 of [Slingerland and Kump's Modeling Textbook](https://press.princeton.edu/books/paperback/9780691145143/mathematical-modeling-of-earths-dynamical-systems) [(access via FSU Library)](https://fsu-flvc.primo.exlibrisgroup.com/view/action/uresolver.do?operation=resolveService&package_service_id=21072912220006576&institutionId=6576&customerId=6560&VE=true)