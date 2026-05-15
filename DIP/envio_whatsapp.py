from notificacoes import Notificacoes

class EnvioWhatsapp(Notificacoes):
    def enviar_notificacao(self, mensagem: str):
        print(f'Enviando mensagem via whatsapp...\nMensagem enviada: {mensagem}')