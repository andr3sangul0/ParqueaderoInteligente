# espacio.py
class Espacio:
    def __init__(self, id, disponible=True, vehiculo_id=None):
        self.id = id
        self.disponible = disponible
        self.vehiculo_id = vehiculo_id
