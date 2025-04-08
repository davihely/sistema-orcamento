import tkinter as tk
import system.insert as insert
from FormValidation import FormValidation
from CreateFormInputs import CreateFormInputs
from tkinter import ttk
from tkinter import messagebox
       
class Form(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.entryDict = []
        self.create_fields()
        
    def create_fields(self): 
        janela = self
        janela.title("Cadastro de cliente")
        janela.geometry('275x560')
        
        entry_keys = {
            'entry_nome': {
                'fields': ['Nome / Razão Social', 'string', 'regular', '0']
            },
            'entry_cpf_cnpj': {
                'fields': ['CPF / CNPJ:', 'string', 'cpfcnpj', '2']
            },
            'entry_telefone': {
                'fields': ['Telefone', 'string', 'tel', '4']
            },
            'entry_email': {
                'fields': ['E-mail', 'string', 'email', '6']
            },
            'entry_endereco': {
                'fields': ['Endereço', 'string', 'regular', '8']
            },
            'entry_cidade': {
                'fields': ['Cidade', 'string', 'regular', '12']
            },
            'entry_estado': {
                'fields': ['Estado', 'combo', 'regular', '14'],
                'options': ["SP", "RJ", "MG", "ES", "RS", "PR", "SC", "BA", "PE", "CE", "GO"]
            },
            'entry_tipo_cliente': {
                'fields': ['Tipo de Cliente', 'combo', 'regular', '16'],
                'options': ["Pessoa Física", "Pessoa Jurídica"]
            }
        }
                
        for key,value in entry_keys.items():
            options = ''
            if value['fields'][1] == 'combo':
                options = value['options']      
            keyEntry = CreateFormInputs(janela, key, value, options)
            returnFields = keyEntry.fields()
            self.entryDict.append(returnFields)
        botao_salvar = tk.Button(janela, text="Salvar Cliente", command=lambda: self.validate_fields())
        botao_salvar.grid(row=18, column=0, pady=20)  
        
    def validate_fields(self):
        print(self.entryDict[0])
        try:
            if all([bool(value[1].get()) == True for value in self.entryDict]):
                for typedFilled in self.entryDict:
                    entryValue = typedFilled[1].get()
                    labelErrorFilled = list(typedFilled[0].values())[0]
                    print(typedFilled)
                    match typedFilled[1]:
                            case 'cpfcnpj':
                                cpfcnpjValid = FormValidation(entryValue, labelErrorFilled)
                                cpfcnpjValid.validate_cpf_cnpj()
                            case 'tel':
                                telValid = FormValidation(entryValue, labelErrorFilled)
                                telValid.validate_tel()
                            case 'email':
                                emailValidation = FormValidation(entryValue, labelErrorFilled)
                                emailValidation.validate_email()
                if cpfcnpjValid and telValid and emailValidation:
                        self.get_values()    
                        return True    
            else:
                raise Exception("Existem campos vazios")
        except Exception as error:
            for typed in self.entryDict:
                    labelIndex = list(typed[1].values())[0]
                    validationObj = FormValidation(typed[0].get(), labelIndex)
                    validationObj.validate_empty() 
        
    def get_values(self):
        input_values = []
        for typed in self.entryDict:
            input_values.append(typed[2].get())   
        insert.insert_cli(input_values)   

    

    