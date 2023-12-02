from utils.sender import send_message

class Student():
    def __init__(self, name, phone, selected_time, message) -> None:
        self.name = name
        self.phone = f"+55{phone}"
        self.selected_time = selected_time
        self.message = message

    def set_message(self):

        start = f"""
Olá {self.name}! Sou seu monitor da infinity. 
Você agendou o horario de {self.selected_time}.
"""     
        forms = f"\nSegue o link para avaliação da monitoria: https://forms.gle/PDtXt2a6EcNE6j8f8 (Preencha ao fim)"
        
        selection = None
        match self.message:
            case "Replacement":
                selection = "Reposição"
            case "Tutoring":    
                selection = "Reforço"
            case "Undeclared":
                return f"{start} \nGostaria de confirmar sua presença na monitoria. Não consegui visualizar exatamente sobre qual assunto vamos tratar, Você conseguiria me especificar? \n{forms}."
            
            case "Introduction":
                selection = "Introdução"

        return f"{start} \nGostaria de confirmar a sua presença na sua aula de {selection}. Qual o assunto especificamente você gostaria de tratar na sua monitoria? \n{forms}."
    
        
        
    def send(self):
        return send_message(self.phone, self.set_message())

