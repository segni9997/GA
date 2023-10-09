import numpy as np
import matplotlib as mp
from ypstruct import structure
import Ga as g


# sphere function
def sphere(x):
    return sum(x ** 2)


# poroblem defintion
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA Paramaters
params = structure()
params.maxit = 100
params.pop = 20

# Run GA
out = g.run(problem, params)

# Results
