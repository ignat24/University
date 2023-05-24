import numpy as np
from latexifier import latexify
from IPython.display import Latex, display



MM = np.arange(1,13).reshape(3,4)

converted = latexify(MM, newline=True, arraytype="Bmatrix")

print("Showing converted LaTeX string:\n")
print(converted)

