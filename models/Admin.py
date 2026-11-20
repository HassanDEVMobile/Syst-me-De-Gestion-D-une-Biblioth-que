

class Admin :
    
    def __init__(self,code_admin,email,mot_de_passe):
        self.code_admin = code_admin
        self.email = email
        self.mot_de_passe = mot_de_passe
        
    
    def update(self,email,mot_de_passe,id):
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.id = id
        return self.email,self.mot_de_passe,self.id