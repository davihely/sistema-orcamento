import tkinter as tk
from tkinter import ttk
from .Validation import FormValidation

class CreateFormInputs():
    def __init__(self,window,field = '',value = '',comboFields = '',key ='',labelError = ''):
        self.window = window
        self.field = field
        self.value = value
        self.comboFields = comboFields
        self.key = key
        self.labelError = labelError
        
    def fields(self):
        label_error = {}  
   
        tk.Label(self.window, text=self.value['fields'][0], anchor="w").grid(row=int(self.value['fields'][3]), column=int(self.value['fields'][4]), sticky="w", padx=10, pady=(10, 0))

        action = "<Key>"
        if self.value['fields'][1] == 'string':
            key = tk.Entry(self.window, width=40)
        elif self.value['fields'][1] == 'combo':
            action = "<<ComboboxSelected>>"
            key = ttk.Combobox(self.window,values=self.comboFields['names'], width=37,state = "readonly")
            
        key.grid(row=(int(self.value['fields'][3]) + 1), column=int(self.value['fields'][4]), padx=10, pady=2)
        self.key = key

        label_error['label_error' + self.value['fields'][3]] = ttk.Label(self.window, foreground='red')
        label_error['label_error' + self.value['fields'][3]].grid(row=int(self.value['fields'][3]), column=0, sticky='E', padx=5)
                
        key.bind(action, lambda event, label=list(label_error.values())[0],entry=self.key: FormValidation.remove_label_error(entry,label))
        if self.value['fields'][1] == 'price':
            action = "<KeyRelease>"
            key.bind(action, lambda event, label=list(label_error.values())[0], entry=self.key: FormValidation.validate_only_numeric(entry.get(), label, entry))
        
        self.labelError = label_error
        
        return [self.key,self.labelError]
    
    def OrcamentoItensFields(self,itens_entry_keys_model,itens_entry_keys):
        for key,value in itens_entry_keys_model.items():
            options = ''
            if value['fields'][1] == 'combo':
                options = value['options']   
            self.key = key
            self.value = value
            self.comboFields = options
            self.fields()
        return True


