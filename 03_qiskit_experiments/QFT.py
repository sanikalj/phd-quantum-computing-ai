from qiskit import  QuantumCircuit
import  numpy as np

def qft(n):
    qc=QuantumCircuit(n)
    for i in range(n):
        qc.h(i)
        for j in range(i+1,n):
            qc.cp(np.pi/2**(j-1), j,i)
    qc.reverse_bits()
    return qc
qc=qft(3)
qc.draw("mpl")
