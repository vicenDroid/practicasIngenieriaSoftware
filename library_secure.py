import os

print("--- PROFESSIONAL LIBRARY SYSTEM (TRY/EXCEPT) ---")

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

# AuditAction base class
class AuditAction:
    def record(self, message):
        raise NotImplementedError()

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

# --- The Indestructible Auditor a new Class ---
class SecureFileAudit(AuditAction):
    def record(self, message):
        try:
            # We try a dangerous operation: writing to a file (which could fail for various reasons)
            with open("audit_log.txt", "a") as file:
                file.write(f"AUDIT LOG: {message}\n")
        except IOError as e:
            # If the file fails, we enter here (Plan B)
            print(f"!!! SECURITY ALERT: Could not write to the file.")
            print(f"!!! TECHNICAL ERROR: {e}")
            print(f"PLAN B (Console): {message}")
        finally:
            # This is executed ALWAYS, whether there's an error or not
            print("--- Audit operation completed ---")

# We create a validator, a system and a book too.
val = UserValidator()
system = LibrarySystem(val)
book = Book("Pelham 1 2 3", "John Godey")
# We create an auditor
auditor = SecureFileAudit()

# TEST BLOCK
# We test a user with spaces to check if the DRY principle is working (the system should clean the spaces)
print("\n>>> PRUEBA 1: Usuario con espacios (DRY check)")
system.perform_loan("  Vicente  ", book)

# We test an invalid user to check if the KISS principle is working
#  (the system should simply check the length)  
print("\n>>> PRUEBA 2: Usuario inválido (KISS check)")
system.perform_loan("Vi", book)

# We test a valid DNI to check if the YAGNI/DIP principle is working 
# (we only implemented what we needed, no extra features)
print("\n>>> PRUEBA 3: Cambio de validador (YAGNI/DIP check)")
dni_val = DniValidator()
sistema_dni = LibrarySystem(dni_val)
sistema_dni.perform_loan("12345678Z", book) 

# We test the auditor with a valid message (should write to the file)
print("\n>>> PRUEBA 4: Auditoría exitosa (Plan A)")
auditor.record("User Vicente loaned 'Pelham 1 2 3'.")

# We test the auditor with an invalid operation (simulate a file error by using an invalid path)
print("\n>>> PRUEBA 5: Auditoría con error (Plan B)")
auditor.record("User Vicente loaned 'Pelham 1 2 3'.")

# We temporarily change the method to simulate an error (monkey patching)
original_record = auditor.record
def faulty_record(message):
    raise IOError("Simulated file error")
auditor.record = faulty_record