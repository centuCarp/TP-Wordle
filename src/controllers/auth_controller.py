from flask import Blueprint, render_template, request, redirect, url_for, session
from repositories.user_repository import UserRepository

# Creamos un Blueprint para agrupar las rutas de autenticación
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_view():
    """Muestra la página de inicio de sesión (Index)."""
    return render_template('index.html')

@auth_bp.route('/register')
def register_view():
    """Muestra la página de registro de usuarios."""
    return render_template('registro.html')

@auth_bp.route('/login', methods=['POST'])
def handle_login():
    """Recibe los datos del formulario de login."""
    email = request.form.get('email')
    password = request.form.get('password')
   # 1. Buscamos al usuario por su email en la base de datos
    usuario = UserRepository.obtener_por_email(email)
    
    # 2. Verificamos si el usuario existe y la contraseña coincide
    # (Nota: idealmente las contraseñas deberían estar hasheadas con Werkzeug, pero si las guardas en texto plano puedes compararlas directamente)
    if usuario and usuario['Contraseña'] == password:
        # Guardamos datos en la sesión de Flask si lo deseas
        session['user_id'] = usuario['Id']
        session['username'] = usuario['Username']
        
        # 3. Redirigimos al juego si el inicio de sesión es exitoso
        return redirect(url_for('game.juego_view'))
    else:
        # Si falla, puedes recargar el login (o mostrar un mensaje de error)
        return redirect(url_for('auth.login_view'))
    
@auth_bp.route('/register', methods=['POST'])
def handle_register():
    """Recibe los datos del formulario de registro."""
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Guardamos usando el repositorio
    UserRepository.guardar_usuario(username, email, password)

    # Aquí guardaremos el usuario usando el repositorio y servicio próximamente
    return redirect(url_for('auth.login_view'))

@auth_bp.route('/logout')
def logout():
    """Cierra la sesión del usuario y redirige al login."""
    session.clear()
    return redirect(url_for('auth.login_view'))

    