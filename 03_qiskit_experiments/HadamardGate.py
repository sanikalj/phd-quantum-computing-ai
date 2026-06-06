from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc=QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])
backend=AerSimulator()

job=backend.run(qc,shots=1024)
result=job.result()

count= result.get_counts()
print(qc)
print("Measurement counts", count)