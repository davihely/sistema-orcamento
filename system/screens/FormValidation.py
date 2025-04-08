import re

class FormValidation():
    def __init__(self,value,label):
        self.label = label
        self.value = value
            
    def validate_email(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, self.value) is None:
            return self.show_message('E-mail invalido', 'red')
        return True
        
    def validate_tel(self):
        pattern = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
        if re.fullmatch(pattern, self.value) is None:
            return self.show_message('Telefone invalido', 'red')   
        return True  
        
    def validate_cpf_cnpj(self):
        patternCpf = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$'
        patternCnpj = r'^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$'
        if re.fullmatch(patternCpf, self.value) or re.fullmatch(patternCnpj, self.value) is not None:
            return True
        return self.show_message('CPF/CNPJ invalido', 'red')

    def validate_empty(self):
        if not self.value:
            return self.show_message('Campo Vazio', 'red')
        return True
            
    def show_message(self, error, color):
            self.label['text'] = error
            self.label['foreground'] = color
            
    @staticmethod        
    def remove_label_error(value,label):
            if value:
                label['foreground'] = 'black'
                label['text'] = ''
            return False
