### Yamashita et al. (2008) 
**Source**

Yamashita, S., Minato, S. -i., & Miller, D. M. (2008). DDMF: An Efficient Decision Diagram Structure for Design Verification of Quantum Circuits under a Practical Restriction. IEICE Transactions on 
Fundamentals of Electronics, Communications and Computer Sciences, E91-A(12), 3793–3802. https://doi.org/10.1093/ietfec/e91-a.12.3793 

<table>
   <tr>
    <th colspan="2">Theoretical diagram</th>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img width="400" alt="Captura de pantalla 2025-08-10 182908" src="https://github.com/user-attachments/assets/ac2c5a92-2e92-4fc4-bba1-3db1625f6304" />
    </td>
  </tr>
  
  <tr>
    <th>IBM Composer implementation</th>
    <th>Transpiled Circuit on FakeVigoV2</th>
  </tr>
  <tr>
    <td align="center">
      <img width="1980" height="909" alt="circuito_original(1)" src="https://github.com/user-attachments/assets/39a50dcc-8cfc-4b41-914e-e40391a42a7f" />
    </td>
    <td align="center">
      <img width="5094" height="942" alt="circuito_transpilado(1)" src="https://github.com/user-attachments/assets/dd8ae414-9d5c-42e9-b234-7c992c33e4bc" />
    </td>
  </tr>

  <tr>    
    <th>Execution Results — Noise-Free Baseline</th>
    <th>Execution Results — With Noise</th>
  </tr>
  <tr>
    <td align="center">
      <img width="1890" height="1406" alt="ejecucion_sin_ruido(1)" src="https://github.com/user-attachments/assets/9d30cf07-81e0-4e0d-9ed2-cc0f1419db7d" />
    </td>
    <td align="center">
      <img width="1890" height="1406" alt="ejecucion_con_ruido(1)" src="https://github.com/user-attachments/assets/1fc713aa-f941-44e3-a5bf-dedda0821ce6" />
    </td>
  </tr>
</table>

<table>
  <tr>
    <th>Quantum Cost</th>
    <th>Delay</th>
    <th>Amount of Qubits</th>
    <th>Garbage Output</th>
  </tr>
  <tr>
    <td>22</td>
    <td>19</td>
    <td>3</td>
    <td>0</td>
  </tr>
  </table>
 <hr> 
 
