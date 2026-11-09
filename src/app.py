from flask import Flask
from controllers.auth_controller import auth_bp
from controllers.game_controller import game_bp

# Inicializamos la aplicación Flask indicando dónde están las carpetas de plantillas y estáticos
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'clave_secreta_para_sesiones'

# Registramos el Blueprint de autenticación (Capa 1)
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)

if __name__ == '__main__':
    # Encendemos el servidor local en el puerto 5000
    app.run(host='127.0.0.1', port=5000, debug=True)