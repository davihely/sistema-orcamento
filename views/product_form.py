import tkinter as tk
import controllers.product_controller as ProductController
       
class ProductForm():
    
    def __init__(self):
        super().__init__()
        self.window = tk.Toplevel()
        self.create_fields()
        
    def create_fields(self): 
        self.window.title("Cadastro de Produtos")
        self.window.geometry('270x560')
        
        product_controller_obj = ProductController.ProductController(self.window)
        product_controller_obj.make_product_form()
                    
        botao_salvar = tk.Button(self.window, text="Salvar Produto", command=lambda: product_controller_obj.validate_product())
        botao_salvar.grid(row=18, column=0, pady=20)    

    

    