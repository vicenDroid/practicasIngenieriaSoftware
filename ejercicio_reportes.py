
# Creamos la clase Reporte para guardar informacion
class Reporte:

    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    
    def obtener_datos(self):
        """Devuelve los datos para que otros puedan usarlos."""
        return self.titulo, self.contenido

# Creamos la clase GestiorArchivo para guardar el reporte en un archivo
class GestorArchivo:

    # Metodo para guardar el reporte en un archivo de texto
    def guardar_reporte(self, reporte):
        titulo, contenido = reporte.obtener_datos()
        with open("reporte.txt", "w") as archivo:
            archivo.write(f"Titulo: {titulo}\n")
            archivo.write(f"Contenido: {contenido}\n")

# Creamos la clase Visualizador para poner bonito el reporte en la pantalla
class Visualizador:

    # Metodo para mostrar el reporte en la pantalla
    def mostrar_reporte(self, reporte):
        titulo, contenido = reporte.obtener_datos()
        print(f"--- {titulo} ---")
        print(contenido)

# 1. Creamos los datos
mi_reporte = Reporte("Ventas Abril", "Se han vendido 500 unidades.")

# 2. Creamos a los especialistas
archivo = GestorArchivo()
pantalla = Visualizador()

# 3. Les pasamos el reporte para que cada uno haga su trabajo
pantalla.mostrar_reporte(mi_reporte)
archivo.guardar_reporte(mi_reporte)