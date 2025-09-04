
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

def fidelity(counts_ideal, counts_noisy):
    print(f"fidelity")
    all_keys = set(counts_ideal.keys()).union(counts_noisy.keys())
    total_ideal = sum(counts_ideal.values())
    total_noisy = sum(counts_noisy.values())
    return sum(np.sqrt(
        (counts_ideal.get(k, 0) / total_ideal) *
        (counts_noisy.get(k, 0) / total_noisy)
    ) for k in all_keys)

def success_probability(counts, expected):
    print(f"success_probability")
    total = sum(counts.values())
    return counts.get(expected, 0) / total if total > 0 else 0

def plot_comparative(counts_ideal, counts_noisy, circuit_name, circuit_description):
    try:
        print(f"plot_comparative {circuit_name} {circuit_description}")
        fig = plot_histogram([counts_ideal, counts_noisy], legend=['Ideal', 'Noisy'],
                            title=f"Comparación Sin Ruido vs Con Ruido.\nCircuit {circuit_name} Sum: {circuit_description}")
        fig.savefig(f"comparacion_ideal_vs_ruido({circuit_name})({circuit_description}).png", dpi=300, bbox_inches="tight")
        plt.close(fig)
        #display(fig)
    except Exception as e:
        print("Ocurrió un error al generar/guardar la figura:", e)
