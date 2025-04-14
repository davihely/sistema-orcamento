from database.connection import BD

class BudgetModel():
    
    def __init__(self):
        self.bdconnection = BD()

    def insert_budget(self, insertData):
        self.bdconnection.insert(insertData, 'orcamentos')


    
