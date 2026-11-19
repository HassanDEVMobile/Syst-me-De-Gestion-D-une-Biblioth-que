
import sqlite3

class LivreRepository:
    
    #Table Livre
    def livre_table(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete ="""
            CREATE TABLE Livre (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                auteur TEXT NOT NULL,
                isbn TEXT NOT NULL,
                annee_pub DATE NOT NULL,
                nombres_exemp INTEGERS NOT NULL,
                categorie NOT NULL,
                statut TEXT  NOT NULL
            )
            """
            cursor = con.cursor()
            cursor.execute(requete)
            
    
    #Ajout d'un livre 
    def livre_insert(self,livre):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "INSERT INTO Livre (titre,auteur,isbn,annee_pub,nombre_exemp,categorie,statut) VALUES (?,?,?,?,?,?,?)"
            cursor = con.cursor()
            cursor.execute(requete,livre)
            con.commit()
            
    
    #Modification d'un livre 
    def livre_update(self,livre):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "UPDATE Livre SET titre = ? , auteur = ? , isbn = ? , annee_pub = ? , nombre_exemp = ? , statut = ? WHERE id = ? "
            cursor = con.cursor()
            cursor.execute(requete,livre)
            con.commit()
            
            
    #Recherche d'un livre a partir du titre 
    def livre_find_one(self,titre):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT titre , auteur , isbn , annnee_pub , nombre_exemp, categorie , statut  FROM livre WHERE titre = ? "
            cursor = con.cursor()
            resultat = cursor.execute(requete,(titre,))
            return resultat.fetchone()
        
    
    #Suppression d'un livre 
    def livre_delete(self,id):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "DELETE FROM Livre WHERE id = ? "
            cursor = con.cursor()
            cursor.execute(requete,(id,))
       
        
    #Rechercher tous les livres 
    def livre_find_all(self):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT * FROM Livre "
            cursor = con.cursor()
            resultat = cursor.execute(requete)
            return resultat.fetchall()
         
            
    #Rechercher des livres par catégorie 
    def livre_find_all_categorie(self,categorie):
        with sqlite3.connect('Bibliotheques.db') as con :
            requete = "SELECT titre , auteur , isbn , annnee_pub , nombre_exemp, statut FROM Livre WHERE categorie = ?  "
            cursor = con.cursor()
            resultat = cursor.execute(requete)
            return resultat.fetchall()