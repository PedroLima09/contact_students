from urllib.parse import quote

from botcity.core import DesktopBot

def send_message(phone, message):

    sender = DesktopBot()
    
    sender.browse(f"https://web.whatsapp.com/send?phone=+55{phone}&text={quote(message)}")

    if not sender.find( "whatsapp", matching=0.97, waiting_time=7500):
        if sender.find( "send_button", matching=0.97, waiting_time=7500):
            sender.click()
            sucess = "Mensagem enviada com sucesso!"
            
            return sucess
        else:
            raise ValueError("Falha ao enviar mensagem.")
    else:
        raise ValueError("Efetue login no whatsapp antes de enviar a mensagem!")

def not_found(label):
    print(f"Element not found: {label}")
