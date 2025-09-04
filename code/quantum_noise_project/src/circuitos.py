from qiskit import QuantumCircuit


class CircuitResult:
    def __init__(self, circuit, name, description):
        self.adderCircuit = circuit
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<CircuitResult name={self.name}, description={self.description}>"



def nielsen_chuang2011(val0=0, val1=0):
    circ = QuantumCircuit(3)

    # Inicializar qubit 0
    if val0 == 1:
        circ.x(0)

    # Inicializar qubit 1
    if val1 == 1:
        circ.x(1)

    circ.barrier()
    circ.ccx(0, 1, 2)
    circ.cx(0, 1)
    circ.measure_all()

    # Name and Description
    name = "nielsen and chuang(2011)"
    description = f"{val0}+{val1}"

    return CircuitResult(circ, name, description)

def yamashita2008():
    circ = QuantumCircuit(3)
    circ.x(0)
    circ.x(1)
    circ.barrier()
    circ.h(2)
    circ.cx(1, 2)
    circ.t(1)
    circ.tdg(2)
    circ.cx(1, 2)
    circ.tdg(1)
    circ.h(2)
    circ.barrier()
    circ.cx(0, 1)
    circ.barrier()
    circ.t(1)
    circ.h(2)
    circ.cx(1, 2)
    circ.tdg(1)
    circ.t(2)
    circ.cx(1, 2)
    circ.h(2)
    circ.barrier()
    circ.t(0)
    circ.h(2)
    circ.cx(0, 2)
    circ.tdg(0)
    circ.t(2)
    circ.cx(0, 2)
    circ.h(2)
    circ.barrier()
    circ.cx(2, 0)
    circ.measure_all()
    return circ
