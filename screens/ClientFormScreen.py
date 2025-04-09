import tkinter as tk
from .Create import CreateFormInputs 
from .Validation import FormValidation
import models.Clients as clients
from tkinter import ttk
from tkinter import messagebox
       
class ClientForm(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.entryDict = []
        self.create_fields()
        
    def create_fields(self): 
        janela = self
        janela.title("Cadastro de cliente")
        janela.geometry('275x560')
        
        entry_keys = {
            'nome_cliente': {
                'fields': ['Nome / Razão Social', 'string', 'regular', '0']
            },
            'cpfcnpj_cliente': {
                'fields': ['CPF / CNPJ:', 'string', 'cpfcnpj', '2']
            },
            'telefone_cliente': {
                'fields': ['Telefone', 'string', 'tel', '4']
            },
            'email_cliente': {
                'fields': ['E-mail', 'string', 'email', '6']
            },
            'entry_endereco': {
                'fields': ['Endereço', 'string', 'regular', '8']
            },
            'cidade_cliente': {
                'fields': ['Cidade', 'string', 'regular', '12']
            },
            'estado_cliente': {
                'fields': ['Estado', 'combo', 'regular', '14'],
                'options': ["SP", "RJ", "MG", "ES", "RS", "PR", "SC", "BA", "PE", "CE", "GO"]
            }
        }
                
        for key,value in entry_keys.items():
            type = value['fields'][2]
            options = ''
            if value['fields'][1] == 'combo':
                options = value['options']      
            keyEntry = CreateFormInputs(janela, key, value, options)
            returnFields = keyEntry.fields()
            self.entryDict.append((returnFields,type))
        botao_salvar = tk.Button(janela, text="Salvar Cliente", command=lambda: self.validate_fields())
        botao_salvar.grid(row=18, column=0, pady=20)  
        
    def validate_fields(self):
        try:
            if all([bool(value[0][0].get()) == True for value in self.entryDict]):
                for typedFilled in self.entryDict:
                    entryValue = typedFilled[0][0].get()
                    labelErrorFilled = list(typedFilled[0][1].values())[0]
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
                    labelIndex = list(typed[0][1].values())[0]
                    validationObj = FormValidation(typed[0][0].get(), labelIndex)
                    validationObj.validate_empty() 
        
    def get_values(self):
        input_values = []
        for typed in self.entryDict:
            input_values.append(typed[0][0].get())   
        clientObj = clients.Client()
        clientObj.insertClient(input_values)   

    

    