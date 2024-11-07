# parqueadero_service.py
from entidades.parqueadero import Parqueadero
from dao.espacio_dao import EspacioDAO

class ParqueaderoService:
    def __init__(self, dao: EspacioDAO):
        self.dao = dao
        self.parqueadero = Parqueadero()

    def inicializar_espacios(self, espacios):
        for espacio in espacios:
            self.parqueadero.agregar_espacio(espacio)
            self.dao.guardar_espacio(espacio)
