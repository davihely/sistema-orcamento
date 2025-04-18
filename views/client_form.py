import tkinter as tk
import controllers.client_controller as ClientController
       
class ClientForm():
    
    def __init__(self):
        super().__init__()
        self.window = tk.Toplevel()
        self.make_client()
        
    def make_client(self): 
        self.window.title("Cadastro de Clientes")
        self.window.geometry('270x560')
        
        client_controller_obj = ClientController.ClientController(self.window)
        client_controller_obj.make_client_form()
                    
        botao_salvar = tk.Button(self.window, text="Salvar Cliente", command=lambda: client_controller_obj.validate_client())
        botao_salvar.grid(row=18, column=0, pady=20)   

    

    