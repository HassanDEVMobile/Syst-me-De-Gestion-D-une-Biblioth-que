
from datetime import datetime

class Views :
    
    #Menu principale pour les employers
    def menu_principale_employe(self):
        menu = """
        === SYSTEME DE GESTION DE BIBLIOTHEQUE ===
        1. Gestionnaire des livres 
        2. Gestionnaire d'un abonné
        3. Effectuer un emprunt
        4. Enregistrer un retour de livre
        5. Consulter la liste des emprunts en cours
        0. Quitter
        """
        print(menu)
        return int(input("Veuillez faire un choix : "))
    
    
    
    #Menu Principale pour les Administrateurs
    def menu_principale_admin(self):
        menu = """
        === SYSTEME DE GESTION DE BIBLIOTHEQUE ===
        1. Gestionnaire des livres 
        2. Gestionnaire des abonné
        3. Effectuer un emprunt
        4. Enregistrer un retour de livre
        5. Consulter la liste des emprunts en cours
        6-Gestionnaire des employers
        0. Quitter
        """
        print(menu)
        return int(input("Veuillez faire un choix : "))
    
    
    #Interface de connexion pour les administrateurs et les employers 
    def interface_connexion(self):
        connexion = """=====CONNEXION=====
                 1-Se connecter 
                 0-Quitter 
              """.strip()
        print(connexion)
        return int(input("Veuillez faire un choix : "))
            
        
    """
    ***On saisie l'email puis ont va verifier si l'email existe dans le controller 
    ***Si l'email existe alors ont va afficher l'interface de saisir de mot de passe
    """
    def interface_saisie_email_connexion(self):
        return input("Veuillez saisir votre email : ")
        
    
    #On saisir le mot le mot de passe 
    def interface_saisie_mot_de_passe_connexion(self):
        return input("Veuillez saisir votre mot de passe : ")
    
    
    #On affiche une erreur si l'email est faux
    def message_erreur_email(self):
        print("Email incorrect !")
    
    #On affiche une erreur si le mot de passe est faux
    def message_erreur_mdp(self):
        print("Mot de passe incorrect !")
        
    
    """
    Fonctionnalité Abonner 
    """
    #Interface de gestion des abonnés
    def interface_gestion_abonner(self):
        menu_gestion_abonner="""
        ========================================
               GESTIONNAIRES DES ABONNEES   
        ========================================
        1-Enregistré un nouvelle abonné 
        2-Modifier un abonner 
        3-Consulter un abonné 
        4-Supprimer un abonné
        5-Afficher tous les abonnés 
        0-Quitter
        """
        print(menu_gestion_abonner.strip())
        return int(input("Veuillez faire un choix : "))
    
    #Enregistrement d'un abonné
    def interface_enregistrement_abonner(self):
        affiche="========Enregistrement======="
        print(affiche.strip())
        numero_abonner = input("Entrer le numéro de l'abonner(Format BBL-xxx) :")
        nom = input("Entrer le nom de l'abonner :")
        prenom = input("Entrer le prenom de l'abonner :")   
        date_naiss = self.saisie_date()
        adresse = input("Entrer l'adresse de labonner : ")
        statut = input("Entrer le statut de l'abonner")
        return numero_abonner,nom,prenom,date_naiss,adresse,statut
    
    #Modification d'un abonné 
    def interface_modification_abonner(self):
        affiche="========Modification======="
        print(affiche.strip())
        nom = input("Entrer le nom de l'abonner :")
        prenom = input("Entrer le prenom de l'abonner :")   
        date_naiss = self.saisie_date()
        adresse = input("Entrer l'adresse de labonner : ")
        statut = input("Entrer le statut de l'abonner")
        return nom,prenom,date_naiss,adresse,statut
    
    #On saisie le numéro d'abonnement pour l'abonner dont ont veut faire la modification
    def interface_saisie_num_abonner_modif(self):
        return input("Entrer le numéro d'abonnement de l'abonner à modifier : ")
    
    #Consultation d'un abonné
    def interface_consultation_abonner(self,abonner):
        affiche="========Consultation======="
        print(affiche.strip())
        print(f"Numéro d'abonnement : {abonner[0]} | Nom : {abonner[1]} | Prenom : {abonner[2]} | Date de naissance :  {abonner[3]} | Adresse :  {abonner[4]} | statut : {abonner[5]}")
    
    #Interface de saisie pour rechercher un abonné 
    def interface_saisie_consultation(self):
       return int(input("Veuillez saisir l'id de l'abonné : "))
   
    #Interface affichant la liste de tous les abonnés avec id pour la recherche d'un aboné 
    def interface_liste_abonner_rech_id(self,liste_abonner):
        for abonner in liste_abonner:
            print(f"id : {abonner[0]} | Numéro abonnement : {abonner[1]} | Nom : {abonner[2]} | prenom : {abonner[3]}")
          
    #Interface de suppression d'un abonner 
    def interface_suppression_abonner(self):
        return int(input("Entrer l'id de l'abonné à supprimer : "))
    
    #Interface qui liste tous les abonnés
    def interface_liste_abonner(self,list_abonner):
        for abonner in list_abonner:
            print(f"Numéro abonnement : {abonner[0]} | Nom : {abonner[1]} | Prenom : {abonner[2]} | Date de naissance : {abonner[3]} | Adresse : {abonner[4]} | Statut : {abonner[5]}")
          
    
    #Methode de saisie de date et de verfication
    def saisie_date(self):
        format_accepter = "%Y-%m-%d"
        while True:
            date = input("Entrer la date de naissance de l'abonner(format yy-mm-dd) : ")
            try:
                date_valide = datetime.strptime(date,format_accepter)
                return date_valide
            except ValueError :
                print("Format de date incorrect ou date inexistante dans le calendrier ")
    
    
    
    #Menu de Gestion des Livres
    def interface_gestion_livre(self):
        menu_gestion_livre="""
        ========================================
               GESTIONNAIRES DES ABONNEES   
        ========================================
        1-Enregistré un nouveau livre
        2-Modifier un livre 
        3-Consulter un livre
        4-Supprimer un livre
        5-Afficher tous les livres 
        0-Quitter
        """
        print(menu_gestion_livre.strip())
        return int(input("Veuillez faire un choix : "))