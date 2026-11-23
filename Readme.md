# 📚 Système de Gestion de Bibliothèque

> **Projet d'apprentissage en Python – en cours de développement 🚧**

Bonjour 👋 !
Je suis **Diabagate Hassane Ilias**, étudiant en Licence 2. Ce projet est une application console de gestion de bibliothèque que je construis **seul** pour m'entraîner à écrire du vrai code, structuré comme dans un projet professionnel (architecture en couches, base de données, Git).

⚠️ **Ce projet n'est pas terminé.** Certaines parties fonctionnent, d'autres sont encore en construction ou contiennent des bugs que je dois corriger. Ce README explique honnêtement où j'en suis.

---

## 🎯 Objectif du projet

Permettre à une bibliothèque de :

- gérer ses **livres** (titre, auteur, ISBN, année de publication, nombre d'exemplaires, catégorie, statut) ;
- gérer ses **abonnés** (inscription, modification, consultation, suppression) ;
- enregistrer les **emprunts** et les **retours** de livres ;
- séparer les droits entre un **administrateur** et des **employés**.

---

## 🛠️ Technologies utilisées

| Outil | Utilisation |
|-------|-------------|
| **Python 3** | Langage principal |
| **SQLite** (module `sqlite3`) | Base de données (`Bibliotheques.db`) |
| **Git / GitHub** | Suivi de version |

Aucune bibliothèque externe n'est nécessaire.

---

## 🧱 Architecture du projet

J'ai séparé le code en plusieurs couches pour que chaque fichier ait un seul rôle :

```
ProjetBibliotheque/
├── main.py                  # Point d'entrée de l'application
├── models/                  # Les classes (Admin, Employe, Utilisateur, Livre, Emprunt)
├── repository/              # L'accès à la base de données (requêtes SQL)
├── views/                   # L'affichage et les saisies dans la console (menus)
├── controllers/             # La logique : fait le lien entre vues et repository
├── Entity.txt               # Mes notes de conception (entités, algorithme de connexion)
└── Bibliotheques.db         # Base SQLite (créée automatiquement)
```

**Comment les couches communiquent :**
`main.py` → `Controllers` → `Views` (pour parler à l'utilisateur) et `Repository` (pour parler à la base de données), avec les `Models` pour représenter les données.

---

## 🚀 Avancement

### ✅ Terminé

- [x] Conception de départ (entités, schéma de connexion dans `Entity.txt`)
- [x] Création de la base de données SQLite et des tables **Admin**, **Employe** et **Utilisateur**
- [x] **Authentification** : connexion par email + mot de passe, avec redirection vers le menu Administrateur ou le menu Employé
- [x] Menus principaux (Admin et Employé) et menu de connexion

### 🔄 En cours

- [ ] **Gestion des abonnés** : enregistrement, modification, consultation par id, suppression, affichage de la liste (les fonctions sont écrites, je suis en train de les tester et de les déboguer)
- [ ] **Gestion des livres** : le modèle et le repository sont écrits, mais l'interface et le branchement au contrôleur ne sont pas terminés

### 📝 À faire

- [ ] **Emprunts et retours** de livres (le modèle existe, le repository est encore vide)
- [ ] Consultation de la liste des **emprunts en cours**
- [ ] **Gestion des employés** par l'administrateur
- [ ] Recherche de livres par catégorie
- [ ] Hachage des mots de passe (aujourd'hui ils sont stockés en clair, ce qui est à proscrire en vrai)
- [ ] Gestion des erreurs de saisie (par exemple quand on tape une lettre à la place d'un nombre)
- [ ] Fichier de configuration (`Config.py`) et tests

---

## ▶️ Lancer le projet

1. Cloner le dépôt et se placer dans le dossier :
   ```bash
   cd ProjetBibliotheque
   ```
2. Lancer l'application :
   ```bash
   python main.py
   ```

La base de données et les tables sont créées automatiquement au premier lancement.

> **Note :** il n'y a pas encore de menu pour créer le premier administrateur. Pour l'instant, je l'ajoute à la main depuis un petit script Python :
> ```python
> from repository.AdminRepository import AdminRepository
> AdminRepository().admin_insert(("ADM-001", "admin@exemple.com", "monMotDePasse"))
> ```

---

## 🐞 Problèmes connus (que je dois corriger)

- Dans `Views.py`, la méthode du menu des livres a le même nom que celle du menu des abonnés : la deuxième écrase la première.
- Dans `LivreRepository.py`, il y a des fautes de frappe dans les noms de colonnes (`nombre_exemp` / `nombres_exemp`, `annnee_pub`) et la table `Livre` n'est pas encore créée automatiquement.
- `livre_find_all_categorie` n'envoie pas le paramètre `categorie` à la requête.
- Les mots de passe sont en clair dans la base.

Je préfère les noter ici pour ne pas les oublier : corriger mes erreurs fait partie de l'apprentissage 💪

---

## 📖 Ce que ce projet m'apprend

- Organiser un projet Python en plusieurs couches (modèles, vues, contrôleurs, repository)
- Écrire des requêtes SQL avec `sqlite3` (requêtes paramétrées avec `?`)
- Programmation orientée objet (classes, méthodes)
- Utiliser Git pour sauvegarder l'avancement avec des commits réguliers
- Déboguer, lire les messages d'erreur et améliorer mon code petit à petit

---

## 👤 Auteur

**Diabagate Hassane Ilias**, étudiant en Licence 2, Côte d'Ivoire 🇨🇮

*Projet commencé en novembre 2026 et toujours en cours de développement.*