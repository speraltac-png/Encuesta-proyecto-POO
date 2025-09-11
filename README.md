# 📋 Encuesta Proyecto POO  

## Autor  
**Santiago Peralta Castellanos**  

## 📝 Descripción  
Este proyecto implementa un sistema de **encuestas en Python** utilizando Programación Orientada a Objetos (POO).  
El programa permite:  
- Registrar **10 encuestas** con nombre, edad y respuestas a preguntas predefinidas.  
- Almacenar las respuestas en objetos de la clase `Encuesta`.  
- Mostrar un **resumen** de todas las encuestas realizadas.  

## 📂 Estructura del Código  
- **Clase `Encuesta`**  
  - Atributos:  
    - `preguntas`: lista de preguntas.  
    - `respuestas`: lista de respuestas del encuestado.  
    - `nombre`: nombre de la persona.  
    - `edad`: edad de la persona.  
  - Método:  
    - `resumen()`: imprime en pantalla las respuestas del encuestado.  

- **Función `main()`**  
  - Define las preguntas.  
  - Solicita los datos de **10 participantes**.  
  - Registra sus respuestas en objetos `Encuesta`.  
  - Muestra un resumen de todas las encuestas al final.  

## 🚀 Ejecución  
1. Asegúrate de tener instalado **Python 3**.  
2. Guarda el archivo como `encuesta.py`.  
3. Abre la terminal en la carpeta del proyecto y ejecuta:  
   ```bash
   python encuesta.py
   ```  

## 🧑‍💻 Ejemplo de Uso  
```
Encuesta proyecto POO
En este campo escriba su nombre: Juan
En este campo escriba su edad: 21
1: ¿Qué tema prefieres para el proyecto?
Responda aquí: Inteligencia Artificial
2: ¿Sabes trabajar en equipo?
Responda aquí: Sí
3: ¿Conoces alguna librería de Python?
Responda aquí: Pandas
```

📋 **Resumen generado:**  
```
Respuestas de Juan (edad 21):
1: ¿Qué tema prefieres para el proyecto? -> Inteligencia Artificial
2: ¿Sabes trabajar en equipo? -> Sí
3: ¿Conoces alguna librería de Python? -> Pandas
```

## 📌 Notas  
- El programa está diseñado para capturar exactamente **10 encuestas**.  
- Se puede modificar el rango en el `for` para cambiar la cantidad de encuestas.  
- Es posible agregar más preguntas editando la lista `preguntas`.  
