# Atelier Python — Persistance des données JSON et CSV

## Présentation du projet

Ce projet a été réalisé dans le cadre de ma formation en Développement IA à **Kadea Academy — Cohorte 2026**.

L'objectif est d'apprendre à sauvegarder et récupérer des données Python à l'aide de fichiers JSON et CSV, sans utiliser de base de données.

## Objectifs pédagogiques

- Comprendre la sérialisation et la désérialisation des données.
- Lire et écrire des fichiers JSON et CSV.
- Utiliser `with open()` pour gérer correctement l'ouverture et la fermeture des fichiers.
- Maîtriser l'encodage UTF-8.
- Gérer les erreurs liées aux fichiers.
- Vérifier la conservation des types de données après lecture.

## Structure du projet

```text
atelier_persistence/
│
├── storage/
│   ├── __init__.py
│   ├── json_storage.py
│   └── csv_storage.py
│
├── data/                  # Fichiers générés (ignorés par Git)
├── .gitignore
├── requirements.txt
├── test_storage.py
└── README.md
```

## Fonctionnalités

### 1. Gestion JSON

Le module `json_storage.py` permet de :

- Sauvegarder une liste de dictionnaires dans un fichier JSON.
- Charger des données JSON.
- Conserver les types Python compatibles avec JSON.
- Retourner une liste vide lorsqu'un fichier est inexistant.
- Détecter un fichier JSON corrompu.
- Gérer les erreurs de permission lors de la sauvegarde.

### 2. Gestion CSV

Le module `csv_storage.py` permet de :

- Exporter des dictionnaires vers un fichier CSV.
- Créer automatiquement les en-têtes des colonnes.
- Importer des données CSV.
- Utiliser l'encodage UTF-8.
- Constater que les valeurs relues depuis un CSV sont des chaînes de caractères.

## Exécution du projet

### 1. Activer l'environnement virtuel

Sous Windows avec PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Installer les dépendances

```powershell
pip install -r requirements.txt
```

### 3. Lancer les tests

```powershell
python test_storage.py
```

## Tests réalisés

Le programme vérifie notamment :

1. La sauvegarde et la lecture des données JSON.
2. La conservation des types `int` et `bool` en JSON.
3. L'exportation et l'importation des données CSV.
4. Le comportement lors de la lecture d'un fichier inexistant.
5. La détection d'un fichier JSON volontairement corrompu.
6. La gestion d'une erreur de permission simulée.

## Technologies utilisées

- Python
- Bibliothèques standard `json`, `csv`, `pathlib`, `logging` et `unittest.mock`
- Git et GitHub
- Visual Studio Code

## Auteur

**KeGrO-cyber**

Apprenant en Développement IA — Kadea Academy, Cohorte 2026.