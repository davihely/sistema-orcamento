import models.client_model as client_model
from views.make_auto_form import AutoForm

class ClientController():
    def __init__(self,window):
        self.client_form_fields = {
            'nome_cliente': {
                'fields': ['Nome / Razão Social', 'string', 'regular', 0, 0, 'e']
            },
            'cpfcnpj_cliente': {
                'fields': ['CPF / CNPJ:', 'string', 'cpfcnpj', 2, 0, 'e']
            },
            'telefone_cliente': {
                'fields': ['Telefone', 'string', 'tel', 4, 0, 'e']
            },
            'email_cliente': {
                'fields': ['E-mail', 'string', 'email', 6, 0, 'e']
            },
            'cidade_cliente': {
                'fields': ['Cidade', 'string', 'regular', 8, 0, 'e']
            },
            'estado_cliente': {
                'fields': ['Estado', 'string', 'regular', 10, 0, 'e']
            }
        }
        
        self.client_model_obj = client_model.ClientModel()
        self.auto_form_obj = AutoForm(window, self.client_form_fields)
    
    def make_client_form(self):
        self.auto_form_obj.fields()
        
    def validate_client(self):
        if self.auto_form_obj.validate_form_fields():
            widget_values = self.auto_form_obj.get_final_values()
            self.client_model_obj.insertClient(widget_values)
           


        

