# 📋 Encuesta Proyecto POO  

## Autor  
**Santiago Peralta Castellanos**  

## 📝 Descripción  
Este proyecto implementa un sistema de **encuestas en Python** utilizando Programación Orientada a Objetos (POO).  
El programa permite:  
- Registrar encuestas con nombre, edad y respuestas a preguntas predefinidas.  
- Almacenar las respuestas en objetos de la clase `Encuesta`.  
- Mostrar un **resumen** de todas las encuestas realizadas.  

## 📂 Estructura del Código  
- **Clase `Encuesta`**  
  - Atributos:  
    - `preguntas`: lista de preguntas.  
    - `respuestas`: lista de respuestas del encuestado.   
  - Método:
    - `agregar_respuestas()`: registra las respuestas del usuario a las preguntas definidas.
    - `mostrar_respuestas()`: imprime en pantalla las respuestas del encuestado.
    - `resumen()`: imprime en pantalla la cantidad de preguntas registradas.  

- **Función `main()`**  
  - Define las preguntas.    
  - Crea los objetos `Encuesta`.  
  - Llama los metodos de la clase Encuesta.  

## 🚀 Ejecución  
1. Asegúrate de tener instalado **Python 3**.  
2. Guarda el archivo como `encuesta.py`.  
3. Abre la terminal en la carpeta del proyecto y ejecuta:  
   


## 🧑‍💻 Ejemplo de Uso 
  <img width="646" height="263" alt="image" src="https://github.com/user-attachments/assets/95b60999-df75-431e-b162-8bd0d8f52f8e" />
```
ncuesta proyecto final
Nombre : Santiago
Edad: 18
1: ¿Qué tema prefieres para el proyecto?: Ejemplo de tema
2: ¿Sabes trabajar en equipo?: si
3: ¿Conoces alguna librería de Python?: si
```

📋 **Enseñar las respuestas:**  
```
Resultado de la encuesta
Nombre : Santiago
Edad: 18
1: ¿Qué tema prefieres para el proyecto?: Ejemplo de tema
2: ¿Sabes trabajar en equipo?: si
3: ¿Conoces alguna librería de Python?: si
Resumen
Total de preguntas: 5
Total de respuestas: 5
```

## 📌 Notas      
- Es posible agregar más preguntas editando la lista `preguntas`.  
