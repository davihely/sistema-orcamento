import tkinter as tk
import system.insert as insert
from FormValidation import FormValidation
from tkinter import ttk
from tkinter import messagebox
    
entry_dict = []
   
class Form(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.creat_fields()
        
    def creat_fields(self): 
        janela = self
        janela.title("Cadastro de cliente")
        janela.geometry('400x560')
        
        entry_keys = {
            'entry_nome' : ['Nome / Razão Social','1','1'], 
            'entry_cpf_cnpj' : ['CPF / CNPJ:','1','2'], 
            'entry_telefone' : ['Telefone','1','3'], 
            'entry_email' : ['E-mail','1','4'], 
            'entry_endereco' : ['Endereço','1','1'],
            'entry_cidade' : ['Cidade','1','1'], 
            'entry_estado' : ['Estado','2','1'],
            'entry_tipo_cliente' : ['Tipo de Cliente','2','1']
        }
        
        combo_fields = [
            ["SP", "RJ", "MG", "ES", "RS", "PR", "SC", "BA", "PE", "CE", "GO"],
            ["Pessoa Física", "Pessoa Jurídica"]
        ]
        
        labelRow = 0
        entryRow = 1
        comboRow = 0
        labelError = 0
                
        for key,value in entry_keys.items():
            label_error = {}
            if value[1] == '1':
                action = "<Key>"
                tk.Label(janela, text=value[0], anchor="w").grid(row=int(value[3]), column=0, sticky="w", padx=10, pady=(10, 0))
                key = tk.Entry(janela, width=40)
                key.grid(row=entryRow, column=0, padx=10, pady=2)
    
            else:
                action = "<<ComboboxSelected>>"
                tk.Label(janela, text=value[0], anchor="w").grid(row=int(value[3]), column=0, sticky="w", padx=10, pady=(10, 0))
                key = ttk.Combobox(janela, values=combo_fields[comboRow], width=37)
                key.grid(row=entryRow, column=0, padx=10, pady=2)

                comboRow += 1
            
            label_error['label_error' + str(labelError)] = ttk.Label(self, foreground='red')
            label_error['label_error' + str(labelError)].grid(row=entryRow, column=1, sticky=tk.W, padx=5)
            key.bind(action, lambda event, label=list(label_error.values())[0], entry=key: validation.remove_label_error(entry.get(), label))
            
            labelRow += 2
            entryRow += 2
            labelError += 1
            entry_dict.append((value[0], value[2] ,key, label_error))
        botao_salvar = tk.Button(janela, text="Salvar Cliente", command=lambda: self.validate_fields())
        botao_salvar.grid(row=18, column=0, pady=20)  
    
    def validate_fields(self):
        try:
            if all([bool(value[1].get()) == True for value in entry_dict]):
                for typedFilled in entry_dict:
                    entryValue = typedFilled[1].get()
                    labelErrorFilled = list(typedFilled[0].values())[0]
                    match typedFilled[1]:
                            case '2':
                                cpfcnpjValid = FormValidation.validate_cpf_cnpj(entryValue, labelErrorFilled)
                            case '3':
                                telValid = FormValidation.validate_tel(entryValue, labelErrorFilled)
                            case '4':
                                emailValidation = FormValidation.validate_email(entryValue, labelErrorFilled)
                if cpfcnpjValid and telValid and emailValidation:
                        self.get_values()    
                        return True    
            else:
                raise Exception("Existem campos vazios")
        except Exception as error:
            for typed in entry_dict:
                if not typed[2].get():
                    labelIndex = list(typed[3].values())[0]
                    FormValidation.show_message(labelIndex, 'Campo Vazio', 'Red') 
        
    def get_values(self):
        input_values = []
        for typed in entry_dict:
            input_values.append(typed[2].get())   
        insert.insert_cli(input_values)   