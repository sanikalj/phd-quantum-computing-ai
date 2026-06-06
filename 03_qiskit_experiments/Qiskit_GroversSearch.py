from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Initialize 2 Qubits and 2 Classical bits
qc = QuantumCircuit(2, 2)

# 2. STEP 1: Create equal superposition across all states (FIXED)
qc.h([0, 1])

# 3. STEP 2: The Phase Oracle (Marks the |11> state with a negative phase)
qc.cz(0, 1)

# =========================================================================
# 4. STEP 3: THE DIFFUSER BLOCK (Inversion about the Mean)
# =========================================================================
qc.h([0, 1])   # Transform back from the computational basis
qc.x([0, 1])   # Flip states to prepare for the conditional phase shift
qc.cz(0, 1)    # Apply a controlled-phase shift to invert the target state
qc.x([0, 1])   # Undo the X transformation
qc.h([0, 1])   # Return to the computational basis
# =========================================================================

# 5. STEP 4: The Measurement Layer (The 'M' blocks) (FIXED)
qc.measure([0, 1], [0, 1])

# 6. Execute local simulation
backend = AerSimulator()
job = backend.run(qc, shots=1024)
result = job.result()
count = result.get_counts()

# 7. Print the updated circuit layout and final counts matrix
print(qc)
print("\nMeasurement counts:", count)
