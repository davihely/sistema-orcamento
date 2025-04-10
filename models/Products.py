from database.connection import BD

class Products():
    
    def __init__(self):
        self.bdconnection = BD()

    def insertProduct(self, insertData):
        self.bdconnection.insert(insertData, 'produtos')

    