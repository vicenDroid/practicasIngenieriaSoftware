print("--- PROFESSIONAL LIBRARY SYSTEM (DRY-KISS-YAGNI) ---")

# DRY Principle: We centralize the "strip" logic here
class Validator:
    def prepare_data(self, data):
        """Clean the data once for all validators."""
        return data.strip()

    def is_valid(self, data):
        raise NotImplementedError("Subclasses must implement this method.")

# Now the subclasses are K.I.S.S. (Simple and clean)
class UserValidator(Validator):
    def is_valid(self, name):
        clean_name = self.prepare_data(name) # DRY: Using the base method
        return len(clean_name) > 5

class DniValidator(Validator):
    def is_valid(self, dni):
        clean_dni = self.prepare_data(dni) # DRY: Using the base method
        return len(clean_dni) == 9

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# We create a librarySystem class that can work with any validator, following the YAGNI & KISS principles
#  (we only implement what we need).
class LibrarySystem():
    def __init__(self, validator):
        self.validator = validator

    def perform_loan(self, user, book):
        if self.validator.is_valid(user):
            print(f"Loan successful: '{book.title}' for {user}")
        else:
            print(f"Error: User '{user}' is not valid.")

# We create a validator, a system and a book too.
val = UserValidator()
system = LibrarySystem(val)
book = Book("Clean Code", "Robert C. Martin")

# TEST BLOCK

# We test a user with spaces to check if the DRY principle is working (the system should clean the spaces)
print("\n>>> PRUEBA 1: Usuario con espacios (DRY check)")
system.perform_loan("  Vicente  ", book)

# We test an invalid user to check if the KISS principle is working
#  (the system should simply check the length)
print("\n>>> PRUEBA 2: Usuario inválido (KISS check)")
system.perform_loan("Vi", book)

# We test a valid DNI to check if the YAGNI principle is working 
# (we only implemented what we needed, no extra features)
print("\n>>> PRUEBA 3: Cambio de validador (YAGNI/DIP check)")
dni_val = DniValidator()
sistema_dni = LibrarySystem(dni_val)
sistema_dni.perform_loan("12345678Z", book)