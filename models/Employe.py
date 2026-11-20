

class Employe :
    
    def __init__(self,code_employe,email,mot_de_passe):
        self.code_employe = code_employe
        self.email = email
        self.mot_de_passe = mot_de_passe
        
    def update(self,email,mot_de_passe):
        self.email = email
        self.mot_de_passe = mot_de_passe
        return self.email,self.mot_de_passe