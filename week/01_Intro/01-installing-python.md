# Installing Python

*Numerical Modeling Workshop — Fall 2026*

There are many ways to install Python, and honestly, that's part of what makes getting started confusing. You'll google around and find people telling you to use `pyenv`, `uv`, `homebrew`, the official installer from python.org, or one of the conda-based distributions. They're all valid. But if you're new to this, having too many options is worse than having one, so let me just tell you what to do ([This is an xkcd comic on this very topic](https://xkcd.com/1987/)).

I recommend *[Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))*. You can skip to the section on [why Anaconda](#why-anaconda-or-miniconda) if you want the reasoning, or follow the step-by-step for your operating system below.

Unless you are experienced with Python installations (i.e. you have done this before), please follow these instructions carefully.

:::{warning} What to do if you **already** have python installed on your laptop
**If you already have Anaconda, Conda, or Miniconda installed from a previous experience:**

You can keep your installation if it works for you. If you’d prefer to start fresh, **uninstall Anaconda first** and follow the instructions below.
:::

::::{tab-set}
:::{tab-item} On Windows

Python does not come preinstalled on Windows.

1. Go to [anaconda.com/download](https://www.anaconda.com/download). You'll be asked to register with an email address. Do that and you'll get sent to the download page. If you don't want to register with an email, you can click the skip registration link at the bottom, or use this [link](https://www.anaconda.com/download/success?reg=skipped)
2. Click the Windows 64-bit installer. It's a `.exe` file, around 1 GB.
3. Double-click the installer once it finishes downloading. Click through the welcome screen.
4. Accept the license agreement.
5. When asked who to install for, pick **Just Me**. This is the recommended option unless you have a specific reason otherwise.
6. Pick an install location. The default is fine.
7. On the "Advanced Options" screen, leave **Add Anaconda to PATH** unchecked. This is the default and it's the right choice. Leave **Register Anaconda as the default Python** checked.
8. Click Install. This takes a few minutes.
9. When it finishes, click Next, then Finish. You can skip the promo pages that pop up.

To verify it worked, open the **Anaconda Prompt** from the Start menu (search for it). You should see `(base)` at the start of your prompt. Type `conda list` and hit enter. If you see a long list of packages, you're set.

The reason we don't add Anaconda to your system PATH is that it can conflict with other Python installations you might already have or install later. The Anaconda Prompt handles all of that for you.
:::

:::{tab-item} On MacOS

macOS comes with Python preinstalled, but don't use it. That Python belongs to your operating system, and if you start pip-installing packages into it or messing with versions, you can break things you didn't know depended on it. Trust me on this one. Install Anaconda alongside it.

Before you download, check your Mac's chip. Click the Apple menu → About This Mac. You'll see either "Apple M1/M2/M3/M4" (Apple Silicon) or "Intel." This matters for step 2.

1. Go to [anaconda.com/download](https://www.anaconda.com/download). Register with an email, then you'll get to the download page. If you don't want to register with an email, you can click the skip registration link at the bottom, or use this [link](https://www.anaconda.com/download/success?reg=skipped)
2. Pick your installer:
    * **Apple Silicon Mac**: Choose the **64-Bit (Apple Silicon) Graphical Installer**. This runs natively and is much faster.
    * **Intel Mac**: Anaconda no longer builds new installers for Intel Macs as of August 2025. You have two options: use an archived installer from [repo.anaconda.com/archive](https://repo.anaconda.com/archive/), or skip Anaconda and install Miniforge instead (see the Miniforge section below).
3. Once downloaded, double-click the `.pkg` file to open the installer.
4. Click Continue through the welcome and read-me screens, then Agree to the license.
5. On the destination screen, the default location (`/opt/anaconda3`) is fine. Click Continue, then Install. You'll need to enter your Mac password.
6. Wait for it to finish. When you see "The installation was successful," click Close.
7. Open the Terminal app (Cmd+Space, type "Terminal"). You should see `(base)` at the start of your prompt, which means conda is active.
8. Type `conda list` and hit enter. A long list of packages should show up.

If you don't see `(base)` in your terminal, quit and reopen Terminal, or run `source ~/.zshrc`. If that still doesn't work, you probably need to initialize conda manually:

```bash
source /opt/anaconda3/bin/activate
conda init zsh
```
:::


:::{tab-item} On Linux

Most Linux distributions come with Python preinstalled, but as with macOS, don't touch it. Install Anaconda alongside.

1. Go to [anaconda.com/download](https://www.anaconda.com/download) and grab the 64-bit Linux installer. It's a `.sh` script.
2. Open a terminal and navigate to where you downloaded it (probably `~/Downloads`).
3. Run the installer: (Replace `2025.XX` with whatever version you downloaded.)
```bash
bash Anaconda3-2025.XX-Linux-x86_64.sh
```
4. Press Enter to review the license, then type `yes` to accept.
5. Press Enter to accept the default install location, or type a different path.
6. When it asks whether to initialize Anaconda by running `conda init`, type `yes`. This is important.
7. Close and reopen your terminal.
8. You should see `(base)` at the start of your prompt. Run `conda list` to verify.
:::
::::

Here is a screen recording of Anaconda installation on a Windows machine. MacOs should be somewhat similar.

<iframe width="939" height="528" src="https://www.youtube.com/embed/sEi4pRvq8eE" title="Python Anaconda Installation Windows" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

If you can follow the instructions or video shown above then you are good! The goal for this week is simply having Python / Anaconda installed on your machne. We will go over various ways to run a Python program in Week#2.

## Why Anaconda or Miniconda

Anaconda and Miniconda are [Python distributions](https://wiki.python.org/moin/PythonDistributions.html) made by the same company (Anaconda Inc.). They both give you the `conda` package manager, which lets you create isolated environments so different projects can have different versions of Python and different sets of packages without stepping on each other.

The difference between them:

* **Anaconda** comes bundled with a few hundred scientific Python packages preinstalled (numpy, pandas, matplotlib, scipy, jupyter, spyder, and a lot more). It's big, around 3 GB, but you get everything you need out of the box. It also comes with the Anaconda Navigator, a graphical interface for managing environments and launching apps.
* **Miniconda** is the same thing but stripped down. Just Python and conda. No preinstalled packages, no Navigator. Much smaller, around 400 MB. You install what you need as you go.

:::{note} My setup
:class: dropdown
I personally use the [Miniforge](https://github.com/conda-forge/miniforge) python distribution, which is a version of stripped down Anaconda that defaults to the community-maintained [conda-forge](https://conda-forge.org/) channel instead of the Anaconda's default channel (i.e., I'm installing Python libraries from a server maintained by volunteers, instead of Continuum Inc., the parent company of Anaconda and Miniconda). 

The main reason I choose this option is because I don't need the bells and whistles of Anaconda and I'm comfortable doing everything from the terminal. If you're new to Python scientific programming, then I'd recommend Anaconda. You will have everything you need on day one, and you can use the graphical Navigator to launch things if the terminal feels intimidating. Nothing wrong with that.

You can always switch to Miniconda or Miniforge later once you know what you actually use.
:::


---

<span style="font-size: 85%;">
Some parts of this site is taken from CC-BY 4.0 content written by <a href="https://trchudley.github.io/geospatial-scientific-computing/week/01/installing-python/">Tom Chudley</a> and <a href="https://fabienmaussion.info/climate_risks/ready/01-installation.html">Fabien Maussion</a>.
</span>