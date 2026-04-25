from abc import ABC, abstractmethod

# 1. El "Contrato" (Abierto a extensión, cerrado a modificación)
class MetodoNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# 2. Las clases que ya funcionan (No las toques)
class NotificadorEmail(MetodoNotificacion):
    def enviar(self, mensaje):
        print(f"📧 Email: {mensaje}")

class NotificadorSMS(MetodoNotificacion):
    def enviar(self, mensaje):
        print(f"📱 SMS: {mensaje}")

# 3. Función principal (Le da igual qué notificador sea, mientras funcione)
def enviar_alerta(notificador: MetodoNotificacion, texto):
    notificador.enviar(texto)

# --- TU TURNO AQUÍ ABAJO ---
# Crea la clase NotificadorDiscord que herede de MetodoNotificacion
# Y luego pruébalo llamando a enviar_alerta()
class NotificadorDiscord(MetodoNotificacion):
    def enviar(self, mensaje):
        print(f"💬 Discord: {mensaje}")
# --- LA PRUEBA DE FUEGO ---
# 1. Creamos los objetos (las "herramientas")
correo = NotificadorEmail()
sms = NotificadorSMS()
discord = NotificadorDiscord()

# 2. Usamos la función principal para todos
print("--- Iniciando notificaciones ---")
enviar_alerta(correo, "Tienes una clase nueva")
enviar_alerta(sms, "Tu contraseña ha cambiado")
enviar_alerta(discord, "¡Vicente ya domina SOLID!")