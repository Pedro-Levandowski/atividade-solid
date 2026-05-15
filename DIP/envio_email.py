from notificacoes import Notificacoes

class EnvioEmail(Notificacoes):
    def enviar_notificacao(self, mensagem: str):
        print(f'Enviando mensagem via email...\nMensagem enviada: {mensagem}')