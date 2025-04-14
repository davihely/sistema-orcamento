import models.budget_model as budget_model
import models.client_model as client_model
import controllers.budget_itens_controller as budget_itens_controller
from views.make_auto_form import AutoForm


class BudgetController():
    def __init__(self,window):
        self.budget_itens = []
        self.budget_model_obj = budget_model.BudgetModel()
        self.budget_form_fields = {
            'cliente_orcamento': {
                'fields': ['Cliente:', 'combo', 'regular', 0, 0],
                'options': self.get_clients_for_combo()
            },
            'valor_orcamento': {
                'fields': ['Valor Total:', 'string', 'price', 2, 0]
            }
        }
        self.auto_form_obj = AutoForm(window, self.budget_form_fields)
        self.budget_widgets_ = []
        
    def get_clients_for_combo(self):
        clients_dict: dict = {}
        client_model_obj = client_model.ClientModel()
        all_clients = client_model_obj.list_all_clients()
        client_id_list = []
        client_name_list = []
        
        for client in all_clients:
            client_id_list.append(client[0])
            client_name_list.append(client[1])
            clients_dict['ids'] = client_id_list
            clients_dict['names'] = client_name_list
            
        return clients_dict
    
    def make_budget_form(self):
        self.budget_widgets_index = self.auto_form_obj.fields()
        
    def validate_budget_form(self):
        widget_values = self.auto_form_obj.validate_form_fields()
        if widget_values:
            widget_values = self.auto_form_obj.get_final_values()
            self.budget_model_obj.insert_budget(widget_values)    
        
    def add_budget_itens(self, item):
        self.budget_itens.append(item)

        

        
        