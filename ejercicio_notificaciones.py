
# Importamos el módulo abc para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta para notificaciones
class MetodoNotificacion(ABC):

    # Método abstracto para enviar notificaciones
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificacionEmail(MetodoNotificacion):

    # Método para enviar notificaciones por email
    def enviar(self, mensaje):
        print(f"Enviando notificación por Email: {mensaje}")

class NotificacionSMS(MetodoNotificacion):

    # Método para enviar notificaciones por SMS
    def enviar(self, mensaje):
        print(f"Enviando notificación por SMS: {mensaje}")

# Intentamos usar lo que hemos creado
email = NotificacionEmail()
email.enviar("Tu pedido ha sido enviado.")
sms = NotificacionSMS()
sms.enviar("Tu pedido ha sido entregado.")