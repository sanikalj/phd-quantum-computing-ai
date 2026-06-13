import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# Step 1: Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Step 2: Put qubit 0 into a 50/50 superposition
qc.h(0)

# Step 3: Entangle qubit 0 and qubit 1 using a CNOT gate
qc.cx(0, 1)

# Step 4: Capture the true quantum statevector
state = Statevector.from_instruction(qc)

# Print the final vector probabilities
print("Quantum State Vector:\n", state.data)

