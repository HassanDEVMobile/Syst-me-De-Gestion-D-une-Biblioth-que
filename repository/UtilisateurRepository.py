
from models.Utilisateur import Utilisateur
import sqlite3

class UtilisateurRepository:
    
    #Création de la table utilisateur
    def utilisateur_table(self):
        con = sqlite3.connect('Bibliotheque.db')
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE Utilisateur(
            id PRIMARY KEY AUTOINCREMENT,
            numeroAbonner TEXT UNIQUE NOT NULL , 
            nom TEXT NOT NULL , 
            prenom TEXT NOT NULL,
            dateNaiss DATE NULL ,
            adress NOT NULL,
            statut TEXT NULL                
            )
                """)
        con.close()
        
        
     #Insertion d'un utilisateur   
    def utilisateur_insert(self,utilisateur):  
        self.utilisateur()
        con = sqlite3.connect('Bibliotheque.db')
        cursor = con.cursor()
        cursor.execute(" INSERT INTO Utilisateur(?,?,?,?,?,?)",utilisateur)
        con.commit()
        con.close()
        
        
    #Modification d'un utilisateur
    def utilisateur_update(self,id):
        self.utilisateur()
        con = sqlite3.connect('Bibliotheque.db')
        cursor = con.cursor()
        cursor.execute("""
                       UPDATE Utilisateur
                       SET
                       nom = ? 
                       prenom = ? 
                       dateNaiss = ? 
                       
                       """)
        

"""
utilisateurRepository = UtilisateurRepository()
utilisateur = Utilisateur("BBT-001","Diabagate","Hassane ILias","2007-04-25","Grand-Bassam","actif")
utilisateurRepository.utilisateur_insert(tuple(utilisateur__dict__.values()))
"""