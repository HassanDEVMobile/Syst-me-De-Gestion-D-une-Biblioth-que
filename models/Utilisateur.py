

class Utilisateur :
    
    def __init__(self,numero_abonner,nom,prenom,date_naiss,adresse,statut):
        self.numero_abonner = numero_abonner
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.adresse = adresse
        self.statut = statut 
    
    def __init__(self,id,nom,prenom,date_naiss,adresse,statut): 
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.adresse = adresse
        self.statut = statut 
        self.id = id 
        
    def to_tuple(self):
        return self.numero_abonner,self.nom,self.prenom,self.date_naiss,self.adresse,self.statut


utilisateur = Utilisateur("BT008","Diabagate","Hassane ILias","2007-04-25","Abidjan","inactif")
print(utilisateur.to_tuple())