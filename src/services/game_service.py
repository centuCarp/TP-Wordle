from repositories.word_repository import WordRepository

class GameService:
    def __init__(self):
        # Obtenemos la palabra secreta inicial
        self.palabra_secreta = WordRepository.obtener_palabra_aleatoria()

    def reiniciar_juego(self):
        # Genera una nueva palabra aleatoria al reiniciar
        self.palabra_secreta = WordRepository.obtener_palabra_aleatoria()

    def procesar_intento(self, palabra_ingresada):
        palabra = palabra_ingresada.upper().strip()
        
        if len(palabra) != 5:
            return {"error": "La palabra debe tener exactamente 5 letras."}
        
        if not WordRepository.existe_palabra(palabra):
            return {"error": "La palabra no se encuentra en el diccionario."}
        
        secreta = self.palabra_secreta.upper()
        resultado = [None] * 5
        letras_secretas_disponibles = list(secreta)
        
        # Primera pasada: Aciertos exactos (Verde / correct)
        for i in range(5):
            if palabra[i] == secreta[i]:
                resultado[i] = "correct"
                letras_secretas_disponibles[i] = None
                
        # Segunda pasada: Letras contenidas (Amarillo / present) o ausentes (Gris / absent)
        for i in range(5):
            if resultado[i] is not None:
                continue
                
            letra = palabra[i]
            if letra in letras_secretas_disponibles:
                idx = letras_secretas_disponibles.index(letra)
                resultado[i] = "present"
                letras_secretas_disponibles[idx] = None
            else:
                resultado[i] = "absent"
                
        ganado = (palabra == secreta)
        
        return {
            "resultado": resultado,
            "ganado": ganado,
            "palabra_secreta": self.palabra_secreta
        }