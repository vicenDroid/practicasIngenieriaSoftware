from abc import ABC, abstractmethod

class MetodoPago(ABC):
    """
    Esta es la Interfaz (Clase Base Abstracta). 
    Define las reglas que todos los tipos de pago deben cumplir.
    """
    @abstractmethod
    def procesar_transaccion(self, importe):
        """
        Método obligatorio para realizar el cobro del dinero.
        Cada clase hija debe implementar su propia lógica.
        """        
        pass

    @abstractmethod
    def generar_recibo(self):
        """
        Método obligatorio para emitir el comprobante de pago.
        """
        pass

# --- IMPLEMENTA TUS CLASES AQUÍ ABAJO ---
# 1. Crea la clase PagoTarjeta(MetodoPago)
# 2. Crea la clase PagoPayPal(MetodoPago)
# 3. No olvides poner comentarios a tus métodos explicando qué hacen.

class PagoTarjeta(MetodoPago):

    # Metodo para procesar el pago con tarjeta de credito
    def procesar_transaccion(self, importe):
        print(("Procesando transaccion con tarjeta de credito"))

    # Metodo para generar el recibo del pago con tarjeta de credito
    def generar_recibo(self):
        print(("Generando recibo con tarjeta de credito"))

class PagoPayPal(MetodoPago):    

    # Metodo para procesar el pago con PayPal
    def procesar_transaccion(self, importe):
        print(("Procesando transaccion con PayPal"))

    # Metodo para generar el recibo con PayPal
    def generar_recibo(self):
        print(("Generando recibo con PayPal"))    
        
# Intentamos usar lo que hemos creado
tarjeta = PagoTarjeta()
tarjeta.procesar_transaccion(50)
tarjeta.generar_recibo()   
payPal = PagoPayPal()
payPal.procesar_transaccion(50)
payPal.generar_recibo()     