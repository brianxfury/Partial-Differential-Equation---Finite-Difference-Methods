# Scientific Computing using Python 
# @Bryan Dimabayao
# Partial Differential Equation - Finite Difference Methods

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpl_toolkits.mplot3d
import scipy.sparse as sp
import scipy.sparse.linalg
import scipy.linalg as la
import dolfin
import mshr

N = 5
u0, u1 = 1, 2
dx = 1.0 / (N + 1)

A = (np.eye(N, k=-1) - 2 * np.eye(N) + np.eye(N, k=1)) / dx**2
A
#Output of Array

x = np.linspace(0, 1, N+2)
U = np.hstack([[u0], u, [u1]])
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, U)
ax.plot(x[1:-1], u, 'ks')
ax.set_xlim(0, 1)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$u(x)$", fontsize=18)
# Output and Plotting of Solution to the second-order ODE boundary value problem
