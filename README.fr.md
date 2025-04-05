# Application d'Utilitaires pour Développeurs (Dev Utils App)

Une application GUI en Python qui fournit diverses fonctionnalités utiles pour les développeurs. Avec une interface moderne et des fonctions pratiques, elle rend le travail de développement plus efficace.

![Capture d'écran de l'application](screenshot.png)

## Fonctionnalités Principales

### Comparaison de Texte (Text Diff)
- Affiche visuellement les différences entre deux textes
- Mise en évidence précise des différences grâce à la comparaison ligne par ligne
- Interface intuitive pour une utilisation facile
- Bouton de réinitialisation pour commencer rapidement un nouveau travail

### Visualiseur JSON
- Visualise les chaînes JSON sous forme de structure arborescente
- Fonctionnalité de repli/déploiement des nœuds pour naviguer facilement dans des structures complexes
- Données d'exemple fournies pour des tests rapides
- Changements automatiques de thème selon le mode clair/sombre

## Stack Technologique

- **Frontend**: CustomTkinter (bibliothèque GUI Python)
- **Algorithme de Comparaison**: bibliothèque diff-match-patch
- **Analyse JSON**: module json intégré à Python
- **Système de Thèmes**: prise en charge des modes clair/sombre

## Configuration Requise

- Python 3.8 ou supérieur
- Les packages Python suivants:
  - customtkinter
  - pillow
  - diff-match-patch

## Installation

### 1. Cloner le Dépôt
```bash
git clone https://github.com/ghdquddnr/dev_utils_app.git
cd dev_utils_app
```

### 2. Configurer l'Environnement Virtuel et Installer les Packages
```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Installer les packages
pip install customtkinter pillow diff-match-patch
```

### 3. Lancer l'Application
```bash
python main.py
```

## Comment Utiliser

### Fonctionnalité de Comparaison de Texte
1. Entrez le texte original dans la zone de texte de gauche.
2. Entrez le texte à comparer dans la zone de texte de droite.
3. Cliquez sur le bouton "Comparer" pour voir les différences entre les deux textes mises en évidence avec des couleurs.
   - Parties supprimées: Fond rouge
   - Parties ajoutées: Fond vert
4. Cliquez sur le bouton "Réinitialiser" pour effacer tout le texte et commencer une nouvelle comparaison.

### Fonctionnalité de Visualiseur JSON
1. Entrez une chaîne JSON dans la zone de texte de gauche.
2. Cliquez sur le bouton "Convertir" pour visualiser le JSON sous forme de structure arborescente à droite.
3. Cliquez sur les boutons + ou - sur les nœuds de l'arbre pour les déployer ou les replier.
4. Utilisez le bouton "Tout Déployer"/"Tout Replier" pour contrôler l'ensemble de l'arbre en une seule fois.
5. Cliquez sur le bouton "Données d'Exemple" pour saisir automatiquement des données JSON d'exemple.
6. Cliquez sur le bouton "Réinitialiser" pour effacer toutes les données.

### Changement de Thème
- Cliquez sur le bouton "Changer de Thème" en bas de la barre latérale pour basculer entre les modes clair et sombre.

## Configuration de l'Environnement de Développement

```bash
# Installer les packages de développement
pip install -e ".[dev]"
```

## Plans Futurs

- Fonctionnalités utilitaires supplémentaires en développement
- Optimisation des performances
- Fonctionnalité de sauvegarde des paramètres utilisateur

## Licence

Ce projet est distribué sous la licence MIT. Pour plus de détails, veuillez consulter le fichier [LICENSE](LICENSE).

## Contribution

Les contributions sont toujours les bienvenues ! Vous pouvez aider à améliorer ce projet grâce à des rapports de bugs, des demandes de fonctionnalités ou des contributions de code. 