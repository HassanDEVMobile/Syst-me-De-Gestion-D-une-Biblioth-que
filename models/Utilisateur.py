

class Utilisateur :
    
    #Création d'un objet utilisateur pour faire l'insertion en BD 
    def __init__(self,numero_abonner,nom,prenom,date_naiss,adresse,statut):
        self.numero_abonner = numero_abonner
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.adresse = adresse
        self.statut = statut 
        
    
    #Création d'un objet utilisateur pour faire une modification en BD 
    def update(self,nom,prenom,date_naiss,adresse,statut,id):
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.adresse = adresse
        self.statut = statut 
        self.id = id 
        return self.nom,self.prenom,self.date_naiss,self.adresse,self.statut,id
        
        
        
    def to_tuple(self):
        return self.numero_abonner,self.nom,self.prenom,self.date_naiss,self.adresse,self.statut


