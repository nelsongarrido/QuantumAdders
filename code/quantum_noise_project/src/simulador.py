
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_gate_map
from qiskit_ibm_runtime.fake_provider import FakeVigoV2
from IPython.display import display

from qiskit import QuantumCircuit
from circuitos import CircuitResult

import os
import time
import matplotlib
matplotlib.use("Agg")      
import matplotlib.pyplot as plt 

def get_FakeVigoV2_backend():
    return FakeVigoV2()

def setup_backends(device_backend, seed=None):
    sim_ideal = AerSimulator(seed_simulator=seed)
    sim_noisy = AerSimulator.from_backend(device_backend)
    if seed:
        sim_noisy.set_options(seed_simulator=seed)
    return sim_ideal, sim_noisy

def transpile_for_noise(circuit, backend):
    print(f"transpile_for_noise")
    return transpile(circuit, backend)

def run_circuit(simulator, circuit, shots=1024, show_plot=False, title=""):
    os.environ["MPLBACKEND"] = "Agg"   
    print(f"run_circuit")
    #result = simulator.run(circuit, shots=shots).result()
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    print(f"Job finalizado con status: {job.status().name}")
    print(f"Result: {result}")    
    counts = result.get_counts()

    if show_plot:
        fig = plot_histogram(counts, title=title)
        fig.savefig(f"{title.replace(' ', '_')}.png", dpi=300)
        plt.close(fig)
    return counts



def run_job_circuit(simulator, circuit, shots=1024, show_plot=False, title="", wait_time=0.5, max_retries=100):
    print("run_circuit")
    
    job = simulator.run(circuit, shots=shots)
    
    # Esperar hasta que el job esté terminado o se alcance el máximo de reintentos
    retries = 0
    while not job.status().name == "DONE":
        print(f"Job status: {job.status().name} (esperando...)")
        time.sleep(wait_time)
        retries += 1
        if retries >= max_retries:
            raise TimeoutError("El job no terminó en el tiempo esperado.")
    
    # Una vez completado, obtener el resultado
    result = job.result()
    print(f"Job finalizado con status: {job.status().name}")
    print(f"Result: {result}")
    
    counts = result.get_counts()
    
    if show_plot:
        fig = plot_histogram(counts, title=title)
        fig.savefig(f"{title.replace(' ', '_')}.png", dpi=300)
        plt.close('all')
    
    return counts


def get_and_draw_circuit(circuit: CircuitResult | None = None, qubits: int = 3, draw: bool = True) -> QuantumCircuit:
    if draw:
        fig = circuit.adderCircuit.draw("mpl")
        #display(fig)
        fig.savefig(f"circuito_original({circuit.name})({circuit.description}).png", dpi=300, bbox_inches="tight")
        plt.close(fig)

    return circuit.adderCircuit

def render_transpiled(transpiled_circuit: QuantumCircuit, filename=""):
    print(f"render_transpiled")
    fig = transpiled_circuit.draw("mpl", style="iqp"); #display(fig)
    fig.savefig(f"circuito_transpilado{filename}.png", dpi=300, bbox_inches="tight"); plt.close(fig)

def plot_device_topology(device_backend, filename=""):
    print(f"plot_device_topology")
    fig = plot_gate_map(device_backend); #display(fig)
    fig.savefig(f"topologia_backend({filename}).png", dpi=300, bbox_inches="tight"); plt.close(fig)