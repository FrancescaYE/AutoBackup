# AutoBackup

## Présentation

AutoBackup est un outil de sauvegarde automatisée développé en Python. Il permet de copier récursivement le contenu d’un dossier local vers un répertoire de sauvegarde, tout en conservant l’organisation des fichiers et sous-dossiers.

Chaque exécution crée une sauvegarde horodatée. L’intégrité des fichiers copiés est ensuite vérifiée à l’aide de l’algorithme de hachage SHA-256.

Ce projet a été réalisé dans le cadre de mon apprentissage de Python et de l’automatisation des tâches informatiques.

## Fonctionnalités

* Vérification de l’existence et de la validité du dossier source.
* Création automatique du répertoire de destination.
* Copie récursive des fichiers et sous-dossiers.
* Création de sauvegardes horodatées.
* Vérification de l’intégrité des fichiers avec SHA-256.
* Gestion des erreurs et exceptions.
* Journalisation des opérations avec le module logging.
* Mode simulation (Dry-run) permettant de visualiser les opérations prévues sans effectuer de copie.

## Technologies utilisées

* Python 3.12
* pathlib
* shutil
* datetime
* hashlib
* logging

Le projet utilise exclusivement la bibliothèque standard de Python. Aucune dépendance externe n’est nécessaire.

## Structure du projet
```
AutoBackup/
├── autobackup.py
├── test_documents/
│   ├── rapport.txt
│   ├── facture.txt
│   └── projets/
│       └── projet1.txt
├── backups/
├── logs/
├── .gitignore
└── README.md

```

Les dossiers backups/ et logs/ sont générés et utilisés lors de l’exécution du programme. Ils sont exclus du dépôt Git.

## Prérequis

* Python 3.12 ou une version compatible.
* Un environnement Linux ou un système disposant des fonctionnalités nécessaires à l’exécution du script.

## Installation et exécution

### 1. Cloner le dépôt :

```git clone https://github.com/FrancescaYE/AutoBackup.git```

### 2. Accéder au répertoire du projet :

```cd AutoBackup```

### 3. Exécuter le script :

```python3 autobackup.py```

### Mode simulation (Dry-run)

Le mode simulation permet d’afficher le dossier source et le chemin de destination prévu sans effectuer de copie.

Pour activer ou désactiver ce mode, modifier la variable dry_run dans le fichier autobackup.py :

dry_run = True  # Mode simulation
dry_run = False  # Sauvegarde réelle

### Journalisation

Les opérations et les erreurs sont enregistrées dans le fichier :

logs/autobackup.log

Cette journalisation permet de conserver un historique des sauvegardes et de consulter les éventuelles erreurs.

### Objectifs pédagogiques

Ce projet m’a permis de mettre en pratique :

* La manipulation des fichiers et répertoires avec Python.
* L’automatisation de tâches système.
* La gestion des exceptions.
* La vérification de l’intégrité des données.
* La journalisation des opérations.
* L’organisation d’un projet Python.

### Auteur

Francesca YETO

GitHub : FrancescaYE
