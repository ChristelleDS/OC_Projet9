# LITReview

Le site est un site de demande et rédaction de critiques de livres.
Il permet également à chaque utilisateur de s'abonner à des utilisateurs.

Le site n'est accessible qu'aux utilisateurs ayant crée un compte.
La page "flux" présente les demandes de critiques et les avis donnés par les utilisateurs suivis.
La page "posts" présente les éléments rédigés par l'utilisateur connecté.
La page "Abonnements" permet de s'abonner à un utilisateur et de voir qui sont ses abonnés.
L'onglet "mon compte" permet d'accéder à une fonctionnalité de changement de mot de passe.


# GITHUB Source Repository

Se positionner dans le répertoire d'installation souhaité:
$ cd LITReview_repository

Récupérer le code source sur le repository Github :
  -  git clone https://github.com/ChristelleDS/OC_Projet9
 

# Créez un environnement virtuel et l'activer

$ python -m venv env
$ . env/bin/activate
$ env/Scripts/Activate (sous windows)

# Installez les dépendances

$ pip install -r requirements.txt


# Initialisez la DB

$ python manage.py makemigrations
$ python manage.py migrate

# Lancez le serveur de dev

$ cd LITReview_repository
$ python manage.py runserver

Le site sera accessible à l'adresse http://localhost:8000/.


# Interface d'administration du site

Pour créer un compte administrateur:

$ python manage.py createsuperuser

Un backoffice est accessible  à l'adresse: http://localhost:8000/admin/
Il permet d'administrer les comptes utilisateurs ainsi que les publications.
 
 
 ## Technicals notes
 
 Le site utilise certains modules:

* Utilisation de Bootstrap
* Utilisation d'un kit.fontawesome.com pour l'affichage des notes 



