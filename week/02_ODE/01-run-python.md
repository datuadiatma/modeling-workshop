# Running a Python Program

:::{danger} Come again later!
:class: dropdown
Content is under construction, check again in a few days.
:::

Once you have Python installed, there are a few different ways to actually run code. They're all doing the same thing under the hood, but they feel very different to work with.

**The REPL.** Open a terminal (or Anaconda Prompt on Windows), type `python`, and hit enter. You'll get a prompt where you can type Python code one line at a time and see the result immediately. Great for quick calculations, testing a one-liner, or checking what a function does. Not great for writing anything longer than a few lines.
```bash
(base) datuadiatma@Datu-iMac ~ % python                  
Python 3.12.10 | packaged by conda-forge | (main, Apr 10 2025, 22:19:24) [Clang 18.1.8 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "Datu"
>>> print(f"hello {name}") 
hello Datu
>>> x = 10
>>> y = 3
>>> print(x+y)
13
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
```

**Running a script from the terminal.** Write your code in a `.py` file using any text editor, then run it with `python myscript.py`. This is how most "real" Python programs get run in the wild. Good for anything you want to run repeatedly or share.

**Spyder.** A dedicated Python IDE that comes bundled with Anaconda. It has an editor, a REPL, a variable inspector, and a plot window all in one place. If you're coming from MATLAB, Spyder will feel familiar. It's a solid choice if you want a graphical environment without a lot of setup.

**Jupyter Notebook.** This is my favorite for scientific work, and it's what I'll be using for most of the tutorials in this series. Jupyter lets you mix code, output (including plots), and markdown text in a single document. You can run code in small chunks called cells and see the results right below each one. It's perfect for exploratory analysis, working through a modeling problem step by step, or writing up something you want to share with a colleague. Both Anaconda and Miniforge give you access to Jupyter, either through the Navigator or by running `jupyter notebook` in the terminal.

**VS Code.** Not covered here, but worth mentioning. VS Code is a general-purpose code editor with excellent Python support and native Jupyter notebook integration. Once you're comfortable with Python, I'd suggest giving it a try. It's what I use day to day.