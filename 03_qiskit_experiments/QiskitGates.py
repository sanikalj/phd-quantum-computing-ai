from qiskit import QuantumCircuit
from qiskit.quantum_info import  Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc=QuantumCircuit(1)
qc.h(0)
qc.x(0)
qc.z(0)
qc.draw('mpl')
plot_bloch_multivector(Statevector.from_instruction(qc))
plt.show()