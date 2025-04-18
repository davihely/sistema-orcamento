import models.product_model as product_model
from views.make_auto_form import AutoForm

class ProductController():
    def __init__(self,window):
        self.products_form_fields = {
            'nome_produto': {
                'fields': ['Nome', 'string', 'regular', 0, 0, 'e']
            },
            'descricao_produto': {
                'fields': ['Descrição', 'string', 'regular', 2, 0, 'e']
            },
            'preco_produto': {
                'fields': ['Preço', 'string', 'price', 4, 0, 'e']
            }
        }
        
        self.product_model_obj = product_model.ProductModel()
        self.auto_form_obj = AutoForm(window, self.products_form_fields)
    
    def make_product_form(self):
        self.auto_form_obj.fields()
        
    def validate_product(self):
        if self.auto_form_obj.validate_form_fields():
            widget_values = self.auto_form_obj.get_final_values()
            self.product_model_obj.insertProduct(widget_values)
           


        

