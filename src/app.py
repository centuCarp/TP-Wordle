from flask import Flask, render_template

# Inicializamos la aplicación Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'clave_secreta_para_sesiones'

# Ruta principal que carga la interfaz del juego
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Arrancamos el servidor de desarrollo local en el puerto 5000
    app.run(host='127.0.0.1', port=5000, debug=True)