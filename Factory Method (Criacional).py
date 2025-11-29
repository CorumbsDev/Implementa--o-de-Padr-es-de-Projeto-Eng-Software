from abc import ABC, abstractmethod
from enum import Enum

# Interface do Produto
class Vehicle(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

# Produtos Concretos
class Truck(Vehicle):
    def deliver(self) -> str:
        return "Entrega por caminhão: transporte terrestre de carga pesada"

class Ship(Vehicle):
    def deliver(self) -> str:
        return "Entrega por navio: transporte marítimo de containers"

class Airplane(Vehicle):
    def deliver(self) -> str:
        return "Entrega por avião: transporte aéreo rápido"

# Criador
class Logistics(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass
    
    def plan_delivery(self) -> str:
        vehicle = self.create_vehicle()
        return f"Planejando entrega... {vehicle.deliver()}"

# Criadores Concretos
class RoadLogistics(Logistics):
    def create_vehicle(self) -> Vehicle:
        return Truck()

class SeaLogistics(Logistics):
    def create_vehicle(self) -> Vehicle:
        return Ship()

class AirLogistics(Logistics):
    def create_vehicle(self) -> Vehicle:
        return Airplane()

# Uso
if __name__ == "__main__":
    def client_code(logistics: Logistics) -> None:
        print(logistics.plan_delivery())
    
    # Testando diferentes fábricas
    client_code(RoadLogistics())
    client_code(SeaLogistics())
    client_code(AirLogistics())