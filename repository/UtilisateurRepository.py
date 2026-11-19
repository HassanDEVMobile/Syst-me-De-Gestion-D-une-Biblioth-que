
from models.Utilisateur import Utilisateur
import sqlite3

class UtilisateurRepository:
    
    #Création de la table utilisateur
    def utilisateur_table(self):
     with sqlite3.connect('Bibliotheques.db') as con :
        cursor = con.cursor()
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
            requete = " INSERT INTO Utilisateur(numeroAbonner,nom,prenom,dateNaiss,adress,statut) VALUES (?,?,?,?,?,?)"
            cursor = con.cursor()
            cursor.execute(requete,utilisateur)
            con.commit()
            
    
    #Modification d'un utilisateur
    def utilisateur_update(self,utilisateur):
        requete = "UPDATE Utilisateur SET nom = ? , prenom = ?, dateNaiss = ? , adress = ? , statut = ? WHERE id = ? "
        with sqlite3.connect('Bibliotheques.db') as con :
            cursor = con.cursor()
            cursor.execute(requete,utilisateur)
            con.commit()
    
    
    #Recherche d'un utilisateur
    def utilisateur_find_one(self,id):
        
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Utilisateur WHERE id = ?"
            cursor = con.cursor()
            resultat = cursor.execute(requete,(id,))
            return resultat.fetchone()
        
        
    #suppression d'un utilisateur
    def utilisateur_delete(self,id):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "DELETE FROM utilisateur WHERE id = ?"
            cursor = con.cursor()
            cursor.execute(requete,(id,))
            
    
    #Recherhcher tous les utilisateurs 
    def utilisateur_find_all(self):
        with sqlite3.connect('Bibliotheques.db') as con : 
            requete = "SELECT * FROM Utilisateur ORDER BY nom"
            cursor = con.cursor()
            resultat =  cursor.execute(requete)
        return resultat.fetchall()
    