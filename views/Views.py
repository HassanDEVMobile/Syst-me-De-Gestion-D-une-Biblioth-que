


class view :
    
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
        2. Gestionnaire d'un abonné
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
        print("=====CONNEXION=====")
        email = input("Entrer votre email : ")
        if self.verifier_email(email) == True :
            mot_de_passe = input("Entrer votre mot de passe : ")
            if self.verifier_mot_de_passe(mot_de_passe):
                self.menu_principale_admin()
    
    def verifier_email(self,email):
        pass