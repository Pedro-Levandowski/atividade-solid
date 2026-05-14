from abc import ABC, abstractmethod

class IntAdmin(ABC):
    @abstractmethod
    def enviar_notificacao(self):
        pass

    @abstractmethod
    def gerar_relatorio(self):
        pass