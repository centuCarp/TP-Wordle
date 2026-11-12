from flask import Blueprint, render_template, request, jsonify, session
from services.game_service import GameService

game_bp = Blueprint('game', __name__)
game_service = GameService()

@game_bp.route('/juego')
def juego_view():
    # Si no hay una palabra secreta en la sesión de este usuario, la creamos
    if 'palabra_secreta' not in session:
        session['palabra_secreta'] = game_service.palabra_secreta
        session['fila_actual'] = 0
        session['historial'] = []
    
    return render_template('juego.html')

@game_bp.route('/api/guess', methods=['POST'])
def guess_word():
    data = request.get_json()
    palabra = data.get('word', '')
    
    # Sincronizamos la palabra secreta del servicio con la de la sesión del usuario
    game_service.palabra_secreta = session.get('palabra_secreta', game_service.palabra_secreta)
    
    respuesta = game_service.procesar_intento(palabra)
    
    if "error" in respuesta:
        return jsonify(respuesta), 400
        
    # Guardamos en la sesión
    if 'historial' not in session:
        session['historial'] = []
    
    session['historial'].append({
        "palabra": palabra,
        "resultado": respuesta["resultado"]
    })
    session['fila_actual'] = len(session['historial'])
    session.modified = True
        
    return jsonify(respuesta)

@game_bp.route('/api/estado', methods=['GET'])
def obtener_estado():
    return jsonify({
        "historial": session.get('historial', []),
        "palabra_secreta": session.get('palabra_secreta', '')
    })

@game_bp.route('/api/reset', methods=['POST'])
def reset_game():
    game_service.reiniciar_juego()
    session['palabra_secreta'] = game_service.palabra_secreta
    session['fila_actual'] = 0
    session['historial'] = []
    session.modified = True
    return jsonify({"mensaje": "Juego reiniciado con éxito"})