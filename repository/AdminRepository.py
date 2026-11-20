
import sqlite3

class AdminRepository:
    
    #Création de table Admin
    def __init__(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = " CREATE TABLE IF NOT EXISTS Admin ( id INTEGER PRIMARY KEY AUTOINCREMENT,  codeAdmin TEXT UNIQUE NOT NULL,email TEXT UNIQUE NOT NULL,  motDePasse TEXT NOT NULL)"
            cursor = con.cursor()
            cursor.execute(requete)
            
    
    #Ajout d'un Admin 
    def admin_insert(self,admin):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "INSERT INTO Admin (codeAdmin,email,motDePasse) VALUES (?,?,?)"
            cursor = con.cursor()
            cursor.execute(requete,admin)
            con.commit()
            
            
    #Modification d'un Admin
    def admin_update(self,admin):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "UPDATE Admin SET email = ? , motDePasse = ? WHERE id = ?"
            cursor = con.cursor()
            cursor.execute(requete,admin)
            con.commit()
            
    
    #Recherche d'un Admin
    def admin_find_one(self,id):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT email FROM Admin WHERE id = ? "
            cursor = con.cursor()
            resultat = cursor.execute(requete,(id,))
            return resultat.fetchone()


    #Rechercher tous les Admin
    def admin_find_all(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT email FROM Admin "
            cursor = con.cursor()
            resultat = cursor.execute(requete)
            return resultat.fetchall()
        
    
    #Verification de l'emails d'un admin
    def admin_email_verification(self,email):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Admin WHERE email = ?"
            cursor = con.cursor()
            resultat = cursor.execute(requete,(email,))
            return resultat.fetchone() is None 
     
     
    #Verification du mot de passe d'un admin
    def admin_mot_de_passe_verification(self,mot_de_passe,email):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Admin WHERE email = ? AND motDePasse = ? "
            cursor = con.cursor()
            resultat = cursor.execute(requete,(email,mot_de_passe))
            return resultat.fetchone() is None 
        


#adminRepo.admin_insert(tuple(vars(admin).values()))