from notificacoes import Notificacoes

class Notificador():
    def __init__(self, notificacoes: Notificacoes):
        self.notificacoes = notificacoes

    def alertar_multa(self):
        self.notificacoes.enviar_notificacao('Pedido com atraso na entrega!')
