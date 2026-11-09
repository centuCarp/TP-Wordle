from flask import Blueprint, render_template, request, redirect, url_for

# Creamos un Blueprint para agrupar las rutas de autenticación
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_view():
    """Muestra la página de inicio de sesión (Index)."""
    return render_template('index.html')

@auth_bp.route('/register')
def register_view():
    """Muestra la página de registro de usuarios."""
    return render_template('register.html')

@auth_bp.route('/login', methods=['POST'])
def handle_login():
    """Recibe los datos del formulario de login."""
    email = request.form.get('email')
    password = request.form.get('password')
    # Aquí llamaremos al servicio de autenticación próximamente
    return redirect(url_for('auth.login_view'))

@auth_bp.route('/register', methods=['POST'])
def handle_register():
    """Recibe los datos del formulario de registro."""
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    # Aquí guardaremos el usuario usando el repositorio y servicio próximamente
    return redirect(url_for('auth.login_view'))

@auth_bp.route('/juego')
def juego_view():
    """Muestra la pantalla principal del Wordle (juego.html)."""
    return render_template('juego.html')
    