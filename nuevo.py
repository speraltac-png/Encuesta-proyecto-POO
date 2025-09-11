#Autor: Santiago Peralta Castellanos
#Encuesta para proyecto final
#Caso de uso: Registrar 10 encuentas 

class Encuesta:
    def __init__(self, preguntas, respuestas, nombre, edad):
        self.preguntas = preguntas
        self.respuestas = respuestas
        self.nombre = nombre
        self.edad = edad

    def resumen(self):
        print(f"\nRespuestas de {self.nombre} (edad {self.edad}):")
        for pregunta, respuesta in zip(self.preguntas, self.respuestas):
            print(f"{pregunta} -> {respuesta}")

def main():
    print("Encuesta proyecto POO")
    
    encuestas = []  # Guardar todas las encuestas

    preguntas = [
        "1: ¿Qué tema prefieres para el proyecto?",
        "2: ¿Sabes trabajar en equipo?",
        "3: ¿Conoces alguna librería de Python?"
    ]

    for _ in range(10):
        nombre = input("En este campo escriba su nombre: ")
        edad = int(input("En este campo escriba su edad: "))

        respuestas = []
        for pregunta in preguntas:
            print(pregunta)
            respuesta = input("Responda aquí: ")
            respuestas.append(respuesta)

        encuesta = Encuesta(preguntas, respuestas, nombre, edad)
        encuestas.append(encuesta)

    # Mostrar resumen de todas las encuestas
    for encuesta in encuestas:
        encuesta.resumen()

main()
