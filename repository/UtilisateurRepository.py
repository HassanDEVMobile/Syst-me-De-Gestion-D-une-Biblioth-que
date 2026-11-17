
from models.Utilisateur import Utilisateur
import sqlite3

class UtilisateurRepository:
    
    #Création de la table utilisateur
    def utilisateur_table(self):
     with sqlite3.connect('Bibliotheques.db') as con :
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS Utilisateur")
        cursor.execute("""
            CREATE TABLE Utilisateur(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numeroAbonner TEXT UNIQUE NOT NULL , 
            nom TEXT NOT NULL , 
            prenom TEXT NOT NULL,
            dateNaiss DATE NULL ,
            adress NOT NULL,
            statut TEXT NULL                
            )
                """)
       
        
     #Insertion d'un utilisateur   
    def utilisateur_insert(self,utilisateur):  
        self.utilisateur_table()
        with sqlite3.connect('Bibliotheques.db') as con :
            cursor = con.cursor()
            cursor.execute(" INSERT INTO Utilisateur(numeroAbonner,nom,prenom,dateNaiss,adress,statut) VALUES (?,?,?,?,?,?)",utilisateur)
            con.commit()
           
    
    
        
        
        
utilisateurRepository = UtilisateurRepository()
utilisateur = Utilisateur("BT008","Diabagate","Hassane ILias","2007-04-25","Abidjan","inactif")
print(utilisateur.to_tuple())
utilisateurRepository.utilisateur_insert(utilisateur.to_tuple()) 