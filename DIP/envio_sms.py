from notificacoes import Notificacoes

class EnvioSMS(Notificacoes):
    def enviar_notificacao(self, mensagem: str):
        print(f'Enviando mensagem via SMS...\nMensagem enviada: {mensagem}')