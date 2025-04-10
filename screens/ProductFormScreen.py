import tkinter as tk
from .Create import CreateFormInputs 
from .Validation import FormValidation
import models.Products as products
from tkinter import ttk
from tkinter import messagebox
       
class ProductForm(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.entryDict = []
        self.create_fields()
        
    def create_fields(self): 
        janela = self
        janela.title("Cadastro de Produto/Serviço")
        janela.geometry('275x560')
        
        entry_keys = {
            'nome_produto': {
                'fields': ['Nome', 'string', 'regular', '0']
            },
            'descricao_produto': {
                'fields': ['Descrição:', 'string', 'regular', '2']
            },
            'preco_produto': {
                'fields': ['Preço', 'price', 'price', '4']
            },
            'categoria_produto': {
                'fields': ['Categoria', 'combo', 'regular', '6'],
                'options': ['Produto', 'Serviço']
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
        botao_salvar = tk.Button(janela, text="Salvar Produto", command=lambda: self.validate_fields())
        botao_salvar.grid(row=18, column=0, pady=20)  
        
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
        for typed in self.entryDict:
            input_values.append(typed[0][0].get())   
        ProductsObj = products.Products()
        ProductsObj.insertProduct(input_values)   

    

    