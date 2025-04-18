import tkinter as tk
from tkinter import ttk
from .Validation import FormValidation

class AutoForm():
    def __init__(self,window,form_dict):
        self.window = window
        self.form_dict = form_dict
        self.widget_list = []
        
    def fields(self):
        for key,value in self.form_dict.items(): 
            tk.Label(self.window,text=value['fields'][0], anchor="w").grid(row=value['fields'][3],column=value['fields'][4],sticky="w",padx=10,pady=(10, 0))
            action = "<Key>"
            var = ''
            combo_ids = ''
            if value['fields'][1] == 'string':
                var = tk.StringVar()
                widget = tk.Entry(self.window,width=40,textvariable=var)
            elif value['fields'][1] == 'combo':
                action = "<<ComboboxSelected>>"
                widget = ttk.Combobox(self.window,values=value['options']['names'],width=37,state="readonly")   
                combo_ids = value['options']['ids']
                
            widget.grid(row=(value['fields'][3] + 1), column=value['fields'][4], padx=10, pady=2)
            
            label_error = ttk.Label(self.window, foreground='red')
            label_error.grid(row=value['fields'][3], column=value['fields'][4], sticky='E', padx=5)
            
            self.widget_list.append([widget,label_error,combo_ids,var])

            match value['fields'][5]:
                case 'e':
                    widget.config(state='normal')
                case 'd':
                    widget.config(state='disabled')
            
            widget.bind(action, lambda event, label=label_error,widget=widget: FormValidation.remove_label_error(widget,label))
            
            if value['fields'][2] == 'price':
                action = "<KeyRelease>" 
                widget.bind(action, lambda event, label=label_error, widget=widget: FormValidation.validate_only_numeric(widget.get(),label,widget))
        return True
    
    def validate_form_fields(self):
        try:
            if all([bool(value[0].get()) == True for value in self.widget_list]):
                    return True
            else:
                raise Exception("Existem campos vazios")
        except Exception as error:
            for typed in self.widget_list:
                    validationObj = FormValidation(typed[0].get(), typed[1])
                    validationObj.validate_empty()
            return False

    def get_final_values(self):
        input_values = []
        combo_ids = []
        for value in self.widget_list:
            if isinstance(value[0], ttk.Combobox):
                combo_ids.append(self.get_id_combo_box(value[0],value[2]))
            input_values.append(value[0].get()) 
        input_values.extend(combo_ids)
        return input_values
    
    def get_id_combo_box(self,combo,ids):
            index = combo.current()
            id_choosen = ids[index]
            return id_choosen
        
    def get_current_widget(self):
        return self.window.focus_get()
    
    def get_all_form_widgets(self):
        return self.widget_list
    
    def set_widget_value(self,widget,value):
        widget.delete(0,'end')
        widget.insert(0, value)
        
    def set_bind(self,action,widget,function):
        widget.bind(action, lambda event: self.window.after(1, lambda: function()))
        
    def set_enable_insert_disabled(self, widget, value):
        widget.config(state="normal")
        self.set_widget_value(widget,value)
        widget.config(state="disabled")
