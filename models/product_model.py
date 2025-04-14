from database.connection import BD

class ProductModel():
    
    def __init__(self):
        self.bdconnection = BD()

    def insertProduct(self, insertData):
        self.bdconnection.insert(insertData, 'produtos')

    def list_all_products(self):
        return self.bdconnection.list('produtos')