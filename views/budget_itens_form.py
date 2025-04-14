import tkinter as tk
import controllers.budget_itens_controller as BudgetItensController

class BudgetItensForm():
    
    def __init__(self,window,budget_controller_obj):
        super().__init__()
        self.budget_controller_obj = budget_controller_obj
        self.window = window
        self.make_budget_itens()
        
    def make_budget_itens(self): 
        budget_itens_controller_obj = BudgetItensController.BudgetItensController(self.window,self.budget_controller_obj)
        
        button_new_item = tk.Button(self.window, text="Novo Item", command=lambda: budget_itens_controller_obj.make_budget_item_form())
        button_new_item.grid(row=20, column=0, pady=20)     
          
        button_new_item2 = tk.Button(self.window, text="Novo Item", command=lambda: budget_itens_controller_obj.validate_budget_item_form())
        button_new_item2.grid(row=25, column=0, pady=20)     
         
        

    

    