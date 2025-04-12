from database.connection import BD

class Client():
    
    def __init__(self):
        self.bdconnection = BD()

    def insertClient(self, insertData):
        self.bdconnection.insert(insertData, 'clientes')
        
    def listClients(self):
        return self.bdconnection.list('clientes')
        

    
    
