
##  Análisis de Circuitos Sumadores Cuánticos con Ruido en FakeVigoV2
### Objetivo del proyecto

Este proyecto tiene como finalidad analizar los principales circuitos sumadores propuestos en la literatura.
Para ello, los circuitos se han clasificado en dos categorías: Half Adder, Full Adder.

El objetivo es evaluar su desempeño en condiciones de ruido simuladas, identificando cuáles presentan un mejor comportamiento.

### Elección del backend: FakeVigoV2
<table>
  <tr>    
    <th>Description</th>
    <th>Quantum Cost</th>
    <th>Delay</th>
  </tr>
  <tr>
    <td>Pauli-X</td>
    <td>1</td>
    <td>1</td>
  </tr>
    <tr>
    <td>CNOT</td>
    <td>1</td>
    <td>1</td>
  </tr>
  </table>
 <hr> 

### Controlled-V gate

**IBM implementation**

<img width="256" alt="IBM implementation" src="https://github.com/nelsongarrido/quantumAdders-/assets/6036814/10565829-55cd-4420-9d32-344eba7a12ac">
