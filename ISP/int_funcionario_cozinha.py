from abc import ABC, abstractmethod

class IntFuncionarioCozinha(ABC):
    @abstractmethod
    def gerenciar_pedidos(self):
        pass