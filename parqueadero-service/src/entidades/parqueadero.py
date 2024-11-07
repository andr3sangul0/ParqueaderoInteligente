# parqueadero.py
class Parqueadero:
    def __init__(self):
        self.espacios = {}

    def agregar_espacio(self, espacio):
        self.espacios[espacio.id] = espacio

    def obtener_espacio(self, id):
        return self.espacios.get(id)

    def reservar_espacio(self, id, vehiculo_id):
        espacio = self.obtener_espacio(id)
        if espacio and espacio.disponible:
            espacio.disponible = False
            espacio.vehiculo_id = vehiculo_id
            return True
        return False
