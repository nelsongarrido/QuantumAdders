
# Evaluación de Circuitos Cuánticos en Ambientes Ruidosos

Este proyecto estudia algoritmos sumadores cuánticos ejecutados en simuladores con ruido, específicamente sobre la arquitectura **IBM VigoV2**. Se analizan distintas métricas para evaluar el impacto del ruido en la fidelidad y precisión de los resultados cuánticos.

---

## MÉTRICAS RECOMENDADAS PARA AMBIENTES CON RUIDO

### 1. Fidelidad de salida (Output Fidelity)
- **¿Qué es?** Mide cuán parecida es la distribución de salida ruidosa a la distribución ideal (sin ruido).
- **Cómo se mide:** Se calcula la *fidelity* entre el histograma ideal y el histograma ruidoso.
- **Relevancia:** Refleja directamente cómo el ruido afecta la confiabilidad del resultado del sumador.

---

### 2. Tasa de éxito / Probabilidad de acierto (Success Probability)
- **¿Qué es?** Proporción de ejecuciones que resultan en el resultado correcto.
- **Cómo se mide:** Cuántas veces aparece el resultado correcto sobre el total de *shots*.
- **Relevancia:** Útil si se espera un único resultado (por ejemplo, suma exacta como `2 + 3 = 5 → 101`).

---

### 3. Distribución de errores
- **¿Qué es?** Observa qué estados incorrectos son más comunes.
- **Cómo se mide:** Se identifican los estados más frecuentes distintos del correcto.
- **Relevancia:** Puede revelar si hay errores sistemáticos (estructurales) o aleatorios (aleatoriedad del ruido).

---

### 5. Variabilidad entre ejecuciones
- **¿Qué es?** Evalúa la consistencia del circuito ejecutado varias veces bajo las mismas condiciones.
- **Cómo se mide:** Se corre el mismo circuito múltiples veces y se calcula la varianza de los histogramas.
- **Relevancia:** Evalúa la estabilidad y confiabilidad del comportamiento cuántico.

---

### 6. Comparación entre distintas topologías
- **¿Qué es?** Se prueba el mismo circuito sobre diferentes conectividades físicas (emuladores o dispositivos).
- **Cómo se mide:** Se transpila para cada topología y se comparan métricas como fidelidad y tasa de error.
- **Relevancia:** Ayuda a determinar si un diseño es más robusto ante restricciones físicas del hardware.

---

## Estructura sugerida para artículo académico

### 1. Introducción
- Contexto de computación cuántica ruidosa
- Motivación de evaluar sumadores en simuladores IBM

### 2. Diseño de circuitos sumadores
- Tipos implementados: Ripple-Carry, Carry Lookahead, Cuántico Modular

### 3. Evaluación en ambiente ideal
- Métricas: coste cuántico, profundidad, delay

### 4. Evaluación en ambiente ruidoso
- Descripción del simulador con ruido (IBM VigoV2)
- Fidelidad, tasa de error, distribución de errores, robustez

### 5. Discusión
- ¿Qué circuitos son más robustos frente al ruido?
- ¿Qué tipo de errores son más comunes?

### 6. Conclusiones y trabajo futuro
- Posibles optimizaciones
- Mitigación de errores
- Ejecución en hardware real (no emulado)

---
## Circuitos Sumadores Cuánticos Analizados

Este repositorio se basa en el artículo:

> F. Orts et al. (2020). *A review on reversible quantum adders*. Journal of Network and Computer Applications, 170, 102810.  
> [https://doi.org/10.1016/j.jnca.2020.102810](https://doi.org/10.1016/j.jnca.2020.102810)

El artículo presenta una exhaustiva revisión y comparación de **sumadores cuánticos reversibles**, divididos por tipo de arquitectura. A continuación se listan todos los circuitos descritos, con referencias a sus autores.

---

### Half Adders (Sumadores de medio bit)

| Circuito                        | Autor(es)                     | Año  |
|--------------------------------|-------------------------------|------|
| Toffoli + CNOT (no completo)   | Basado en Nielsen & Chuang   | 2011 |
| Peres Gate HA                  | Hung et al.                   | 2006 |
| Yamashita HA                   | Yamashita et al.             | 2008 |
| RSG Gate HA/Subtractor         | Sarma & Jain                 | 2018 |
| Fault-Tolerant HA/Subtractor  | Kaur & Dhaliwal              | 2012 |
| Fault-Tolerant HA/Subtractor  | Balaji et al.                | 2018 |

---

### Full Adders (Sumadores completos)

| Circuito                          | Autor(es)                          | Año  |
|----------------------------------|------------------------------------|------|
| Peres × 2                        | Bhagyalakshmi & Venkatesha         | 2010 |
| Fredkin FA (mejorado por Bruce)  | Khlopotine, Bruce et al.           | 2002 |
| MAJ + UMA                        | Cuccaro et al.                     | 2004 |
| Cout-preserving FA               | Wang et al.                        | 2016 |
| Controlled-V FA                  | Maslov et al.                      | 2008 |
| RSG Gate FA/Subtractor           | Sarma & Jain                       | 2018 |
| BKG, IG, PCTG FA (comparativa)   | Batish et al.                      | 2018 |
| Fault-Tolerant FAs               | Zhou, Mitra, Islam, Dastan et al.  | 2009–2014 |

---

### Ripple-Carry Adders (RCA)

| Circuito                          | Autor(es)                   | Año  |
|----------------------------------|-----------------------------|------|
| VBE Adder                        | Vedral, Barenco, Ekert      | 1996 |
| CDKM RCA                         | Cuccaro et al.              | 2004 |
| Takahashi RCA (dos variantes)    | Takahashi et al.            | 2005/2010 |
| RCA con TR Gates                 | Thapliyal & Ranganathan     | 2011/2013 |
| Peres + TR RCA                   | Mohammadi et al.            | 2020 |
| Fault-Tolerant RCA               | Gidney                     | 2018 |
| RCA con 4N ancillas              | Nagamani et al.             | 2014 |

---

### Carry-Lookahead Adders (CLA)

| Circuito                          | Autor(es)                   | Año  |
|----------------------------------|-----------------------------|------|
| Log-depth CLA                    | Draper et al.               | 2004 |
| Optimized CLA                    | Thapliyal et al.            | 2013 |
| CLA con RPA Gate                 | Lisa & Babu                 | 2015 |
| Dos versiones CLA                | Rahmati et al.              | 2017 |
| FT CLA (T-count optimized)       | Thapliyal et al.            | 2020 |

---



