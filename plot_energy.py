import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("energy.txt")

plt.semilogy(data[10:, 0], data[10:, 3])

plt.xlabel("Simulation time")
plt.ylabel("Kinetic energy")

plt.tight_layout()

plt.savefig("energy.pdf")
