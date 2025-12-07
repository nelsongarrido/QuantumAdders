from circuitos import nielsen_chuang2011, yamashita2008, cnotGate, toffoliGate, hadamardGate, tGate, tDagaGate
from simulador import get_FakeVigoV2_backend, setup_backends, transpile_for_noise, run_circuit, get_and_draw_circuit, render_transpiled, plot_device_topology
from metricas import fidelity, success_probability, plot_comparative

def run_adder_experiment(adderCircuit):
    fileName = f"({adderCircuit.name})({adderCircuit.description})"

    backend = get_FakeVigoV2_backend()
    sim_ideal, sim_noisy = setup_backends(backend, seed=42)
    circuit = get_and_draw_circuit(adderCircuit, draw=True)

    transpiled = transpile_for_noise(circuit, sim_noisy)
    render_transpiled(transpiled, filename= fileName)
    plot_device_topology(backend, filename= fileName)

    shots = 1024
    counts_ideal = run_circuit(sim_ideal, circuit, shots, show_plot=True, title=f"ideal {fileName}")
    counts_noisy = run_circuit(sim_noisy, transpiled, shots, show_plot=True, title=f"noisy {fileName}")

    fid = fidelity(counts_ideal, counts_noisy)
    prob = success_probability(counts_noisy, "111")

    print(f"Fidelidad: {fid:.4f}")
    print(f"Probabilidad de éxito (111): {prob:.4f}")
    plot_comparative(counts_ideal, counts_noisy, adderCircuit.name, adderCircuit.description)

def main():
    try:
        operations = [[0,0],[0,1],[1,0],[1,1]]
        for c in operations:
            print(c)
            print(f"{c[0]} + {c[1]}")
        combinaciones = [[0,0]]
        #for combo in combinaciones:
        #    adderCircuit = nielsen_chuang2011(0,0)
        #    run_adder_experiment(adderCircuit)

        # adderCircuit = nielsen_chuang2011(0,0)
        # run_adder_experiment(adderCircuit)

        adderCircuit = yamashita2008(0,0)
        run_adder_experiment(adderCircuit)

        # print("Puerta: CNOT--------------")
        # cnot = cnotGate()
        # run_adder_experiment(cnot)
        # print("------------------------")

        # print("Puerta: Toffoli--------------")
        # toffoli = toffoliGate()
        # run_adder_experiment(toffoli)
        # print("------------------------")

        # print("Puerta: Hadamard--------------")
        # hadamard = hadamardGate()
        # run_adder_experiment(hadamard)
        # print("------------------------")
        
        # print("Puerta: T--------------")
        # t = tGate()
        # run_adder_experiment(t)
        # print("------------------------")

        # print("Puerta: T Daga--------------")
        # tDaga = tDagaGate()
        # run_adder_experiment(tDaga)
        # print("------------------------")
    except Exception as e:
        print("Ocurrió un error al generar/guardar la figura:", e)

if __name__ == "__main__":
    main()


