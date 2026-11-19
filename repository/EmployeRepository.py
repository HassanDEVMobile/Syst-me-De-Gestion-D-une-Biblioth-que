

import sqlite3

class EmployeRepository :
    
    #Création de table Employe 
    def employe_table(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = """
            CREATE TABLE Employe (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codeEmploye TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                motDePasse TEXT NOT NULL,
                statut TEXT
            )
            """
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