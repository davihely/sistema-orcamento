from database.connection import BD

class Orcamento():
    
    def __init__(self):
        self.bdconnection = BD()

    def insertOrcamento(self, insertData):
        print(insertData)
        self.bdconnection.insert(insertData, 'orcamentos')

    
