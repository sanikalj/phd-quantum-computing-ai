from qiskit import  QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector

qc= QuantumCircuit(1,1)
qc.h(0)
state=Statevector.from_instruction(qc)
qc.measure(0,0)
sim=Aer.get_backend('qasm_simulator')
result = sim.run(qc, shots=10).result()
print(result.get_counts())
print(state)

