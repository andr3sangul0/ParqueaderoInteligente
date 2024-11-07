# registro_service.py
from entidades.registro import Registro
from dao.registro_dao import RegistroDAO

class RegistroService:
    def __init__(self, dao: RegistroDAO):
        self.dao = dao

    def registrar_entrada(self, vehiculo_id, espacio_id):
        registro = Registro(vehiculo_id, espacio_id)
        self.dao.guardar_registro(registro)
        return registro
