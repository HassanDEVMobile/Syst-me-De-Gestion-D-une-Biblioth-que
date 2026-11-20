

import sqlite3

class EmployeRepository :
    
    #Création de table Employe 
    def __init__(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = " CREATE TABLE IF NOT EXISTS Employe (id INTEGER PRIMARY KEY AUTOINCREMENT,codeEmploye TEXT UNIQUE NOT NULL,email TEXT UNIQUE NOT NULL,motDePasse TEXT NOT NULL)"
            cursor = con.cursor()
            cursor.execute(requete)
            
    
    #Ajout d'un employe
    def employe_insert(self,employe):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "INSERT INTO Employe (codeEmploye,email,motDePasse) VALUES (?,?,?)"
            cursor = con.cursor()
            cursor.execute(requete,employe)
            con.commit()
            
            
    #Modification d'un employe 
    def employe_update(self,employe):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "UPDATE Employe SET email = ? , motDePasse = ? WHERE id = ?"
            cursor = con.cursor()
            cursor.execute(requete,employe)
            con.commit()
            
    
    #Recherche d'un employe 
    def employe_find_one(self,id):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Employe WHERE id = ? "
            cursor = con.cursor()
            resultat = cursor.execute(requete,(id,))
            return resultat.fetchone()


    #Rechercher tous les employe 
    def employe_find_all(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Employe "
            cursor = con.cursor()
            resultat = cursor.execute(requete)
            return resultat.fetchall()
        
    
    #Verifier l'email d'un employer 
    def employe_verifier_email(self,email):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Employe WHERE email = ?"
            cursor = con.cursor()
            resultat = cursor.execute(requete,(email,))
            return resultat.fetchone() is None  
        
        
    #Verifier le mot de passe d'un employer 
    def employer_verifier_mot_de_passe(self,email,mot_de_passe):
         with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Employe WHERE email = ? AND motDePasse = ? "
            cursor = con.cursor()
            resultat = cursor.execute(requete,(email,mot_de_passe))
            return resultat.fetchone() is None
        