import models.budget_model as budget_model
import models.product_model as product_model
from views.make_auto_form import AutoForm
import controllers.budget_controller as budget_controller

class BudgetItensController():
    def __init__(self,window, budget_controller_obj):
        self.budget_model_obj = budget_model.BudgetModel()
        self.budget_controller_obj = budget_controller_obj
        self.budget_itens_form_fields = {
            'produto_item': {
                'fields': ['Produto:', 'combo', 'regular', 4, 0],
                'options': self.get_products_for_combo()
            },
            'quantide_item': {
                'fields': ['Quantidade:', 'string', 'regular', 4, 1]
            },
            'valor_item': {
                'fields': ['Valor Total Item:', 'string', 'regular', 4, 2]
            }
        }
        self.window = window
        self.budget_itens_widgets_index = []
        self.number_of_itens = 0
        
    def get_products_for_combo(self):
        products_dict: dict = {}
        client_model_obj = product_model.ProductModel()
        all_products = client_model_obj.list_all_products()
        products_id_list = []
        products_name_list = []
        
        for product in all_products:
            products_id_list.append(product[0])
            products_name_list.append(product[1])
            products_dict['ids'] = products_id_list
            products_dict['names'] = products_name_list
            
        return products_dict
    
    def make_budget_item_form(self):
        auto_form_obj = AutoForm(self.window, self.budget_itens_form_fields)
        if self.number_of_itens > 0:
            for key,value in self.budget_itens_form_fields.items():
                self.budget_itens_form_fields[key]['fields'][3] = (2 * self.number_of_itens) + value['fields'][3]
        self.budget_widgets_index = auto_form_obj.fields()
        if self.budget_widgets_index:
            self.number_of_itens += 1 
        self.budget_controller_obj.add_budget_itens(auto_form_obj)



         
        