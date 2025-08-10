
##  Análisis de Circuitos Sumadores Cuánticos con Ruido en FakeVigoV2
### Objetivo del proyecto

Este proyecto tiene como finalidad analizar los principales circuitos sumadores propuestos en la literatura.
Para ello, los circuitos se han clasificado en dos categorías: Half Adder, Full Adder.

El objetivo es evaluar su desempeño en condiciones de ruido simuladas, identificando cuáles presentan un mejor comportamiento.

### Elección del backend: FakeVigoV2

Para este proyecto se seleccionó el backend **FakeVigoV2** debido a que proporciona un entorno de simulación realista, incorporando parámetros de ruido basados en datos de calibración de un dispositivo cuántico real de IBM. Esto permite evaluar el comportamiento de los circuitos sumadores bajo condiciones cercanas a la realidad, pero sin requerir acceso a hardware cuántico físico.

<table>
  <tr>    
    <th>Característica</th>
    <th>¿Incluida en FakeVigoV2?</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td>Ruido de un solo qubit</td>
    <td><div align="center">&#10003;</div></td>
    <td>Error depolarizante y relajación térmica.</td>
  </tr>
  <tr>
    <td>Ruido de dos qubits</td>
    <td><div align="center">&#10003;</div></td>
    <td>Error depolarizante seguido por relajación térmica en ambos qubits.</td>
  </tr>
  <tr>
    <td>Error de lectura</td>
    <td><div align="center">&#10003;</div></td>
    <td>Simula la probabilidad de medición incorrecta de un qubit.</td>
  </tr>
  <tr>
    <td>Simulación sin ruido disponible</td>
    <td><div align="center">&#10003;</div></td>
    <td>Usando <code>AerSimulator</code> sin parámetros de ruido para referencia.</td>
  </tr>
</table>
<hr>

Topología física de VigoV2.
Cuenta con 5 qubits. Lo que es suficiente para implementar los circuitos, tanto Half Adders como Full Adders, seleccionados.

<div align="center">
  <img width="300" height="300" alt="topologia_backend" src="https://github.com/user-attachments/assets/32a95126-823a-4312-921b-79ace1203e67" />
</div>

### Estructura del proyecto
En este repositorio encontrarás:

Una notebook de Colab con el código para ejecutar los circuitos analizados.    
En la notebook se generan:
<ul>
      <li>El circuito original.</li>
      <li>El circuito transpilado para FakeVigoV2.</li>
      <li>Gráficos de resultados con y sin ruido.</li>
</ul>
    
### Ejecución y resultados

El análisis se centra en comparar la fidelidad de salida y el comportamiento de cada circuito bajo condiciones ideales y con ruido, aprovechando las capacidades de simulación realista de FakeVigoV2.
