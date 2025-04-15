import tkinter as tk
import controllers.budget_controller as BudgetController
from views.budget_itens_form import BudgetItensForm

class BudgetForm():
    
    def __init__(self):
        super().__init__()
        self.window = tk.Toplevel()
        self.make_budget()
        
    def make_budget(self): 
        self.window.title("Cadastro de Orçamento")
        self.window.geometry('800x560')
        
        budget_controller_obj = BudgetController.BudgetController(self.window)
        budget_controller_obj.make_budget_form()
        
        BudgetItensForm(self.window,budget_controller_obj)
            
        botao_salvar = tk.Button(self.window, text="Salvar Orçamento", command=lambda: budget_controller_obj.validate_budget_and_itens_form())
        botao_salvar.grid(row=18, column=0, pady=20)  
        

         
          
         
        

    

    