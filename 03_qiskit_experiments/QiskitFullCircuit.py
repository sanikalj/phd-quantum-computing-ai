from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import Aer
import matplotlib.pyplot as plt


qc= QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])


sim = Aer.get_backend('qasm_simulator')
result = sim.run(qc, shots=1000).result()
counts = result.get_counts()
print(counts)
qc.draw('mpl')
plt.show()