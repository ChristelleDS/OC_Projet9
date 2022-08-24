# LITReview

Le site est un site de demande et rédaction de critiques de livres. <br/>
Il permet également à chaque utilisateur de s'abonner à des utilisateurs. <br/>

Le site n'est accessible qu'aux utilisateurs ayant crée un compte. <br/>
La page "flux" présente les demandes de critiques et les avis donnés par les utilisateurs suivis. <br/>
La page "posts" présente les éléments rédigés par l'utilisateur connecté. <br/>
La page "Abonnements" permet de s'abonner à un utilisateur et de voir qui sont ses abonnés. <br/>
L'onglet "mon compte" permet d'accéder à une fonctionnalité de changement de mot de passe.


# GITHUB Source Repository

Se positionner dans le répertoire d'installation souhaité: <br/>
$ cd LITReview_repository

Récupérer le code source sur le repository Github : <br/>
$  git clone https://github.com/ChristelleDS/OC_Projet9
 

# Créez un environnement virtuel et l'activer

$ python -m venv env <br/>
$ . env/bin/activate <br/>
$ env/Scripts/Activate (sous windows)

# Installez les dépendances

$ pip install -r requirements.txt


# Initialisez la DB

$ python manage.py makemigrations <br/>
$ python manage.py migrate

# Lancez le serveur de dev

$ cd LITReview_repository     <br/>
$ python manage.py runserver 

Le site sera accessible à l'adresse http://localhost:8000/.


# Interface d'administration du site

Pour créer un compte administrateur: 

$ python manage.py createsuperuser

Un backoffice est accessible  à l'adresse: http://localhost:8000/admin/  <br/>
Il permet d'administrer les comptes utilisateurs ainsi que les publications.
 
 
 ## Technicals notes
 
 Le site utilise certains modules:

* Utilisation de Bootstrap
* Utilisation d'un kit.fontawesome.com pour l'affichage des notes 

# Paramétrage

Répertoire de stockage des images uploadées par les utilisateurs:
FICHIER SETTINGS.PY
* MEDIA_URL = '/media/'
* MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Lors d'une bascule en production, mettre à False le paramétrage suivant:
* DEBUG = True

