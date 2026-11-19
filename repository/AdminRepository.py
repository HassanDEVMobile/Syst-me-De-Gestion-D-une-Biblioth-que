
import sqlite3

class AdminRepository:
    
     #Création de table Admin
    def admin_table(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = """
            CREATE TABLE Admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codeAdmin TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                motDePasse TEXT NOT NULL,
                statut TEXT
            )
            """
            cursor = con.cursor()
            cursor.execute(requete)
            
    
    #Ajout d'un Admin 
    def employe_insert(self,Admin):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "INSERT INTO Admin (codeAdmin,email,motDePasse) VALUES (?,?,?)"
            cursor = con.cursor()
            cursor.execute(requete,employe)
            con.commit()
            
            
    #Modification d'un Admin
    def employe_update(self,Admin):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "UPDATE Admin SET email = ? , motDePasse = ? WHERE id = ?"
            cursor = con.cursor()
            cursor.execute(requete,employe)
            con.commit()
            
    
    #Recherche d'un Admin
    def employe_find_one(self,id):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT emails FROM Admin WHERE id = ? "
            cursor = con.cursor()
            resultat = cursor.execute(requete,(id,))
            return resultat.fetchone()


    #Rechercher tous les Admin
    def employe_find_all(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT emails FROM Admin "
            cursor = con.cursor()
            resultat = cursor.execute(requete)
            return resultat.fetchall()