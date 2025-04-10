import tkinter as tk
from tkinter import ttk
import screens.ClientFormScreen as clientform
import screens.ProductFormScreen as productform
import database.connection as conection

def clicar():
    botao.config(text="Botão pressionado!")

root = tk.Tk() 
root.geometry("1000x600") 
root.title("Sistema")

botao = tk.Button(root, text="Novo Cliente", command=lambda: clientform.ClientForm())
botao.config(height = 2, width = 12)
botao.place(x=50,y=50)

botao = tk.Button(root, text="Novo Produto/Serviço", command=lambda: productform.ProductForm())
botao.config(height = 2, width = 20)
botao.place(x=160,y=50)

botao = tk.Button(root, text="Orçamento", command=clicar)
botao.config(height = 2, width = 12)
botao.place(x=330,y=50)

table = ttk.Treeview(root, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.place(x=50, y=120, width=600, height=400)
for i in range(100):
    data = ("dsadas")
    table.insert(parent = '', index = 0, values = data)
root.mainloop()
    