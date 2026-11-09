from flask import Blueprint, render_template, request, jsonify
from services.game_service import GameService

game_bp = Blueprint('game', __name__)
game_service = GameService()

@game_bp.route('/juego')
def juego_view():
    return render_template('juego.html')

@game_bp.route('/api/guess', methods=['POST'])
def guess_word():
    data = request.get_json()
    palabra = data.get('word', '')
    
    respuesta = game_service.procesar_intento(palabra)
    
    if "error" in respuesta:
        return jsonify(respuesta), 400
        
    return jsonify(respuesta)