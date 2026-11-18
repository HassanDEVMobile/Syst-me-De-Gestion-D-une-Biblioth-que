
from models.Utilisateur import Utilisateur
import sqlite3

class UtilisateurRepository:
    
    #Création de la table utilisateur
    def utilisateur_table(self):
     with sqlite3.connect('Bibliotheques.db') as con :
        cursor = con.cursor()
        #cursor.execute("DROP TABLE IF EXISTS Utilisateur")
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
        
        with sqlite3.connect('Bibliotheques.db') as con :
            cursor = con.cursor()
            cursor.execute(" INSERT INTO Utilisateur(numeroAbonner,nom,prenom,dateNaiss,adress,statut) VALUES (?,?,?,?,?,?)",utilisateur)
            con.commit()
            
    
    #Modification d'un utilisateur
    def utilisateur_update(self,utilisateur):
        requete = "UPDATE Utilisateur SET nom = ? , prenom = ?, date_naiss = ? , adress = ? , statut = ? WHERE id = ? "
        with sqlite3.connect('Bibliotheque.db') as con :
            cursor = con.cursor()
            cursor.execute(requete,utilisateur)
            con.commit()
           
    
    
        
        
        
utilisateurRepository = UtilisateurRepository()
utilisateur = Utilisateur("BT008","Diabagate","Hassane ILias","2007-04-25","Abidjan","inactif")
print(utilisateur.to_tuple())
utilisateurRepository.utilisateur_update(utilisateur.update("Hassan","diaba","2025-11-12","Grand Bassam","actif",1)) 