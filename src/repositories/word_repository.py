import os
import random

class WordRepository:
    
    @staticmethod
    def obtener_todas_las_palabras():
        """Lee el archivo .txt y retorna una lista de palabras limpias de 5 letras."""
        ruta_archivo = os.path.join(os.path.dirname(__file__), '../../data/palabras_5_letras.txt')
        
        palabras = []
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    palabra = linea.strip().upper()
                    if len(palabra) == 5:
                        palabras.append(palabra)
        else:
            # Respaldo por seguridad si no encuentra el archivo
            palabras = ["PERRO", "GATO", "LIBRO", "MESA", "SILLA"]
        return palabras

    @staticmethod
    def obtener_palabra_aleatoria():
        """Selecciona y retorna una palabra aleatoria para iniciar una partida de Wordle."""
        palabras = WordRepository.obtener_todas_las_palabras()
        if palabras:
            return random.choice(palabras)
        return "PYTHON" # Valor de respaldo por seguridad

    @staticmethod
    def existe_palabra(palabra):
        """Verifica si una palabra ingresada existe dentro del conjunto de palabras válidas."""
        palabras = WordRepository.obtener_todas_las_palabras()
        return palabra.upper().strip() in palabras