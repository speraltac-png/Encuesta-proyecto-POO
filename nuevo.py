#Autor: Santiago Peralta Castellanos
#Encuesta para proyecto final
#Caso de uso: Registrar 10 encuentas 

class Encuesta:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas = []


    def agregar_respuestas(self):
        for pregunta in self.preguntas:
            respuesta = input(pregunta + ": ")
            self.respuestas.append(respuesta)  

    def mostrar_resultados(self):
        print("Resultado de la encuesta")
        for i in range(len(self.preguntas)):
            print(f"{self.preguntas[i]}: {self.respuestas[i]}")
        
    def resumen(self):            
        print("Resumen")
        print(f"Total de preguntas: {len(self.preguntas)}")
        print(f"Total de respuestas: {len(self.respuestas)}")


def main():
    print("Encuesta proyecto final")

    preguntas = [
        "Nombre ", "Edad", 
        "1: ¿Qué tema prefieres para el proyecto?",
        "2: ¿Sabes trabajar en equipo?",
        "3: ¿Conoces alguna librería de Python?"
    ]
    encuesta_poo = Encuesta(preguntas)

    encuesta_poo.agregar_respuestas()
    encuesta_poo.mostrar_resultados()
    encuesta_poo.resumen()
main()    

