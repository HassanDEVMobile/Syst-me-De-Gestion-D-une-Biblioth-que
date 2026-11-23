
from views.Views import Views
from repository.AdminRepository import AdminRepository
from repository.EmployeRepository import EmployeRepository
from repository.UtilisateurRepository import UtilisateurRepository
from repository.LivreRepository import LivreRepository
from models.Admin import Admin
from models.Employe import Employe
from models.Utilisateur import Utilisateur
from models.Livre import Livre 



class Controllers :
    
    #Création des instances des instances que le controllers utilisera
    def instance(self):
        self.view = Views()
        self.adminRepository = AdminRepository()
        self.employeRepository = EmployeRepository()
        self.utilisateurRepository = UtilisateurRepository()
        self.livreRepository = LivreRepository()
        return self.view,self.adminRepository,self.employeRepository,self.utilisateurRepository,self.livreRepository
    
    
    #Logique de connexion d'un Employe ou d'un Admin
    def authentification(self):
        view,adminRepository,employeRepository = self.instance()[0],self.instance()[1],self.instance()[2]
        choix = view.interface_connexion()
        if choix == 1 :
            email = "root@gmail.com"
            #Tanque l'email de l'admin ou de l'employer est faux ont lui redemande de resaisir 
            while self.adminRepository.admin_email_verification(email) == True or self.employeRepository.employe_email_verification == True :
                email = self.view.interface_saisie_email_connexion()
                if self.adminRepository.admin_email_verification(email) == False :
                   mot_de_passe = "root"
                   #Tanque le mot de passe de l'admin est faux ont lui redemande de resaisir 
                   while self.adminRepository.admin_mot_de_passe_verification(mot_de_passe,email) == True : 
                        mot_de_passe = self.view.interface_saisie_mot_de_passe_connexion()
                        if self.adminRepository.admin_mot_de_passe_verification(mot_de_passe,email) == False:
                            return 1
                        else :
                          #On affiche un message d'erreur pour le mot de passe admin
                          self.view.message_erreur_mdp()
                elif self.employeRepository.employe_verifier_email(email) == False:
                     mot_de_passe = "root"
                     #Tanque le mot de passe de l'employer est faux ont lui redemande de resaisi
                     while self.employeRepository.employer_verifier_mot_de_passe(mot_de_passe) == True :
                           mot_de_passe =  view.interface_saisie_mot_de_passe_connexion()
                           if self.employeRepository.employer_verifier_mot_de_passe(email,mot_de_passe) == False :
                                return 0
                           else :
                               #On affiche un message d'erreur pour le mot de passe employe
                               self.view.message_erreur_mdp()
                else :
                    #On affiche un message d'erreur pour l'email 
                    self.view.message_erreur_email() 
        elif choix == 0 :
            pass
        
    
    """
    fonctionnalité de gestion des abonnés 
    """
    #On enregistre un abonné
    def abonner_enregistrement(self):
        self.view ,self.utilisateurRepository = self.instance()[0] ,self.instance()[3] 
        numero_abonner,nom,prenom,date_naiss,adresse,statut = self.view.interface_enregistrement_abonner()
        utilisateur = Utilisateur()
        utilisateur_insert = utilisateur.insert(numero_abonner,nom,prenom,date_naiss,adresse,statut)
        self.utilisateurRepository.utilisateur_insert(utilisateur_insert)
    
    #On modifie un abonné
    def abonner_modification(self):
        self.view ,self.utilisateurRepository = self.instance()[0] ,self.instance()[3] 
        self.view.interface_liste_abonner(self.utilisateurRepository.utilisateur_find_all())
        numero_abonner = self.view.interface_saisie_num_abonner_modif()
        if self.utilisateurRepository.utilisateur_find_one_modif(numero_abonner) == False :
            nom,prenom,date_naiss,adresse,statut = self.view.interface_modification_abonner()
            utilisateur = Utilisateur()
            utilisateur_modif = utilisateur.update(nom,prenom,date_naiss,adresse,statut,numero_abonner)
            self.utilisateurRepository.utilisateur_update(utilisateur_modif)
        else :
            pass
    
    #On recherche un abonné par son id 
    def abonner_rechercher_par_id(self):
        self.view ,self.utilisateurRepository = self.instance()[0] ,self.instance()[3] 
        liste_abonner = self.utilisateurRepository.utilisateur_find_all_rech_id()
        self.view.interface_liste_abonner_rech_id(liste_abonner)
        id = self.view.interface_saisie_consultation()
        if self.utilisateurRepository.utilisateur_find_one_id_consult(id) == False :
            abonner = self.utilisateurRepository.utilisateur_find_one(id)
            self.view.interface_consultation_abonner(abonner)
        else:
           pass
    
    #On supprime un abonné
    def abonner_supp_par_id(self):
        self.view ,self.utilisateurRepository = self.instance()[0] ,self.instance()[3] 
        liste_abonner = self.utilisateurRepository.utilisateur_find_all_rech_id()
        self.view.interface_liste_abonner_rech_id(liste_abonner)
        id = self.view.interface_suppression_abonner()
        if self.utilisateurRepository.utilisateur_find_one_id_consult(id) == False :
            self.utilisateurRepository.utilisateur_delete(id)
        else :
            pass
    
    #On affiche tous les abonnés 
    def abonner_afficher_tous(self):
        self.view ,self.utilisateurRepository = self.instance()[0] ,self.instance()[3] 
        liste_abonner = self.utilisateurRepository.utilisateur_find_all()
        self.view.interface_liste_abonner(liste_abonner)
 
        
    #Methode de démarrage de l'application
    def run(self):
      #choix = self.authentification()
      self.view = self.instance()[0]
      reponse = self.authentification()
      if reponse == 1:
           choix = 3
           while choix != 0:
                choix = self.view.menu_principale_admin()
                if choix == 1 :
                   pass
                elif choix == 2 :
                   choix_gestion_abonner = 3
                   while choix_gestion_abonner != 0 : 
                        choix_gestion_abonner = self.view.interface_gestion_abonner()
                        if choix_gestion_abonner == 1 :
                          self.abonner_enregistrement()
                        elif choix_gestion_abonner == 2 :
                           self.abonner_modification()
                        elif choix_gestion_abonner == 3 :
                           self.abonner_rechercher_par_id()
                        elif  choix_gestion_abonner == 4 :
                           self.abonner_supp_par_id()
                        elif choix_gestion_abonner == 5 :
                           self.abonner_afficher_tous()
                        elif choix_gestion_abonner == 6 :
                            pass 
                        elif choix_gestion_abonner == 0 : 
                            break
                elif choix == 0 :
                    pass
      elif reponse == 0 :
            choix = 3
            while choix != 0:
                choix = self.view.menu_principale_employe()
                if choix == 1 :
                   pass
                elif choix == 2 :
                   choix_gestion_abonner = 3
                   while choix_gestion_abonner != 0 : 
                        choix_gestion_abonner = self.view.interface_gestion_abonner()
                        if choix_gestion_abonner == 1 :
                          self.abonner_enregistrement()
                        elif choix_gestion_abonner == 2 :
                           self.abonner_modification()
                        elif choix_gestion_abonner == 3 :
                           self.abonner_rechercher_par_id()
                        elif  choix_gestion_abonner == 4 :
                           self.abonner_supp_par_id()
                        elif choix_gestion_abonner == 5 :
                           self.abonner_afficher_tous()
                        elif choix_gestion_abonner == 0 : 
                            break
                elif choix == 0 :
                    pass