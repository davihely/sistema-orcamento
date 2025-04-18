import models.budget_model as budget_model
import models.product_model as product_model
from views.make_auto_form import AutoForm
import controllers.budget_controller as budget_controller
import tkinter as tk

class BudgetItensController():
    def __init__(self,window, budget_controller_obj):
        self.budget_model_obj = budget_model.BudgetModel()
        self.budget_controller_obj = budget_controller_obj
        self.products_for_combo = self.get_products_for_combo()
        self.budget_itens_form_fields = {
            'produto_item': {
                'fields': ['Produto:', 'combo', 'regular', 4, 0, 'e'],
                'options': self.products_for_combo
            },
            'valor_unitario_item': {
                'fields': ['Valor Unitário Item:', 'string', 'price', 4, 1, 'd'],
            },
            'quantide_item': {
                'fields': ['Quantidade:', 'string', 'price', 4, 2,'e']
            },
            'valor_item': {
                'fields': ['Valor Total Item:', 'string', 'price', 4, 3, 'd']
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
        products_price_list = []
        
        for product in all_products:
            products_id_list.append(product[0])
            products_name_list.append(product[1])
            products_price_list.append(product[3])
            products_dict['ids'] = products_id_list
            products_dict['names'] = products_name_list
            products_dict['price'] = products_price_list
            
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

        all_widgets = auto_form_obj.get_all_form_widgets()
             
        all_widgets[0][0].bind('<<ComboboxSelected>>', lambda event: self.window.after(1, lambda: self.set_uni_price(auto_form_obj, all_widgets)))
        all_widgets[2][0].bind('<Key>', lambda event: self.window.after(1, lambda: self.set_final_item_price(auto_form_obj, all_widgets)))
        all_widgets[3][3].trace_add('write', lambda name, index, mode: self.send_item_to_total(name, index, mode, all_widgets[3][0].get()))


    def send_item_to_total(self,var, index, mode, item_price):
        if(item_price):
            self.budget_controller_obj.set_total_value(var,item_price)
        
    def set_uni_price(self,auto_form_obj,widgets):
        item_price = auto_form_obj.get_id_combo_box(widgets[0][0],self.products_for_combo['price'])
        auto_form_obj.set_enable_insert_disabled(widgets[1][0],item_price)
        
        if(widgets[2][0].get()):
            self.set_final_item_price(auto_form_obj,widgets)
        
    def set_final_item_price(self,auto_form_obj,widgets):
        try:
            if(widgets[1][0].get() and widgets[2][0].get()):
                quantity = int(widgets[2][0].get())
                price = float(widgets[1][0].get())
                auto_form_obj.set_enable_insert_disabled(widgets[3][0], price * quantity)
            elif not widgets[2][0].get() and widgets[3][0].get():
                auto_form_obj.set_enable_insert_disabled(widgets[3][0], '')
        except ValueError as Error:
            raise(Error)



         
        