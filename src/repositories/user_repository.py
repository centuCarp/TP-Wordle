import mysql.connector

def get_db_connection():
    """Establece y retorna la conexión con la base de datos MariaDB."""
    return mysql.connector.connect(
        host="localhost",
        user="root",          # Cambia esto por tu usuario de MariaDB si es diferente
        password="",          # Pon tu contraseña de MariaDB aquí
        database="Wordle"     # El nombre de la base de datos que creaste
    )

class UserRepository:
    
    @staticmethod
    def guardar_usuario(username, email, password):
        """Inserta un nuevo usuario en la base de datos."""
        conexion = get_db_connection()
        cursor = conexion.cursor()
        try:
            query = "INSERT INTO Usuarios (Username, Email, Contraseña) VALUES (%s, %s, %s)"
            cursor.execute(query, ( username, email, password))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def obtener_por_email(email):
        """Busca un usuario en la base de datos por su email para el login."""
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True) # dictionary=True devuelve los resultados como diccionarios
        try:
            query = "SELECT * FROM Usuarios WHERE Email = %s"
            cursor.execute(query, (email,))
            usuario = cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()

    