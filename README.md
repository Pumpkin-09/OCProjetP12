# Projet P12: Développez une architecture back-end sécurisée avec Python et SQL

Application de gestion de la relation client pour Epic Events, entreprise spécialisée dans l'organisation d'événements pour start-ups.

## 🎯 Fonctionnalités

- Gestion des clients
- Suivi des contrats
- Planification et organisation d'événements
- Système de permissions par rôle (Gestion, Commercial, Support)
- Journalisation avec Sentry

## 🛠️ Technologies

- Python 3.x
- MySQL
- Sentry (monitoring)

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/Pumpkin-09/OCProjetP12.git
cd epicevents
```

### 2. Créer l'environnement virtuel
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate

# Sur macOS/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

**Créer un utilisateur MySQL dédié**

Se connecter à MySQL en root :
```bash
mysql -u root -p
```

Créer l'utilisateur et lui donner les droits nécessaires sur la base epicevents  :
```sql
CREATE USER 'epicevents_user'@'localhost' IDENTIFIED BY 'votre_mot_de_passe_securise';
GRANT SELECT, INSERT, UPDATE, DELETE ON epicevents.* TO 'epicevents_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Importer le schéma avec le nouvel utilisateur :
```bash
mysql -u epicevents_user -p < schema.sql
```

⚠️ **Important :** Pensez à utiliser le même nom d'utilisateur et mot de passe dans votre fichier `.env` à l'étape suivante.

### 5. Créer le fichier .env

**Créer le fichier à la racine du projet :**
```bash
cat > .env << EOF
DB_HOST=localhost
DB_PORT=3306
DB_NAME=epicevents
DB_USER=epicevents_user
DB_PASSWORD=ton_mot_de_passe_mysql
EOF
```

**Modifier les valeurs selon votre configuration :**
```bash
nano .env  # ou vim .env, ou avec votre éditeur préféré
```

### 6. Lancer l'application
Lors de votre tout premier lancement de l'application, un utilisateur "Admin" de l'équipe gestion sera créé automatiquement pour vous permettre de vous connecter et d'utiliser les fonctionnalités implémentées.
Lors du lancement avec la commande :

```bash
python main.py
```

Vous verrez apparaître le message : `Collaborateur Admin créé avec succès`

Il vous sera alors demandé de vous connecter. Utilisez les identifiants de l'utilisateur admin précédemment créé :
- **Email :** admin@epicevents.com
- **Mot de passe :** admin123

⚠️ Important : Pour des raisons de sécurité, pensez à modifier le mot de passe de l'administrateur dès votre première connexion.

## 📋 Utilisation

L'application propose un menu interactif permettant de :
- Gérer les collaborateurs (équipe Gestion)
- Gérer les clients (équipes Commercial et Gestion)
- Gérer les contrats (équipes Commercial et Gestion)
- Gérer les événements (équipes Support et Gestion)

Les permissions sont automatiquement appliquées selon votre rôle.

## 🔒 Sécurité

- Authentification obligatoire
- Mots de passe hashés
- Permissions basées sur les rôles
- Journalisation des erreurs avec Sentry
