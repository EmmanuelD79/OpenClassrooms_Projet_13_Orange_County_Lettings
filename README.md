## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


`docker run --pull=always --env-file ./oc_lettings_site/.env -p 8000:8000 --name oc_lettings79 manu2179/openclassrooms_projet_13_orange_county_lettings:latest`

## Pipeline CI/CD 

### Prérequis

- Avoir un compte github
- Avoir un compte CircleCi
- Avoir un compte Heroku
- Avoir un compte DockerHub
- Avoir un compte SENTRY. io


### Github

Nous avons 2 branches sur ce projet :
- Refactor
- Master

Un push sur la branche Refactor lancera dans CircleCi le build et les tests.

Un push sur la branche Master lancera en plus du build et des tests, le build de l'image du projet avec un push sur le repository de DockerHub et le déploiement sur Heroku.


### CircleCi

Dans le dossier `. circleci`, le fichier `config.yml` est le script du pipeline comprenant les parties :
- build_and_tests -> la construction du projet et le lancement du linter flake8 et des tests avec pytest
- build_and_push_docker_image -> la construction de l'image du projet avec Docker et le dépôt sur le repository de DockerHub. Cette phase est réalisée seulement quand un push vers Master est effectué et seulement si le build et les tests sont réussis.
- deploy -> le déploiement de l’image docker sur Heroku. Le déploiement est effectué seulement lors d’un push sur Master et seulement si les phases précédentes ont été réussies.

#### Prérequis
Lors de la création du compte, il est nécessaire de connecter le compte github avec le compte CircleCi et mettre en place le projet en sélectionnant le repository github.

#### Paramétrage des variables d'environnement

Pour l'exécution du projet, des variables d'environnement sont nécessaires.
Il faut les paramétrer dans le `Project settings` et `Environment Variables`.

Elles sont :

| Name | Description |
|:--------------- |:---------------|
| DOCKER_IMAGE | Nom de l'image Docker |
| DOCKER_PASS | Mot de passe du compte Docker|
| DOCKER_USER | Utilisateur du compte Docker |
| HEROKU_API_KEY | Clé de l'api HEROKU |
| HEROKU_APP_NAME | Nom de l'application sur HEROKU |
| MODE | 'developpement' ou 'production' |
| SECRET_KEY | La clé du projet Django |
| SENTRY_DNS | Le DNS fournit par SENTRY pour le suivi des erreurs |


### HEROKU

HEROKU héberge le projet, il est accessible à l'adresse https://oc-lettings79.herokuapp.com/

#### Prérequis
- Le compte HEROKU doit être actif.
- Le nom de domaine doit être créé.
- l'API KEY doit être généré et accessible dans `Account settings` puis `Account`


#### Déploiement

CircleCi se charge du déploiement du projet sur HEROKU avec la mise en place de l'image docker et le paramétrage des variables d'environnement.


### DOCKERHUB

DOCKERHUB permet d'archiver les différentes images du projet et de les versionner avec des tags.

La dernière version du projet est taguée `latest`.

L’image est récupérable pour un déploiement local par exemple avec la commande :

`docker run --pull=always --env-file ./oc_lettings_site/.env -p 8000:8000 --name oc_lettings79 manu2179/openclassrooms_projet_13_orange_county_lettings:latest`


### SENTRY. io

Le suivi des erreurs est effectué avec SENTRY.

Des alertes sont configurables selon le type d'erreur et selon sa fréquence.

Il est nécessaire d'assigner une personne chargée du débogage en indiquant son adresse mail lors de la création des alertes.

SENTRY est intégré au projet, pour des raisons de sécurité la variable SENTRY_DNS doit être déclaré en variable d'environnement dans CircleCi.

Le DNS est accessible sur le compte SENTRY `SDK SETUP` puis `Client Keys (DNS)`


