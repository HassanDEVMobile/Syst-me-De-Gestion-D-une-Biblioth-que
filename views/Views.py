


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