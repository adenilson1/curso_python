# method vs @classmethod vs @staticmethod
# method - self, método de instancia
# @classmethod - cls, médoto de classe 
# @staticmethod - método estático (xself, xcls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def sert_user(self, user):
        self.user= user
    
    def sert_password(self, password):
        self.password= password

    
    @classmethod
    def create_with_auth(cls, user, password):
        connection= cls()
        connection.user= user
        connection.password = password
        return connection

    @staticmethod
    def logo(msg):
        print('LOG',msg)

    

# c1 = Connection()
c1 = Connection.create_with_auth('Pedro', '1234')
# c1.sert_user('Pedro')
# c1.sert_password('123')
print(Connection.logo('Essa é a mensagem'))
print(c1.user)
print(c1.password)