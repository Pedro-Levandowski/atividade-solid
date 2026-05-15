from abc import ABC, abstractmethod

class Notificacoes(ABC):
    @abstractmethod
    def enviar_notificacao(self, mensagem: str):
        pass