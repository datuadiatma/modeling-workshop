"""
Lotka-Volterra Predator-Prey Model — Animation
====================================================

The governing equation (taken from wiki):

    dR/dt = α·R  -  β·R·F
    dF/dt = δ·R·F -  γ·F

    R = prey (e.g., rabbits)
    F = predator (e.g., foxes)
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ============================================================
# TUNABLE PARAMETERS
# ============================================================

# --- Initial populations ---
R0 = 30.0          # initial prey population
F0 = 10.0           # initial predator population

# --- Ecological rates ---
alpha = 0.1         # prey birth rate (intrinsic growth)
beta  = 0.02        # predation rate (how effectively predators catch prey)
delta = 0.01        # predator reproduction efficiency (conversion of prey eaten → new predators)
gamma = 0.3         # predator death rate (natural mortality)

# --- Simulation settings ---
t_max  = 200.0      # total time to simulate
dt     = 0.1        # time resolution (smaller = smoother but slower)

# --- Animation settings ---
anim_speed = 5     # how many time steps to advance per frame (higher = faster)
trail_on   = True   # show phase portrait trail? (True/False)


# ============================================================
# SOLVE THE MODEL
# ============================================================

def lotka_volterra(state, t, alpha, beta, delta, gamma):
    """Right-hand side of the Lotka-Volterra ODEs."""
    R, F = state
    dRdt = alpha * R - beta * R * F
    dFdt = delta * R * F - gamma * F
    return [dRdt, dFdt]

# Time array
t = np.arange(0, t_max, dt)

# Solve
initial_state = [R0, F0]
solution = odeint(lotka_volterra, initial_state, t, args=(alpha, beta, delta, gamma))
R = solution[:, 0]   # prey over time
F = solution[:, 1]   # predator over time


# ============================================================
# ANIMATED PLOT
# ============================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Lotka-Volterra Predator–Prey Model", fontsize=14, fontweight="bold")

# --- Left panel: populations vs time ---
ax1.set_xlim(0, t_max)
ax1.set_ylim(0, max(R.max(), F.max()) * 1.15)
ax1.set_xlabel("Time")
ax1.set_ylabel("Population")
ax1.set_title("Population over Time")

line_prey,     = ax1.plot([], [], color="tab:blue",   lw=2, label=f"Prey (α={alpha}, β={beta})")
line_pred,     = ax1.plot([], [], color="tab:red",    lw=2, label=f"Predator (δ={delta}, γ={gamma})")
dot_prey,      = ax1.plot([], [], "o", color="tab:blue",  ms=6)
dot_pred,      = ax1.plot([], [], "o", color="tab:red",   ms=6)
ax1.legend(loc="upper right")

# --- Right panel: phase portrait (prey vs predator) ---
ax2.set_xlim(0, R.max() * 1.15)
ax2.set_ylim(0, F.max() * 1.15)
ax2.set_xlabel("Prey population")
ax2.set_ylabel("Predator population")
ax2.set_title("Phase Portrait")

# faint full trajectory for reference
ax2.plot(R, F, color="gray", alpha=0.15, lw=1)

line_phase,    = ax2.plot([], [], color="tab:purple", lw=1.5, alpha=0.7)
dot_phase,     = ax2.plot([], [], "o", color="tab:purple", ms=7)

# mark the equilibrium point
R_eq = gamma / delta
F_eq = alpha / beta
ax2.plot(R_eq, F_eq, "x", color="black", ms=10, mew=2, label=f"Equilibrium ({R_eq:.0f}, {F_eq:.0f})")
ax2.legend(loc="upper right")

# Time annotation
time_text = ax1.text(0.02, 0.95, "", transform=ax1.transAxes, fontsize=10,
                     verticalalignment="top", bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))


def init():
    """Clear lines for animation init."""
    for line in [line_prey, line_pred, line_phase]:
        line.set_data([], [])
    for dot in [dot_prey, dot_pred, dot_phase]:
        dot.set_data([], [])
    time_text.set_text("")
    return line_prey, line_pred, dot_prey, dot_pred, line_phase, dot_phase, time_text


def update(frame):
    """Advance the animation by one frame."""
    i = min(frame * anim_speed, len(t) - 1)

    # Time series
    line_prey.set_data(t[:i], R[:i])
    line_pred.set_data(t[:i], F[:i])
    dot_prey.set_data([t[i]], [R[i]])
    dot_pred.set_data([t[i]], [F[i]])

    # Phase portrait
    if trail_on:
        line_phase.set_data(R[:i], F[:i])
    dot_phase.set_data([R[i]], [F[i]])

    time_text.set_text(f"t = {t[i]:.1f}")

    return line_prey, line_pred, dot_prey, dot_pred, line_phase, dot_phase, time_text


n_frames = len(t) // anim_speed + 1
ani = FuncAnimation(fig, update, frames=n_frames, init_func=init,
                    interval=30, blit=True, repeat=True)

plt.tight_layout()
plt.show()
