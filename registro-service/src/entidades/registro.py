# registro.py
from datetime import datetime

class Registro:
    def __init__(self, vehiculo_id, espacio_id, fecha_entrada=None, fecha_salida=None):
        self.vehiculo_id = vehiculo_id
        self.espacio_id = espacio_id
        self.fecha_entrada = fecha_entrada or datetime.now()
        self.fecha_salida = fecha_salida
