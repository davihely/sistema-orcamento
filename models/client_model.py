from database.connection import BD

class ClientModel():
    
    def __init__(self):
        self.bdconnection = BD()

    def insertClient(self, insertData):
        self.bdconnection.insert(insertData, 'clientes')
        
    def list_all_clients(self):
        return self.bdconnection.list('clientes')
        

    
    
