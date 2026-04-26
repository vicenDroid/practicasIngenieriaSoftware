# BASE CLASS for Validation
class Validator:
    def is_valid(self, data):
        raise NotImplementedError("Subclasses must implement this method.")

# BASE CLASS for Auditing (The new part!)
class AuditAction:
    def record(self, message):
        raise NotImplementedError("Subclasses must implement this method.")

# BASE CLASS NotificationAction
class NotificationAction:
    def notify(self, user, book_title):
        raise NotImplementedError("Subclasses must implement this method.")

# VALIDATORS
class UserValidator(Validator):
    def is_valid(self, name):
        return len(name.strip()) > 5

class DniValidator(Validator):
    def is_valid(self, dni):
        return len(dni.strip()) == 9
    
# NEW VALIDATOR
class EmailNotification(NotificationAction):
    def notify(self, user, book_title):
        print(f"SENDING EMAIL: Alert! Invalid user {user} tried to take {book_title}")

# AUDITORS (New tools)
class FileAudit(AuditAction):
    def record(self, message):
        with open("audit_log.txt", "a") as file:
            file.write(f"AUDIT LOG: {message}\n")

class ConsoleAudit(AuditAction):
    def record(self, message):
        print(f"SPECIAL AUDIT: {message}")

class LibrarySystem:
    def __init__(self, validator, auditor, notifier):
        self.validator = validator  # Tool 1
        self.auditor = auditor      # Tool 2
        self.notifier = notifier    # Tool 3

    def issue_loan(self, user, book_title):
        if self.validator.is_valid(user):
            # ... éxito ...
            self.auditor.record(message=f"Loan issued for '{book_title}' to user '{user}'")
        else:
            print(f"ERROR: User '{user}' is not valid.")
            # ¡Usamos la tercera herramienta!
            self.notifier.notify(user, book_title)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# TEST RUNNER
def run_library_test(configured_system, user, book):
    print(f"\n--- Starting process for {user} ---")
    configured_system.issue_loan(user, book.title)

# 1. Prepare the tools
user_validator = UserValidator()
file_auditor = FileAudit()
console_auditor = ConsoleAudit()
email_notifier = EmailNotification()

# 2. Create the system with the chosen tools
library_system_with_file_audit = LibrarySystem(user_validator, file_auditor, email_notifier)
library_system_with_console_audit = LibrarySystem(user_validator, console_auditor, email_notifier)

# 3. Create the data
favourite_book = Book("El Código Limpio", "Robert C. Martin")
my_book = Book("El Principito", "Saint-Exupéry")

# 4. Test a case that SHOULD WORK
print("Testing with a valid user:")
run_library_test(library_system_with_file_audit, "Vicente", favourite_book)
run_library_test(library_system_with_console_audit, "Vicente", favourite_book)

# 5. Test a case that SHOULD FAIL
print("\nTesting with an invalid user:")
run_library_test(library_system_with_file_audit, "Vi", favourite_book)
run_library_test(library_system_with_console_audit, "Vi", favourite_book)

# 6. Using the new ID card validation
print("\n> Testing with DNI Validation:")
dni_validator = DniValidator()
library_system_with_dni = LibrarySystem(dni_validator, file_auditor, email_notifier)
run_library_test(library_system_with_dni, "12345678Z", favourite_book)

# 7. Inject different dependencies (DIP)
print("\n>>> TEST 1: SYSTEM WITH FILE AUDIT")
run_library_test(LibrarySystem(user_validator, file_auditor, email_notifier), "Vicente", favourite_book)

print("\n>>> TEST 2: SYSTEM WITH CONSOLE AUDIT")
run_library_test(LibrarySystem(user_validator, console_auditor, email_notifier), "Vicente", favourite_book)

# 8. Test a case that SHOULD WORK using the "blind" function
run_library_test(library_system_with_file_audit, "Vicente", favourite_book)