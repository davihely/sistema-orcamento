import tkinter as tk
from tkinter import ttk
from .Create import CreateFormInputs 
from .Validation import FormValidation
import models.Clients as clients
import models.Orcamentos as orcamentos     

class OrcamentoForm(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.janela = self
        self.entryDict = []
        self.clientsDict = {}
        self.numberOfItens = 0
        self.create_fields()
        
    def create_fields(self): 
        self.janela.title("Cadastro de Produto/Serviço")
        self.janela.geometry('500x560')
        
        cliObj = clients.Client()
        clientsResults = cliObj.listClients()
        listCliIds = []
        listCliNames = []
        for client in clientsResults:
            listCliIds.append(client[0])
            listCliNames.append(client[1])
            self.clientsDict['id'] = listCliIds
            self.clientsDict['names'] = listCliNames

        orcamento_entry_keys = {
            'cliente_orcamento': {
                'fields': ['Cliente:', 'combo', 'regular', '2', '0'],
                'options': self.clientsDict
            },
            'valor_orcamento': {
                'fields': ['Valor Total:', 'string', 'regular', '0', '0']
            }
        }
                
        for key,value in orcamento_entry_keys.items():
            type = value['fields'][2]
            options = ''
            if value['fields'][1] == 'combo':
                options = value['options']      
            keyEntry = CreateFormInputs(self.janela, key, value, options)
            returnFields = keyEntry.fields()
            self.entryDict.append((returnFields,type))
        botao_salvar = tk.Button(self.janela, text="Salvar Produto", command=lambda: self.create_itens_fields())
        botao_salvar.grid(row=18, column=0, pady=20)     
        
    def create_itens_fields(self):
        
        itens_entry_keys_model = {
            'produto_item': {
                'fields': ['Produto:', 'combo', 'regular', '4', '0'],
                'options': self.clientsDict
            },
            'quantide_item': {
                'fields': ['Quantidade:', 'string', 'regular', '4', '1']
            },
            'valor_item': {
                'fields': ['Valor Total Item:', 'string', 'regular', '4', '2']
            }
        }
        
        if self.numberOfItens > 0:
            for key,value in itens_entry_keys_model.items():
                value['fields'][3] = str((2 * self.numberOfItens) + int(value['fields'][3]))
        keyEntry = CreateFormInputs(self.janela)
        returnFields = keyEntry.OrcamentoItensFields(itens_entry_keys_model,self.numberOfItens)
        if returnFields:
            self.numberOfItens += 1
        
        
    def validate_fields(self):
        try:
            if all([bool(value[0][0].get()) == True for value in self.entryDict]):
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
        cliIdChosen = ''
        for typed in self.entryDict:
            if isinstance(typed[0][0], ttk.Combobox):  
                indexCli = typed[0][0].current()
                cliIdChosen = self.clientsDict['id'][indexCli]
            input_values.append(typed[0][0].get()) 
        input_values.append(cliIdChosen) 
        orcamentoObj = orcamentos.Orcamento()
        orcamentoObj.insertOrcamento(input_values)   
        

    

    