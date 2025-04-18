from database.connection import BD

class BudgetModel():
    
    def __init__(self):
        self.bdconnection = BD()

    def insert_budget(self, insert_data):
        return self.bdconnection.insert(insert_data, 'orcamentos')
        
    def insert_itens_budget(self, insert_data):
        tuple_insert = []
        for each in insert_data:
            each.insert(0,'')
            tuple_insert.append(tuple(each))
            each.remove('')
        self.bdconnection.insert_multiple_rows(tuple_insert, 'orcamento_itens')
        
    def delete_budget(self, id):
        self.bdconnection.delete(id, 'id_orcamento', 'orcamentos')