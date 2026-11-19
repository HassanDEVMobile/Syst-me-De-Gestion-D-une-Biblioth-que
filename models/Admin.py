

class Admin :
    
    def __init__(self,id,code_admin,email,mot_de_passe):
        self.id = id 
        self.code_admin = code_code_admin
        self.email = email
        self.mot_de_passe = mot_de_passe
        
    
    def update(self,email,mot_de_passe):
        self.email = email
        self.mot_de_passe = mot_de_passe
        return self.email,self.mot_de_passe