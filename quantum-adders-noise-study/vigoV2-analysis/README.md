
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

### 4. Profundidad efectiva y decoherencia
- **¿Qué es?** Tiempo de ejecución del circuito en relación a los tiempos de decoherencia del hardware.
- **Cómo se mide:** Se analiza la profundidad del circuito y la cantidad de compuertas multi-qubit (como CNOTs).
- **Relevancia:** Permite inferir la susceptibilidad del circuito al ruido temporal.

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

> 💡 *Este repositorio está diseñado como base experimental para el análisis de algoritmos cuánticos bajo condiciones realistas usando Qiskit y backends de IBM Quantum.*


