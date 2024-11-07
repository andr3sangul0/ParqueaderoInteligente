# vehiculo_service.py
from entidades.vehiculo import Vehiculo
from dao.vehiculo_dao import VehiculoDAO

class VehiculoService:
    def __init__(self, dao: VehiculoDAO):
        self.dao = dao

    def registrar_vehiculo(self, placa, marca, modelo, color):
        vehiculo = Vehiculo(placa, marca, modelo, color)
        self.dao.guardar_vehiculo(vehiculo)
        return vehiculo
