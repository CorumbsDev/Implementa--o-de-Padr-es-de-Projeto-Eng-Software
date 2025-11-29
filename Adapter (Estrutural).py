from abc import ABC, abstractmethod

# Interface Alvo (Target)
class EuropeanPlug(ABC):
    @abstractmethod
    def use_european_socket(self) -> str:
        pass

# Serviço Existente (Adaptee)
class AmericanPlug:
    def use_american_socket(self) -> str:
        return "Conectado à tomada americana (110V, 3 pinos)"

# Adaptador
class PlugAdapter(EuropeanPlug):
    def __init__(self, american_plug: AmericanPlug):
        self._american_plug = american_plug
    
    def use_european_socket(self) -> str:
        # Adapta a interface americana para a europeia
        american_result = self._american_plug.use_american_socket()
        return f"Adaptador: {american_result} → Convertido para tomada europeia (220V, 2 pinos)"

# Cliente que espera a interface europeia
class EuropeanSocket:
    def connect(self, plug: EuropeanPlug) -> str:
        return plug.use_european_socket()

# Uso
if __name__ == "__main__":
    # Serviço existente (incompatível)
    american_plug = AmericanPlug()
    
    # Adaptador que torna compatível
    adapter = PlugAdapter(american_plug)
    
    # Cliente usando a interface esperada
    socket = EuropeanSocket()
    
    result = socket.connect(adapter)
    print(result)
    
    # Demonstração sem adaptador (não funcionaria)
    print("\nTentativa sem adaptador:")
    try:
        # Isso causaria erro de tipo
        # socket.connect(american_plug)  # TypeError!
        print("Erro: Interface incompatível!")
    except:
        print("Sem adaptador: As interfaces são incompatíveis!")