
print("--- EL ARCHIVO SE ESTÁ EJECUTANDO ---")

# ENTIDAD: Solo guarda información del libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# SERVICIO: Solo se encarga de validar si un usuario es apto
class ValidadorUsuario:
    def es_valido(self, nombre):
        # Un nombre es válido si no está vacío y tiene más de 3 caracteres
        if len(nombre.strip()) > 5:
            return True
        return False
    
class ValidadorPorDNI:
    def es_valido(self, dni):
        # Regla: Debe tener exactamente 9 caracteres (ejemplo simple)
        return len(dni.strip()) == 9
    
# Creamos la clase SisGestBi para gestionar 
class SisGestBi:

    def __init__(self, validador):
        # Guardamos la herramienta de validación para usarla después
        self.validador = validador

    def realizar_prestamo(self, usuario, libro):
        # Usamos la herramienta para decidir
        if self.validador.es_valido(usuario):
            print(f"Préstamo realizado: '{libro.titulo}' para {usuario}")
        else:
            print(f"Error: El usuario '{usuario}' no es válido.")    

# 1. Preparamos las herramientas
validador = ValidadorUsuario()
sistema = SisGestBi(validador)

# 2. Creamos los datos
libro_favorito = Libro("El Código Limpio", "Robert C. Martin")

# 3. Probamos un caso que DEBERÍA FUNCIONAR
print("Probando con nombre válido:")
sistema.realizar_prestamo("Vicente", libro_favorito)

# 4. Probamos un caso que DEBERÍA FALLAR (Nombre corto)
print("\nProbando con nombre no válido:")
sistema.realizar_prestamo("Vi", libro_favorito)

# Usando la nueva validación por DNI
print("\n> Probando Validación por DNI:")
val_dni = ValidadorPorDNI()
sistema_dni = SisGestBi(val_dni)
sistema_dni.realizar_prestamo("12345678Z", libro_favorito)