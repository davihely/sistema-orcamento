import re

class FormValidation():
    def __init__(self,value,label):
        self.label = label
        self.value = value
            
    def validate_email(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, self.value) is None:
            return self.show_message(self.label, 'E-mail invalido', 'red')
        return True
        
    def validate_tel(self):
        pattern = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
        if re.fullmatch(pattern, self.value) is None:
            return self.show_message(self.label, 'Telefone invalido', 'red')   
        return True  
        
    def validate_cpf_cnpj(self):
        patternCpf = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$'
        patternCnpj = r'^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$'
        if re.fullmatch(patternCpf, self.value) or re.fullmatch(patternCnpj, self.value) is not None:
            return True
        return self.show_message(self.label, 'CPF/CNPJ invalido', 'red')

    def validate_empty(self):
        if not self.value:
            return self.show_message(self.label,'Campo Vazio', 'red')
        return True
    
    @staticmethod 
    def validate_only_numeric(value,label,entry):
        if value.isnumeric():
            FormValidation.remove_label_error(value,label)
        else:
            FormValidation.show_message(label, 'Digite apenas números', 'red')
            entry.delete(len(value) - 1)
    
    @staticmethod    
    def show_message(label, error, color):
            label['text'] = error
            label['foreground'] = color
            
    @staticmethod        
    def remove_label_error(value,label):
            #index = value.current()
            #id_escolhido = comboid[index]
            #print(id_escolhido)
            if value:
                label['foreground'] = 'black'
                label['text'] = ''
            return False
