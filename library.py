
print("--- SYSTEM STARTING ---")
print("--THE FILE IS RUNNING--")

# Any validator must have an is_valid method, but we don't know how it's implemented.
class Validator:
    def is_valid(self, dato):
        raise NotImplementedError("Este método debe ser implementado por las" \
        " subclases.")
    
# ENTITY: Only stores book information
# When we create a book, we only give it the two attributes we need: Title and Author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
 
# NEW VALIDATOR: Validation by ID number, which is completely different from validation by name,
# but the system doesn't know this; it only knows it's a validator. It must be 9 characters long to be valid.
# , for example: "12345678Z"
class DniValidator(Validator):
    def is_valid(self, dni):
        # Regla: Debe tener exactamente 9 caracteres (ejemplo simple)
        return len(dni.strip()) == 9

# SERVICE: Only validates if a user is eligible. Note: Requires more than 5 characters to be valid.
class UserValidator(Validator):
    def is_valid(self, name):
        # A name is valid if it is not empty and has more than 3 characters (simple rule)
        if len(name.strip()) > 5:
            return True
        return False
    
# We created the SisGestBi class for management. It's the system engine. It receives a validator
# in its "backpack" (self.validator) and uses it in perform_loan.
class SisGestBi:

    def __init__(self, Validator):
        # We saved the validation tool for later use
        self.Validator = Validator

    def perform_loan(self, user, book):
        # We use the tool to decide
        if self.Validator.is_valid(user):
            print(f"Préstamo realizado: '{book.title}' para {user}")
        else:
            print(f"Error: El usuario '{user}' no es válido.")    

# TEST RUNNER (DIP: This function is "blind", it just works with what it gets)
def run_library_test(configured_system, user, book):
    print(f"\n--- Iniciando proceso para {user} ---")
    configured_system.perform_loan(user, book)

# 1. We prepare the tools. We create the validator for users, which will be used in the system.
Validator = UserValidator()
# ¡Ojo aquí! Le pasas la herramienta anterior. El sistema ahora "sabe" que debe usar reglas de nombre.
system = SisGestBi(Validator)

# 2. We create the data. The favorite_book object is created with the data from "Clean Code".
favourite_book = Book("El Código Limpio", "Robert C. Martin")

# 3. We tested a case that SHOULD WORKprint("Probando con nombre válido:")
system.perform_loan("Vicente", favourite_book)

# 4. We tested a case that SHOULD FAIL (Short name)
print("\nProbando con nombre no válido:")
system.perform_loan("Vi", favourite_book)

# 5. Using the new ID card validation
print("\n> Probando Validación por DNI:")
val_dni = DniValidator()
sistema_dni = SisGestBi(val_dni)
sistema_dni.perform_loan("12345678Z", favourite_book)

# 6. We create a new book to test with the new system. This book is "The Little Prince" by Saint-Exupéry.
my_book = Book("El Principito", "Saint-Exupéry")

# 7. We inject different dependencies (DIP)
print("\n>>> PRUEBA 1: SISTEMA CON NOMBRE")
run_library_test(SisGestBi(UserValidator()), "Vicente", favourite_book)

print("\n>>> PRUEBA 2: SISTEMA CON DNI")
run_library_test(SisGestBi(DniValidator()), "98765432X", favourite_book)

# 8. We tested a case that SHOULD WORK using the "blind" function
run_library_test(system, "Vicente", favourite_book)

# 9. We tested a case that SHOULD FAIL using the "blind" function
run_library_test(system, "Vi", favourite_book)