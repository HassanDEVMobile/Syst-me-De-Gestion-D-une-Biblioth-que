

class Livre :
    
    def __init__(self,id,titre,auteur,isbn,annee_pub,nombres_exemplaires,categorie,statut):
        self.id = id 
        self.titre = titre 
        self.auteur = auteur 
        self.isbn = isbn 
        self.annee_pub = annee_pub
        self.nombres_exemplaires = nombres_exemplaires
        self.categorie = categorie
        self.statut = statut
        
    def update(self,titre,auteur,isbn,annee_pub,nombres_exemplaires,statut):
        self.titre = titre 
        self.auteur = auteur 
        self.isbn = isbn 
        self.annee_pub = annee_pub
        self.nombres_exemplaires = nombres_exemplaires
        self.statut = statut
        return self.titre,self.auteur,self.isbn,self.annee_pub,self.nombres_exemplaires,self.statut