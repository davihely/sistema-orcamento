from tkinter import *
from tkinter import ttk
#import views.ClientFormScreen as clientform
#import views.ProductFormScreen as productform
from views.budget_form import BudgetForm

def clicar():
    botao.config(text="Botão pressionado!")

root = Tk() 
root.geometry("1000x600") 
root.title("Sistema")

#botao = tk.Button(root, text="Novo Cliente", command=lambda: clientform.ClientForm(tk.Toplevel))
#botao.config(height = 2, width = 12)
#botao.place(x=50,y=50)

#botao = tk.Button(root, text="Novo Produto/Serviço", command=lambda: productform.ProductForm())
#botao.config(height = 2, width = 20) 
#botao.place(x=160,y=50)
botao = Button(root, text="Novo Orçamento", command=lambda: BudgetForm())
botao.config(height = 2, width = 12)    
botao.place(x=330,y=50)

table = ttk.Treeview(root, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.place(x=50, y=120, width=600, height=400)
for i in range(100):
    data = ("dsadas")
root.mainloop()
    