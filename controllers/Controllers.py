
from views.Views import Views
from repository.AdminRepository import AdminRepository
from repository.EmployeRepository import EmployeRepository
from models.Admin import Admin
from models.Employe import Employe


class Controllers :
    
    #Création des instances des instances que le controllers utilisera
    def instance(self):
        self.views = Views()
        self.adminRepository = AdminRepository()
        self.employeRepository = EmployeRepository()
        return self.views,self.adminRepository,self.employeRepository
    
    
    #Logique de connexion d'un Employe ou Admin
    def authentification(self):
        views,adminRepository,employeRepository = self.instance()
        choix = views.interface_connexion()
        if choix == 1 :
            email = self.views.interface_saisie_email_connexion()
            if self.adminRepository.admin_email_verification(email) == False :
                mot_de_passe =  self.views.interface_saisie_mot_de_passe_connexion()
                if self.adminRepository.admin_mot_de_passe_verification(mot_de_passe,email) == False:
                  choix_options = self.views.menu_principale_admin()
                  return choix_options
                else :
                    #On affiche un message d'erreur pour le mot de passe admin
                    self.views.message_erreur_mdp()
            elif self.employeRepository.employe_verifier_email(email) == False:
                mot_de_passe =  views.interface_saisie_mot_de_passe_connexion()
                if self.employeRepository.employer_verifier_mot_de_passe(email,mot_de_passe) == False :
                    choix_options = self.views.menu_principale_employe()
                    return choix_options
                else :
                    #On affiche un message d'erreur pour le mot de passe employe
                     self.views.message_erreur_mdp()
            else :
                #On affiche un message d'erreur pour l'email 
                self.views.message_erreur_email()
        elif choix == 0 :
            pass
   
        
    #Methode de démarrage de l'application
    def run(self):
        self.authentification()