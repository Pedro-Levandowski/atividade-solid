from abc import ABC, abstractmethod

class IntEntregador(ABC):
    @abstractmethod
    def gerenciar_entregas(self):
        pass