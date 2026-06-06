from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc= QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
#qc.draw()
state=Statevector.from_instruction(qc)
print(state)
sim = Aer.get_backend('qasm_simulator')
result = sim.run(qc.measure_all(inplace=False), shots=1000).result()
print(result.get_counts())
qc.draw('mpl')
plot_bloch_multivector(Statevector.from_instruction(qc))
plt.show()



