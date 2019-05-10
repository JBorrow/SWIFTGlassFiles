import numpy as np
import matplotlib.pyplot as plt

plt.style.use("spheric_durham")

kernel = "wendland-C2"
n = 32

scheme_identifiers = [
    "gadget2",
    "minimal",
    "pressure-energy",
    "anarchy-pu",
    "gizmo-mfm",
    "gizmo-mfv"
]

scheme_names = [
    "Density-Entropy",
    "Density-Energy",
    "Pressure-Energy",
    "ANARCHY-PU",
    "SPH-ALE, FM",
    "SPH-ALE, FV"
]

scheme_alphas = [0.5, 1.0, 1.0, 1.0, 1.0, 0.5]

scheme_colours = [0, 0, 1, 3, 2, 2]

def grab_data(scheme):
    """
    Grabs the data!
    """

    data = np.genfromtxt(f"glass_{n}/{kernel}/{scheme}/energy.txt")

    return data

data = [grab_data(scheme) for scheme in scheme_identifiers]

plt.semilogy()

for name, d, c, a in zip(scheme_names, data, scheme_colours, scheme_alphas):
    plt.plot(d[:, 0], d[:, 3], color=f"C{c}", alpha=a, label=name)

plt.xlabel("Simulation time")
plt.ylabel("Kinetic energy")

plt.xlim(0, 100)
plt.ylim(1e-7, 1e-2)

plt.legend(markerfirst=False)

plt.tight_layout()

plt.savefig("energy_all.pdf")
