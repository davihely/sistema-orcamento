from database.connection import BD

class BudgetModel():
    
    def __init__(self):
        self.bdconnection = BD()

    def insert_budget(self, insert_data):
        return self.bdconnection.insert(insert_data, 'orcamentos')
        
    def insert_itens_budget(self, insert_data):
        for each in insert_data:
            self.bdconnection.insert(each, 'orcamento_itens')
        
    
