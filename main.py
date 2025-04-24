from tkinter import *
from tkinter import ttk
from random import choice
from views.client_form import ClientForm
from views.product_form import ProductForm
from views.budget_form import BudgetForm

root = Tk()
root.geometry("1000x600")
root.title("Sistema")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_buttons = Frame(root)
frame_buttons.grid(row=0, column=0, padx=20, pady=20, sticky="w")

Button(frame_buttons, text="Novo Cliente", command=lambda: ClientForm(), height=2, width=12).pack(side=LEFT, padx=10)
Button(frame_buttons, text="Novo Produto", command=lambda: ProductForm(), height=2, width=12).pack(side=LEFT, padx=10)
Button(frame_buttons, text="Novo Orçamento", command=lambda: BudgetForm(), height=2, width=14).pack(side=LEFT, padx=10)

frame_table = Frame(root, padx=20, pady=20)
frame_table.grid(row=1, column=0, sticky="nsew")

table = ttk.Treeview(frame_table, columns=('code', 'client', 'total_value', 'item_quant'), show='headings')
table.heading('code', text='Código')
table.heading('client', text='Cliente')
table.heading('total_value', text='Valor Total')
table.heading('item_quant', text='Quantidade de Itens')
table.pack(fill=BOTH, expand=True, side=LEFT)

scrollbar = ttk.Scrollbar(frame_table, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

code_ar = ['001', '002', '003', '004']
client_ar = ['Maria', 'João', 'Carlos', 'Ana']
total_value_ar = ['R$1200', 'R$980', 'R$450', 'R$600']
item_quant_ar = ['10', '5', '2', '8']

for i in range(20):
    code = choice(code_ar)
    client = choice(client_ar)
    total_value = choice(total_value_ar)
    item_quant = choice(item_quant_ar)
    table.insert('', END, values=(code, client, total_value, item_quant))

def delete_selected():
    print('delete')

def show_details():
    print('details')

def edit_selected():
    print('edit')

frame_actions = Frame(root)
frame_actions.grid(row=2, column=0, pady=(0, 20))

Button(frame_actions, text="Detalhes", command=show_details, width=15).pack(side=LEFT, padx=10)
Button(frame_actions, text="Alterar", command=edit_selected, width=15).pack(side=LEFT, padx=10)
Button(frame_actions, text="Deletar", command=delete_selected, width=15).pack(side=LEFT, padx=10)

root.mainloop()
