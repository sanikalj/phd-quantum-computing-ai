from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np

qc= QuantumCircuit(1)
qc.h(0)
qc.draw('mpl')
state=Statevector.from_instruction(qc)
print(state)
plot_bloch_multivector(state)
plt.show()
