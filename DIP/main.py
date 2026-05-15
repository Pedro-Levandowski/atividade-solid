from envio_email import EnvioEmail
from envio_sms import EnvioSMS
from envio_whatsapp import EnvioWhatsapp
from notificador import Notificador

envio_email = EnvioEmail()
envio_sms = EnvioSMS()
envio_whatsapp = EnvioWhatsapp()

notificador_1 = Notificador(envio_email)
notificador_2 = Notificador(envio_sms)
notificador_3 = Notificador(envio_whatsapp)

notificador_1.alertar_multa()
notificador_2.alertar_multa()
notificador_3.alertar_multa()